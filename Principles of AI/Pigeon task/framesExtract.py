import cv2
import os

# Define folder path containing videos
folder_path = './Videos'
output_folder = 'Frames'
os.makedirs(output_folder, exist_ok=True)

# Frame extraction interval (in seconds)
frame_interval = 3
frameCount = 0

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.mp4') or filename.endswith('.avi') or filename.endswith('.mov'):
        video_path = os.path.join(folder_path, filename)
        
        # Load the video
        cap = cv2.VideoCapture(video_path)
        
        # Get the frame rate of the video
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        
        # Initialize frame count
        count = 0
        
        # Loop through frames
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Extract frame at the defined interval
            if count % (fps * frame_interval) == 0:
                frame_name = os.path.join(output_folder, f'frame_{frameCount}.jpg')
                cv2.imwrite(frame_name, frame)
                print(f'Extracted: {frame_name} from {filename}')
                frameCount += 1
            
            count += 1
        
        cap.release()

print('Frame extraction completed.')
