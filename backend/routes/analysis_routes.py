from flask import Blueprint, request, jsonify
from backend.services.video_service import predict_video
from backend.services.audio_service import predict_audio
from backend.utils.preprocess_video import preprocess_video
from backend.utils.preprocess_audio import preprocess_audio




analysis_bp = Blueprint('analysis_bp', __name__)

@analysis_bp.route('/analyze_video', methods=['POST'])
def analyze_video():
    file = request.files['file']
    prediction = predict_video(file)
    return jsonify({'prediction': prediction})

@analysis_bp.route('/analyze_audio', methods=['POST'])
def analyze_audio():
    file = request.files['file']
    prediction = predict_audio(file)
    return jsonify({'prediction': prediction})
