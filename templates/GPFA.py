from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
app.secret_key = 'your_secret_key'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_images():
    files = request.files.getlist('images')

    valid_files = [file for file in files if file.filename != '']

    if len(valid_files) < 3 or len(valid_files) > 10:
        flash('Please upload between 3 and 10 images.')
        return redirect(url_for('index'))

    image_paths = []

    for file in valid_files:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        image_paths.append(filepath)

    return f"Uploaded {len(image_paths)} images successfully."

if __name__ == '__main__':
    app.run(debug=True)