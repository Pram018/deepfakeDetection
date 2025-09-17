import joblib
import os
from sklearn.linear_model import LogisticRegression
import numpy as np

# ✅ Save directly to top-level "models" folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

audio_model_path = os.path.join(MODEL_DIR, "audiomodel.pkl")
video_model_path = os.path.join(MODEL_DIR, "videomodel.pkl")

# Dummy training data
X = np.random.rand(10, 5)
y = np.random.randint(0, 2, 10)

# Dummy audio model
audio_model = LogisticRegression()
audio_model.fit(X, y)
joblib.dump(audio_model, audio_model_path)

# Dummy video model
video_model = LogisticRegression()
video_model.fit(X, y)
joblib.dump(video_model, video_model_path)

print(f"✅ Dummy models saved in {MODEL_DIR}")
