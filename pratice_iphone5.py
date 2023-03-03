# from flask import Flask, render_template, Response, request
# import cv2
# import base64
# import numpy as np
# import time

# #create the flask app
# app = Flask(__name__)

# #Defines the route for the URL
# @app.route('/')
# def index():
#     #return html
#     return render_template ('ios5.html')

# #runs the Flask app / debug
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000,debug=True, ssl_context='adhoc')

from flask import Flask, render_template, Response, request
import cv2
import base64
import numpy as np
import time
import ssl

#create the flask app
app = Flask(__name__)

#Defines the route for the URL
@app.route('/')
def index():
    #return html
    return render_template ('ios5.html')

# Define the route for the video feed
@app.route('/video_feed', methods=['POST'])
def video_feed():
    # Get the video stream from the request
    data_url = request.values['data'] # Extract the image data from the request's data field
    data_url = data_url.split(',')[1] # Remove the data URI prefix from the image data
    data = base64.b64decode(data_url) # Decode the base64-encoded image data
    image = np.frombuffer(data, dtype=np.uint8) # Convert the decoded data to a NumPy array
    image = cv2.imdecode(image, cv2.IMREAD_COLOR) # Decode the JPEG image

    print('this is working')
    # Save the JPEG frame to disk with a unique filename based on the current timestamp
    filename = "./practiceimages/" + f'frame_{time.time()}.jpg'
    cv2.imwrite(filename, image)

    return 'OK'

if __name__ == '__main__':
    # Configure the Flask app to use TLS
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('cert.pem', 'key.pem')

    # Start the Flask development server with TLS enabled
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=context)
