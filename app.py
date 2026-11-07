from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/Google37734168e5868827.html")
def google_verification():
    return send_from_directory(
        app.root_path,
        "Google37734168e5868827.html"
    )
if __name__ == "__main__":
    app.run(debug=True)
