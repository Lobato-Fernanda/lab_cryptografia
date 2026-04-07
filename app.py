from flask import Flask, render_template, request
from crypto_utils import generate_rsa_keys, encrypt_message, decrypt_message

app = Flask(__name__)

private_key, public_key = generate_rsa_keys()

@app.route("/", methods=["GET", "POST"])
def index():
    encrypted = None
    decrypted = None

    if request.method == "POST":
        message = request.form["message"]

        encrypted_msg, encrypted_key = encrypt_message(message, public_key)

        decrypted_msg = decrypt_message(
            encrypted_msg,
            encrypted_key,
            private_key
        )

        encrypted = encrypted_msg
        decrypted = decrypted_msg

    return render_template(
        "index.html",
        encrypted=encrypted,
        decrypted=decrypted
    )

if __name__ == "__main__":
    print("INICIANDO SERVIDOR...")
    app.run(debug=True)