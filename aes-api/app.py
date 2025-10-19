from flask import Flask, request, jsonify
import aes_main
import aes_main_inverse

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"status": "AES API is running"})


@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.get_json()
        plaintext = data.get('plaintext')
        key = data.get('key')

        if not plaintext or not key:
            return jsonify({"error": "plaintext and key are required"}), 400

        result = aes_main.encrypt(plaintext, key)
        cipher = ''.join(result)
        return jsonify({"cipher": cipher})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.get_json()
        ciphertext = data.get('ciphertext')
        key = data.get('key')

        if not ciphertext or not key:
            return jsonify({"error": "ciphertext and key are required"}), 400

        result = aes_main_inverse.decrypt(ciphertext, key)
        plaintext = ''.join(result)
        return jsonify({"plaintext": plaintext})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
