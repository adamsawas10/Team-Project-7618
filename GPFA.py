from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from colorfiltersTEMP import grayscale, negative, sepia, saturation

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
app.secret_key = 'your_secret_key'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload_images():
    files = request.files.getlist("images")
    valid_files = [file for file in files if file.filename != ""]
    selected_filter = request.form.get("filter")

    if len(valid_files) < 3 or len(valid_files) > 10:
        flash("Please upload between 3 and 10 images.")
        return redirect(url_for("index"))

    image_paths = []

    for file in valid_files:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        if selected_filter == "grayscale":
            filtered_path = grayscale(filepath)
        elif selected_filter == "negative":
            filtered_path = negative(filepath)
        elif selected_filter == "sepia":
            filtered_path = sepia(filepath)
        elif selected_filter == "saturation":
            filtered_path = saturation(filepath)
        else:
            filtered_path = filepath

        image_paths.append(filtered_path)

    image_urls = []

    for path in image_paths:
        filename = os.path.basename(path)
        image_urls.append(url_for("static", filename=f"uploads/{filename}"))

    return render_template("results.html", images=image_urls)

if __name__ == '__main__':
    app.run(debug=True)