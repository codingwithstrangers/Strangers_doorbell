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
    # Get the video stream from the request
    # Extract the image data from the request's data field
    data_url = request.values['data']
    # Remove the data URI prefix from the image data
    data_url = data_url.split(',')[1]
    data = base64.b64decode(data_url)  # Decode the base64-encoded image data
    # Convert the decoded data to a NumPy array
    image = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)  # Decode the JPEG image

    print('this is working')
    # Save the JPEG frame to disk with a unique filename based on the current timestamp
    filename = "./practiceimages/" + f'frame_{time.time()}.jpg'
    cv2.imwrite(filename, image)

    return 'OK'


def delete_images():
    # this will delete all files in folder practiceimage
    for filename in os.listdir('practiceimages'):
        if filename.endswith('jpg'):
            os.remove(os.path.join('practiceimages', filename))


atexit.register(delete_images)

if __name__ == '__main__':
    # Start the Flask development server
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')
    print('Stranger danger')
