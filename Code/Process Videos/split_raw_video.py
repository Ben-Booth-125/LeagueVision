import cv2

def split_video_to_frames(video_path, output_folder):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Read the first frame
    success, frame = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)
    target_fps = 8
    increment = int(fps / target_fps)

    count = 0

    while success:
        success, frame = video.read()

        frame = cv2.resize(frame, (256, 128))
        # Save the frame as a JPG image
        cv2.imwrite(f"{output_folder}/frame_{count}.jpg", frame)
        # Read the next frame
        count += 1
        video.set(cv2.CAP_PROP_POS_FRAMES, count * increment)

    # Release the video file
    video.release()

game = 0
video_path = f"Media/Video-walk.mp4"
output_folder = f"Media/LoLgames2024/g{game}"

# Call the function to split the video into frames
split_video_to_frames(video_path, output_folder)