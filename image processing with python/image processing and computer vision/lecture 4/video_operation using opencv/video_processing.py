import cv2

video = cv2.VideoCapture("clg.mp4")
print("video:",video)

while True:
# here are two values one is boolean (ret) and another is image (frame)

    ret, frame = video.read()
    frame = cv2.resize(frame,(500,400))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("gray:",gray)
    k = cv2.waitKey(20)
    if k == ord("m") & 0xFF:
        break
video.release()    
cv2.destroyAllWindows()    
