from flask import Flask, request
import os

UPLOAD_FOLDER = 'test/'
ALLOWED_EXTENSIONS = {'tif', 'tiff'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(request):
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    directory = 'test/'
    # Iterate over all files and folders in the directory
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            os.remove(file_path)  # Remove file
        for name in dirs:
            dir_path = os.path.join(root, name)
            os.rmdir(dir_path)  # Remove directory
    if file and allowed_file(file.filename):
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return 'File uploaded successfully', 200
    else:
        return 'Invalid file format', 400

