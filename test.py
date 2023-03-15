from flask import Flask, render_template, Response, request
import cv2
import base64
import numpy as np
import time
import os
import atexit

# app = Flask(__name__)

# # Define the route for the home page


# @app.route('/')
# def index():
#     return render_template('index.html')


# print(" Define the route for receiving the video feed data")


# @app.route('/video_feed', methods=['POST'])
# def video_feed():
#     # Get the video stream from the request
#     # Extract the image data from the request's data field
#     data_url = request.values['data']
#     # Remove the data URI prefix from the image data
#     data_url = data_url.split(',')[1]
#     data = base64.b64decode(data_url)  # Decode the base64-encoded image data
#     # Convert the decoded data to a NumPy array
#     image = np.frombuffer(data, dtype=np.uint8)
#     image = cv2.imdecode(image, cv2.IMREAD_COLOR)  # Decode the JPEG image

#     print('this is working')
#     # Save the JPEG frame to disk with a unique filename based on the current timestamp
#     filename = "./practicevideos/" + f'frame_{time.time()}.jpg'
#     cv2.imwrite(filename, image)

#     return 'OK'

# 

import cv2
import os

# Set the directory containing the frames
frames_dir = r'F:\Coding with Strangers\topflightsecurity\practicevideos'

# Set the output video file name and path
output_path = r'F:\Coding with Strangers\topflightsecurity\video.mp4'

# Get the frame dimensions from the first frame
frame1_path = os.path.join(frames_dir, os.listdir(frames_dir)[0])
frame1 = cv2.imread(frame1_path)
height, width, channels = frame1.shape

# Create a VideoWriter object to write the video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc,30.0, (width, height))

# Loop through each frame in the directory and write it to the video
for filename in sorted(os.listdir(frames_dir)):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        frame_path = os.path.join(frames_dir, filename)
        frame = cv2.imread(frame_path)
        out.write(frame)

# Release the video writer and destroy all windows
out.release()
cv2.destroyAllWindows()


# def delete_images():
#     # this will delete all files in folder practiceimage
#     for filename in os.listdir('practicevideos'):
#         if filename.endswith('jpg'):
#             os.remove(os.path.join('practicevideos', filename))


# atexit.register(delete_images)

# if __name__ == '__main__':
#     # Start the Flask development server
#     app.run(host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')
#     print('Stranger danger')
