from flask import Flask, request, jsonify
from ultralytics import YOLO
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

model = YOLO("model/yolov11n.pt")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    results = model(image_path)

    probs = results[0].probs
    cls_id = int(probs.top1)
    cls_name = results[0].names[cls_id]
    confidence = float(probs.top1conf)

    response = {
        "prediction": cls_name,
        "confidence": round(confidence * 100, 2),
        "remedy": "General plant care and disease management recommended"
    }

    print("✅ JSON sent to frontend:", response)  # DEBUG LINE

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
