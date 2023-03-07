import os
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './practiceimages/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_file = request.files['video']
        if video_file:
            video_filename = video_file.filename
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_filename)
            video_file.save(video_path)

        photo_file = request.files['photo']
        if photo_file:
            photo_filename = photo_file.filename
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo_filename)
            photo_file.save(photo_path)
    return render_template('ios1043.html')

if __name__ == '__main__':
    app.run(ssl_context='adhoc', host='0.0.0.0', port=5000)
