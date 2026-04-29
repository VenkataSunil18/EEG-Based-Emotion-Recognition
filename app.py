from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
import os

app = Flask(__name__)

# ✅ Use .h5 file
MODEL_PATH = os.path.join("model", "model.h5")

# ✅ Check if file exists
if not os.path.exists(MODEL_PATH):
    print("❌ Model file not found at:", MODEL_PATH)
    exit()

# ✅ Load model (compatible with TF 2.10)
model = tf.keras.models.load_model(MODEL_PATH, compile=False)
print("✅ EEG Emotion Model Loaded Successfully")

# ✅ Emotion mapping
EMOTION_MAP = {
    0: "Neutral",
    1: "Happy",
    2: "Sad",
    3: "Angry"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # ✅ Ensure correct shape (important for EEG model)
        features = np.array(data['features']).reshape(1, 14, 1)

        prediction = model.predict(features)
        confidence = float(np.max(prediction) * 100)
        predicted_class = int(np.argmax(prediction))

        return jsonify({
            "predicted_class": predicted_class,
            "predicted_emotion": EMOTION_MAP.get(predicted_class, "Unknown"),
            "confidence": round(confidence, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)