from flask import Flask, render_template, Response, request
import cv2
import base64
import numpy as np
import time

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for receiving the video feed data
@app.route('/video_feed', methods=['POST'])
def video_feed():
    # Get the video stream from the request
    data_url = request.values['data'] # Extract the image data from the request's data field
    data_url = data_url.split(',')[1] # Remove the data URI prefix from the image data
    data = base64.b64decode(data_url) # Decode the base64-encoded image data
    image = np.frombuffer(data, dtype=np.uint8) # Convert the decoded data to a NumPy array
    image = cv2.imdecode(image, cv2.IMREAD_COLOR) # Decode the JPEG image

    # Save the JPEG frame to disk with a unique filename based on the current timestamp
    filename = 'C:\\Users\\Huvo\\Desktop\\webcamer\\images\\' + f'frame_{time.time()}.jpg'
    cv2.imwrite(filename, image)

    return 'OK'

if __name__ == '__main__':
    # Start the Flask development server
    app.run(host='0.0.0.0', port=5000, debug=True)
