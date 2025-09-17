import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "models", "audiomodel.pkl")
MODEL_PATH = os.path.abspath(MODEL_PATH)

audio_model = joblib.load(MODEL_PATH)

def predict_audio(features):
    return audio_model.predict([features])[0]
