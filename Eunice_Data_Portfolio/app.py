from flask import Flask, render_template, send_from_directory, Response, url_for

app = Flask(__name__)


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# GOOGLE VERIFICATION
@app.route("/Google37734168e5868827.html")
def google_verification():
    return send_from_directory(
        app.root_path,
        "Google37734168e5868827.html"
    )


# GOOGLE SITEMAP
@app.route("/sitemap.xml")
def sitemap():
    website_url = url_for("home", _external=True)

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{website_url}</loc>
    </url>
</urlset>"""

    return Response(xml, mimetype="application/xml")


# ROBOTS.TXT
@app.route("/robots.txt")
def robots():
    website_url = url_for("sitemap", _external=True)

    content = f"""User-agent: *
Allow: /

Sitemap: {website_url}
"""

    return Response(content, mimetype="text/plain")


# RUN APPLICATION
if __name__ == "__main__":
    app.run(debug=True)
