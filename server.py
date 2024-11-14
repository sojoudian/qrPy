from flask import Flask, send_file
from io import BytesIO
import qrcode

# Generate the QR code
qr = qrcode.make("https://maziar.work")
qr_img = BytesIO()
qr.save(qr_img, format="PNG")
qr_img.seek(0)

# Create the web server
app = Flask(__name__)

@app.route("/qr-code")
def serve_qr():
    qr_img.seek(0)  # Reset pointer in case it's accessed multiple times
    return send_file(qr_img, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
