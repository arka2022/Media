import time

import cv2
import os


def ExtractImages(vid_src,img_dest,frame_interval):
    sec=0
    try:
        # creating a folder named data
        if not os.path.exists(img_dest):
            os.makedirs(img_dest)
    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    currentFrame=0
    vid = cv2.VideoCapture(vid_src)
    while(True):
        #read from frame
        ret,frame=vid.read()
        if ret:
            # finding the frame rate
            fps = vid.get(cv2.CAP_PROP_FPS)

            for i in range(int(fps)):
                #create images till video is left
                #img_name=img_dest+'/img'+str(currentFrame)+'.jpg'
                img_name = img_dest + '/img' + str(sec)+'frame'+str(i) + '.jpg'
                print('Creating..'+img_name)
                #write extracted images
                cv2.imwrite(img_name,frame)

            currentFrame += fps * frame_interval
            # Skip to next specific i/p seconds
            vid.set(cv2.CAP_PROP_POS_FRAMES, currentFrame)
            #Update second
            sec=sec+frame_interval

            #currentFrame+=1
        else:
            break
    vid.release()
    cv2.destroyAllWindows()

video_source="England_India.mp4"
image_destination_location="data"
frameInterval_sec=5

ExtractImages(video_source,image_destination_location,frameInterval_sec)


def readImages(location,time,frame):
    frame1=frame+1
    i_name=location+'/'+'img'+str(time)+'frame'+str(frame1)+'.jpg'
    print(i_name)
    image=cv2.imread(i_name,1)
    #print(image)
    cv2.imshow('image', image)
    k = cv2.waitKey(0)
    if k==27:
         cv2.destroyAllWindows();
    elif k==ord('s'):
         cv2.destroyAllWindows();

#readImages(image_destination_location,2,2)




