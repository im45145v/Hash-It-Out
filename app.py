from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import os
# from function import functions


app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('dashboard.html')

# Specify the upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create the upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if the 'audio_file' file input field is present in the form
    if 'audio_file' not in request.files:
        return "No file part"

    audio_file = request.files['audio_file']

    # Check if the file is empty
    if audio_file.filename == '':
        return "No selected file"

    # Save the uploaded file to the 'uploads' folder
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
    audio_file.save(upload_path)

    # transcribe(audio_file)

    return f"File '{audio_file.filename}' has been uploaded and processed."

if __name__ == '__main__':
    app.run(debug=True)