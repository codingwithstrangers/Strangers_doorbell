# flask_code.py

from flask import Flask, render_template, Response, request
import cv2
import base64
import numpy as np
import time
import os

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index2.html')

# Route for receiving video frames
@app.route('/video_feed', methods=['POST'])
def video_feed():
    # Get the base64-encoded image data from the request
    data_url = request.values['data']
    # Remove the data URI prefix
    data_url = data_url.split(',')[1]
    # Decode the base64 data
    data = base64.b64decode(data_url)
    # Convert the decoded data to a NumPy array
    image = np.frombuffer(data, dtype=np.uint8)
    # Decode the JPEG image
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Save the JPEG frame to disk with a unique filename based on the current timestamp
    path1 = r'F:\Coding with Strangers\topflightsecurity\practicevideos'
    path2 = f'frame_{time.time()}.jpg'
    filename = os.path.join(path1, path2)
    cv2.imwrite(filename, image)

    return 'OK'

# Route for receiving audio data
@app.route('/audio_feed', methods=['POST'])
def audio_feed():
    # Get the audio data from the request
    audio_data = request.files['audio_data']
    # Save the WAV audio to disk with a unique filename based on the current timestamp
    path1 = r'F:\Coding with Strangers\topflightsecurity\practiceaudio'
    path2 = f'audio_{time.time()}.wav'
    filename = os.path.join(path1, path2)
    audio_data.save(filename)

    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')
