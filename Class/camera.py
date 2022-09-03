import cv2

cap = cv2.VideoCapture(-1)
cap.open(0, cv2.CAP_DSHOW)
cap.set(3, 1280)
cap.set(4, 720)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('urna_teclado3.avi', fourcc, 10.0, (1280, 720))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # write the flipped frame
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()