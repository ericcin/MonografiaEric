import cv2
from matplotlib import pyplot as plt


WIDTH = 1280
HEIGHT = 720

capture = cv2.VideoCapture(-1)
capture.open(0, cv2.CAP_DSHOW)

capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

writer = cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (WIDTH, HEIGHT))

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = capture.get(cv2.CAP_PROP_FPS)

print(width, height, fps)

while True:
    ret, frame = capture.read()
    if ret:
        cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

capture.release()
writer.release()
cv2.destroyAllWindows()

