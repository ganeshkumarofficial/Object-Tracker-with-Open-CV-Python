"""Access IP Camera in Python OpenCV"""
import cv2

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def drawBox():
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(frame,(x,y),((x+w),(y+h)),(40,0,255),3,1)
    cv2.putText(frame, 'Tracking', (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

stream = cv2.VideoCapture('http://ganesh:Ganesh007@26.1.154.28:8080/video')
#tracker = cv2.TrackerMOSSE_create()
tracker = cv2.TrackerCSRT_create()
ret, frame = stream.read()
box = cv2.selectROI('Tracking',frame,False)
tracker.init(frame,box)


while True:
    timer = cv2.getTickCount()
    ret, frame = stream.read()
    ret, bbox = tracker.update(frame)
    print(bbox)
    #frame = rescale_frame(frame, percent=50)
    if ret:
        drawBox()
    else:
        cv2.putText(frame, 'Lost', (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(frame,'FPS: '+str(int(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
    cv2.putText(frame, 'Press "q" to Exit', (750, 470), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 145, 255), 1)
    cv2.putText(frame, 'A Pro by Ganesh', (750, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.imshow('Webcam',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #cv2.destroyAllWindows()
        break
