import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "models", "videomodel.pkl")
MODEL_PATH = os.path.abspath(MODEL_PATH)

video_model = joblib.load(MODEL_PATH)

def predict_video(features):
    return video_model.predict([features])[0]
