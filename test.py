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

def create_video():
    #read all the Jpgs
    filenames = [os.path.join('practicevideos', f) for f in os.listdir('practicevideos')if f.endswith('.jpg')]
    #sort images by by ttime stamp (line 56 for now)
    sorted_filenames = sorted(filenames)
    #read the first frame
    frame = cv2.imread(filenames[0])
    height, width, layers = frame.shape
    #creat video you need to source then output it (this is so dumb and it better work)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v") 
    video = cv2.VideoWriter('output.mp4', fourcc,30, (width, height))
    #make the Loop
    for filename in filenames:
        frame = cv2.imread(filename)
        video.write(frame)

    #call the video
    video.release()
    return "ok"
    #prove this shit works by making calll that 
    atexit.register(create_video)
create_video()



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
