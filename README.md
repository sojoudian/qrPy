
# qrPy

A simple Python web server to generate and serve a QR code that links to [https://maziar.work](https://maziar.work).

## Repository
- GitHub: [qrPy](https://github.com/sojoudian/qrPy.git)

## Description
This project uses Python and Flask to create a web server that serves a QR code image. The QR code, when scanned, will redirect to the website [https://maziar.work](https://maziar.work).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sojoudian/qrPy.git
   cd qrPy
   ```

2. Install the required packages:
   ```bash
   pip install "Flask" "qrcode[pil]"
   ```

## Usage

Run the Flask server to start serving the QR code:

```bash
python server.py
```

Once the server is running, visit `http://127.0.0.1:5000/qr-code` in your web browser to view the QR code.

## File Structure
- `server.py`: The main script to run the Flask server and serve the QR code.

## Author
- **sojoudian**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

