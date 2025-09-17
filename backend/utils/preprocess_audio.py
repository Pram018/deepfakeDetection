import numpy as np
import librosa

def preprocess_audio(y, sr):
    # simple MFCC features
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc = np.mean(mfcc.T, axis=0)
    return mfcc
