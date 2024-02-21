import cv2
import time

root = '../Media/FirstVid'
# Initialize video capture
cap = cv2.VideoCapture(f'{root}.mp4')  # Replace with your video file path

# Buffer to store recorded frames
frame_buffer = []

recording = False
start_time = None
num_vids = 0

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
            num_vids += 1
            recording = True
            start_time = time.time()
        else:
            print("Saving Recording Now...")
            recording = False
            if frame_buffer:
                # Save recorded frames to a new video file
                out = cv2.VideoWriter(f'{root}/Recording-{num_vids}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame.shape[1], frame.shape[0]))
                for saved_frame in frame_buffer:
                    out.write(saved_frame)
                out.release()
                frame_buffer.clear()
            print("Finished Saving")

    if recording:
        frame_buffer.append(frame)

cap.release()
cv2.destroyAllWindows()