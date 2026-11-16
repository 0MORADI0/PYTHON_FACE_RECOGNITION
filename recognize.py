#pip install opencv-python face_recognition -i https://mirror-pypi.runflare.com/simple
import cv2, pickle
import faceio
import db
import speaker

THRESHOLD = 0.363
UNKNOWN_FRAMES = 10

db.init()
with open("encodings.pickle", "rb") as f:
    known = pickle.load(f)

cam = cv2.VideoCapture(0)
marked = set()
announced = set()
unknown_frames = 0
print("Press Q to quit")

while True:
    ok, frame = cam.read()
    if not ok:
        break

    has_unknown = False
    for face in faceio.detect(frame):
        enc = faceio.encode(frame, face)
        name, best = "Unknown", 0.0
        for n, k in known.items():
            s = faceio.similarity(enc, k)
            if s > best:
                best = s
                if s >= THRESHOLD:
                    name = n

        if name == "Unknown":
            has_unknown = True
        else:
            if name not in marked:
                if db.mark(name):
                    print(f"Attendance marked: {name}")
                marked.add(name)
            if name not in announced and speaker.announce_known(name):
                announced.add(name)

        x, y, w, h = face[:4].astype(int)
        color = (0, 200, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, name, (x, max(y - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    unknown_frames = unknown_frames + 1 if has_unknown else 0
    if unknown_frames >= UNKNOWN_FRAMES:
        speaker.announce_unknown()

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()