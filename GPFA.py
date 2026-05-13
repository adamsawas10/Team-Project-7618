from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from colorfilters import grayscale, negative, sepia, saturation, selectivecolor
from group_collage import collage
from imagetools import pallete, brightness, add_RGB

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
    target_color = request.form.get("target_color")
    new_r = request.form.get("new_r")
    new_g = request.form.get("new_g")
    new_b = request.form.get("new_b")
    target = request.form.get("target_format")

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
        elif selected_filter == "brightness":
            filtered_path = brightness(filepath)
        elif selected_filter == "add_RGB":
            filtered_path = add_RGB(filepath, new_r, new_g, new_b)  
        elif selected_filter == "selectivecolor":
            filtered_path = selectivecolor(filepath, target_color)
        else:
            filtered_path = filepath

        image_paths.append(filtered_path)

    image_urls = []

    collage_image = collage(image_paths)

    collage_path = os.path.join(app.config["UPLOAD_FOLDER"], "final_collage.jpg")
    collage_image.save(collage_path)
    colors = pallete(collage_image)
    collage_url = url_for("static", filename="uploads/final_collage.jpg")
    c1 = f"rgb{colors[0]}"
    c2 = f"rgb{colors[1]}"
    c3 = f"rgb{colors[2]}"
    c4 = f"rgb{colors[3]}"
    c5 = f"rgb{colors[4]}"
    #^^^ This just makes it into strings html can use.
    return render_template("results.html", collage_image=collage_url, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)



if __name__ == '__main__':
    app.run(debug=True)

