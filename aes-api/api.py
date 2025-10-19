from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY", "default_api_key")

@app.route("/", methods=["GET"])
def index():
    return "AES API is running!"

@app.route("/encrypt", methods=["POST"])
def encrypt():
    api_key = request.headers.get("X-API-KEY")
    if api_key != API_KEY:
        return jsonify({"status": False, "msg": "Unauthorized"}), 401

    data = request.get_json() or request.form
    voucher = data.get("voucherTemp")
    password = data.get("password")

    if not voucher or not password:
        return jsonify({"status": False, "msg": "Missing voucherTemp or password"}), 400

    try:
        # Jalankan aes_main.py dengan 2 argumen
        result = subprocess.run(
            ["python3", "aes_main.py", voucher, password],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return jsonify({"status": False, "msg": result.stderr.strip()}), 500

        output = result.stdout.strip()
        return jsonify({"status": True, "encrypted": output}), 200

    except Exception as e:
        return jsonify({"status": False, "msg": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

