import cv2, pickle, os
import faceio

name = input("Name: ").strip()
cam = cv2.VideoCapture(0)
print("Press SPACE to capture, Q to quit")

while True:
    ok, frame = cam.read()
    if not ok:
        break
    cv2.imshow("Enroll", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if key == ord(" "):
        faces = faceio.detect(frame)
        if len(faces) != 1:
            print("Need exactly one face in frame, try again")
            continue
        data = {}
        if os.path.exists("encodings.pickle"):
            with open("encodings.pickle", "rb") as f:
                data = pickle.load(f)
        data[name] = faceio.encode(frame, faces[0])
        with open("encodings.pickle", "wb") as f:
            pickle.dump(data, f)
        print(f"Saved {name}")
        break

cam.release()
cv2.destroyAllWindows()