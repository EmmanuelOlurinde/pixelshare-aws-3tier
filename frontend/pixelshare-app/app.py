from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET"])
def index():
    images = os.listdir(UPLOAD_FOLDER)
    return render_template("index.html", images=images)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["photo"]
    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)
    return redirect(url_for("index"))

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return app.send_static_file(os.path.join("uploads", filename))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)