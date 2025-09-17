import cv2

def preprocess_video(cap):
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # resize frame
        frame = cv2.resize(frame, (224,224))
        frames.append(frame)
    return frames
