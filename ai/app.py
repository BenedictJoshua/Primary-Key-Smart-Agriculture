from flask import Flask, request, jsonify
from model import predict_crop

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        result = predict_crop(
            data["soil_type"],
            float(data["ph"]),
            float(data["nitrogen"]),
            float(data["phosphorus"]),
            float(data["potassium"])
        )

        return jsonify({
            "success": True,
            "prediction": result
        })

    except Exception as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002)