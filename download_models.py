import urllib.request, os

BASE = "https://github.com/opencv/opencv_zoo/raw/main/models/"
FILES = {
    "yunet.onnx": BASE + "face_detection_yunet/face_detection_yunet_2023mar.onnx",
    "sface.onnx": BASE + "face_recognition_sface/face_recognition_sface_2021dec.onnx",
}

os.makedirs("models", exist_ok=True)
for name, url in FILES.items():
    path = os.path.join("models", name)
    if not os.path.exists(path):
        print("Downloading", name)
        urllib.request.urlretrieve(url, path)
print("Done")