from flask import Flask, request, jsonify
from model_train import model
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=["GET", "POST"])
def index():
    return jsonify("Hello, World!")


@app.route("/generate", methods=["POST"])
def generate_response():
    input_text = request.json["input_text"]
    response = model(input_text, do_sample=True, max_length=100)[0]["generated_text"]
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
