# capture video from webcam and save into memory
import cv2

video = cv2.VideoCapture(0)  #0 means , the camera of laptop
# 1 means the external camera

# DIVX , XVID , MJPG , X264 ,WMV1 , WMV2 
fourcc = cv2.VideoWriter_fourcc(*"XVID") 

#IT contains 4 parameters  , name , codec , fps(frame/sec) , resolution
output = cv2.VideoWriter("output.avi", fourcc, 110.0 ,(700,500), 0)
print("cap:",video)


while video.isOpened():
        
    # here are two values one is boolean (ret) and another is image (frame)

        ret, frame = video.read()
        if ret == True:
                
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.flip(frame,-1)
            cv2.imshow("frame",frame)
            cv2.imshow("gray:",gray)
            # output.write(frame)
            output.write(gray)
            if cv2.waitKey(1) & 0xFF == ord("m") :

                # here 0 means image and 1 means video(dynamic )
                break
video.release()  
output.release()  
cv2.destroyAllWindows()    
