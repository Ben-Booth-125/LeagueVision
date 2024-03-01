import cv2
import os
import time

root = '../Media/Video'  # Replace with your desired output directory
technique_name = 'walk'
path = f'{root}-{technique_name}'
os.makedirs(f'{path}-16', exist_ok=True)
os.makedirs(f'{path}-8', exist_ok=True)
os.makedirs(f'{path}-1', exist_ok=True)

# Initialize video capture
cap = cv2.VideoCapture(f'{path}.mp4')  # Capture video from default camera

# Buffer to store recorded frames
frame_buffer = []

recording = False
start_time = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video Player', frame)
    key = cv2.waitKey(10) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('r'):
        if not recording:
            print("Begin Recording...")
            recording = True
            start_time = time.time()
        else:
            print("Saving Recording at various FPS")
            recording = False
            if frame_buffer:
                # Save recorded frames as images
                for i, saved_frame in enumerate(frame_buffer[::16]):
                    image_path = os.path.join(f'{path}-16', f"Image-{i + 1}.jpg")
                    cv2.imwrite(image_path, saved_frame)
                print("Saved at 1/16th Frames")
                for i, saved_frame in enumerate(frame_buffer[::8]):
                    image_path = os.path.join(f'{path}-8', f"Image-{i + 1}.jpg")
                    cv2.imwrite(image_path, saved_frame)
                print("Saved at 1/8th Frames")
                for i, saved_frame in enumerate(frame_buffer):
                    image_path = os.path.join(f'{path}-1', f"Image-{i + 1}.jpg")
                    cv2.imwrite(image_path, saved_frame)
                print("Saved all Frames")
                frame_buffer.clear()

    if recording:
        frame_buffer.append(frame)

cap.release()
cv2.destroyAllWindows()