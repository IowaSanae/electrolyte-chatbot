from flask import Flask, request, jsonify
from model_connect import model_train
from helper import remove_input_string
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=["GET", "POST"])
def index():
    return jsonify("Hello, World!")


@app.route("/generate", methods=["POST"])
def generate_response():
    try:
        data = request.get_json(force=True)
        input_text = data.get("input_text", "")
        response = model_train(input_text)

        for i in range(len(response)):
            response[i]["generated_text"] = remove_input_string(input_text, response[i]["generated_text"])

        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
