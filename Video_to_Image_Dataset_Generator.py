import cv2
import numpy as np
import os
import random

def extract_frames_from_video(video_path, output_folder, num_frames_per_second=10):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    fps = int(video.get(cv2.CAP_PROP_FPS))

    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Choose 'num_frames_per_second' random frames from the video
    frame_indices = sorted(random.sample(range(total_frames), num_frames_per_second * fps))

    frame_count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break

        if frame_count in frame_indices:
            output_path = os.path.join(output_folder, f"{frame_count}.jpg")
            cv2.imwrite(output_path, frame)

        frame_count += 1

    video.release()

def extract_frames_from_videos(video_folder, output_folder, num_frames_per_second):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for video_name in os.listdir(video_folder):
        video_path = os.path.join(video_folder, video_name)
        if os.path.isfile(video_path) and video_path.endswith(".mp4"):
            extract_frames_from_video(video_path, output_folder, num_frames_per_second)

if __name__ == "__main__":
    video_folder = "/home/takmashhido/Downloads/FlameNet/Car_fire_videos"
    output_folder = "/home/takmashhido/Downloads/FlameNet/Car_fire_videos/own_dataset"
    num_frames_per_second = 10
    extract_frames_from_videos(video_folder, output_folder, num_frames_per_second)
