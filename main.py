import os
from PIL import Image, ImageColor
from flask import Flask, request, redirect, render_template, flash


app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "img"
app.secret_key = 'secret key'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], 'test.jpg'))
            flash("Изображение загружено")
            return redirect(request.url)
    return render_template("index.html")

@app.route('/research-image', methods=['POST'])
def black_or_white():
    image = Image.open('img/test.jpg')
    black = 0
    white = 0
    for pixel in image.getdata():
        if pixel == (0, 0, 0):
            black += 1
        elif pixel == (255, 255, 255):
            white += 1
    if black > white:
        flash("Черных пикселей больше")
    else:
        flash("Белых пикселей больше")
    return render_template("index.html")

@app.route('/find-hex-color', methods=['POST'])
def find_hex_color():
    counter = 0
    image = Image.open('img/test.jpg')
    hex = request.form['hex']
    if len(hex) == 7 and hex[0] == '#':
        hex_to_rgb = ImageColor.getcolor(hex, "RGB")
        for pixel in image.getdata():
            if pixel == hex_to_rgb:
                counter += 1
            else:
                counter = counter
        flash("Количество пикселей выбранного цвета: " + str(counter))
    else:
        flash("Введите hex код цвета состоящий из 7 символов, начиная с #, например: #ffffff")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5002, host='0.0.0.0')


