# capture video from webcam and save into memory
import cv2
camera = "http://192.168.1.9:8080"

video = cv2.VideoCapture(0)  #0 means , the camera of laptop
# 1 means the external camera
video.open(camera)
print("check== ",video.isOpened())
# DIVX , XVID , MJPG , X264 ,WMV1 , WMV2 
fourcc = cv2.VideoWriter_fourcc(*"XVID") 

#IT contains 4 parameters  , name , codec , fps(frame/sec) , resolution
output = cv2.VideoWriter("output.mp4", fourcc, 110.0 ,(700,500), 0)
# print("cap:",video)


while video.isOpened():
        
    # here are two values one is boolean (ret) and another is image (frame)

        ret, frame = video.read()
        if ret == True:
            frame = cv2.resize(frame,(700,300))
                
            cv2.imshow("frame",frame)
            output.write(frame)
            if cv2.waitKey(1) & 0xFF == ord("m") :

                # here 0 means image and 1 means video(dynamic )
                break
video.release()  
output.release()  
cv2.destroyAllWindows()    
