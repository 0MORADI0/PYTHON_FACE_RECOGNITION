import cv2

DETECTOR_PATH = "models/yunet.onnx"
RECOGNIZER_PATH = "models/sface.onnx"

detector = cv2.FaceDetectorYN.create(DETECTOR_PATH, "", (320, 320), 0.8, 0.3, 5000)
recognizer = cv2.FaceRecognizerSF.create(RECOGNIZER_PATH, "")

def detect(frame):
    h, w = frame.shape[:2]
    detector.setInputSize((w, h))
    _, faces = detector.detect(frame)
    return [] if faces is None else faces

def encode(frame, face):
    aligned = recognizer.alignCrop(frame, face)
    return recognizer.feature(aligned)

def similarity(a, b):
    return recognizer.match(a, b, cv2.FaceRecognizerSF_FR_COSINE)