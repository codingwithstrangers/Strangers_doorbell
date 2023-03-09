from flask import Flask, render_template, Response, request
import cv2
import base64
import numpy as np
import time
import os
import atexit

app = Flask(__name__)

# Define the route for the home page


@app.route('/')
def index():
    return render_template('button.html')

        
print(" Define the route for receiving the video feed data")


@app.route('/video_feed', methods=['POST'])
def video_feed():
    print('this is a test if the video is working video feed')
    # Get the video stream from the request
    # Extract the image data from the request's data field
    data_url = request.values['data']
    # Remove the data URI prefix from the image data
    data_url = data_url.split(',')[1]
    data = base64.b64decode(data_url)  # Decode the base64-encoded image data
    # Convert the decoded data to a NumPy array
    image = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)  # Decode the JPEG image
    height, width, channels = image.shape

    #make video writer, if not created

    if not hasattr(video_feed,'video_writer'):
        filename = f"./practice/video_{time.time()}.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = 20
        video_feed.video_writer = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    # print('this is working')
    # # Save the JPEG frame to disk with a unique filename based on the current timestamp
    # filename = "./practiceimages/" + f'frame_{time.time()}.jpg'
    # cv2.imwrite(filename, image)
    
    #write the current image to video file
    video_feed.video_writer.write(image)
    return 'OK'


# def delete_images():
#     # this will delete all files in folder practiceimage
#     for filename in os.listdir('practiceimages'):
#         if filename.endswith('jpg'):
#             os.remove(os.path.join('practiceimages', filename))
# atexit.register(delete_images)


@app.route('/download_video')
def download_video():
    print('video downloaded')
    #read whole video file (does this work durning buffering)
    video_bytes = b''
    filename = "Stuff.mp4"
    # for filename in os.listdir('practicevideos'):
    #     if filename.endswith('mp4'):
    print('did the file create')
    with open (os.path.join('praticevideos',filename), 'rb') as f:
        video_bytes += f.read()
    # return "ok"


if __name__ == '__main__':
    # Start the Flask development server
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')
    print('Stranger danger')




# from flask import Flask, render_template
# from flask_socketio import SocketIO

# app = Flask(__name__)
# socketio = SocketIO(app)

# # Render the index.html template
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Listen for WebRTC signaling messages from the client
# @socketio.on('message')
# def handle_message(message):
#     # Broadcast the signaling message to all clients
#     socketio.emit('message', message, broadcast=True)

# if __name__ == '__main__':
#     socketio.run(app)



# from flask import Flask, render_template, Response, request
# import cv2

# app = Flask (__name__)

# def gen_frame():
#     cap = cv2.VideoCapture()
#     while True:
#         #reads a frame of the video to check if feed is alive
#         success, frame = cap.read()
#         if not success:
#             #if there is no frame in video the code will break
#             break
#             break
#         else:
#             # Convert the frame to JPEG format
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             # Yield the frame in bytes
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
# #release the video objject captured
#     cap.release()

# # this will make a hompage button
# @app.route('/')
# def index():
#     return render_template('index.html')

# #this rounte streamthe video from camera to client
# @app.route('/download_video')
# def download_video():
#     #capture the video default
#     cap = cv2.VideoCapture(0)
#     #define codec to create a videowriter
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     filename= 'output.avi'
#     out = cv2.VideoWriter('./practiceimages/' + filename, fourcc, 20,(640,480))

#     while True:
#         #read the frame from video
#         success , frame = cap.read()
#         if not success:
#             # if there is nothing to read break that shit
#             break
#         else:
#             #write the frame if missing 
#             out.write(frame)
#     #release video
#     cap.release()
#     out.release()

#     #return message that shit worked
#     return 'video was saved ./practiceimages/' + filename
# if __name__ == '__main__':
#     app.run(debug=True)



# import base64
# import numpy as np
# import time
# import os
# import atexit

# app = Flask(__name__)

# # Define the route for the home page


# @app.route('/')
# def index():
#     return render_template('button.html')


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
#     filename = "./practiceimages/" + f'frame_{time.time()}.jpg'
#     cv2.imwrite(filename, image)

#     return 'OK'


# def delete_images():
#     # this will delete all files in folder practiceimage
#     for filename in os.listdir('practiceimages'):
#         if filename.endswith('jpg'):
#             os.remove(os.path.join('practiceimages', filename))


# atexit.register(delete_images)

# if __name__ == '__main__':
#     # Start the Flask development server
#     app.run(host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')
#     print('Stranger danger')
