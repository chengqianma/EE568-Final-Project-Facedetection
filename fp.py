import cv2 as cv
import numpy as np
from tkinter import filedialog
def ip():
    global file_path
    file_path = filedialog.askopenfilename()
    #face_mask(file_path)

def face_mask():
    global file_path
    i = cv.imread(file_path)
    gray = cv.cvtColor(i,cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(
       gray,
       scaleFactor = 1.1,       
       minNeighbors = 10,
       minSize = (100,100),
       flags = cv.CASCADE_SCALE_IMAGE
    )

    sample = 30
    for(x,y,w,h) in faces:
        #cv.rectangle(i,(x,y),(x+w,y+w),(0,255,0),2)
        a = i[y+10:y+h-10,x+10:x+w-10]
        b = a[::sample,::sample]
        for c in range(b.shape[0]):
            for j in range(b.shape[1]):
                i[y+10+c*sample:sample+y+c*sample,x+10+j*sample:sample+x+j*sample]=b[c,j]
            
   #i[y+10:y+h-10,x:x+w,1]=np.random.normal(size=(h-20,w))
   #i[y+10:y+h-10,x:x+w,2]=np.random.normal(size=(h-20,w))
    cv.namedWindow("image",0);
    cv.resizeWindow("image",640,960)
    cv.imshow("image",i)
    cv.waitKey(0)

def ip2():
    global file_path2
    file_path2 = filedialog.askopenfilename()


def face_mask2():
    global file_path
    global file_path2
    i = cv.imread(file_path)
    gray = cv.cvtColor(i,cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(
       gray,
       scaleFactor = 1.1,       
       minNeighbors = 10,
       minSize = (100,100),
       flags = cv.CASCADE_SCALE_IMAGE
    )

    i2 = cv.imread(file_path2)
    x2, y2 = i2.shape[0:2]
   

    #cv.imshow("",p2)
    
    d = 0
    e = 0
    for(x,y,w,h) in faces:
        #a = i[y+10:y+h-10,x+10:x+w-10]
        p2 = cv.resize(i2,(w,h),fx = w/x2,fy = h/y2)
        for m in range(y,y+h-1):
            for n in range(x,x+w-1):
                i[m][n] = p2[d][e]
                e = e + 1
            e = 0
            d = d + 1
        d = 0
    cv.namedWindow("1",0);
    cv.resizeWindow("1",1920,1080)
    cv.imshow("1",i)
    cv.waitKey(0)
"""
def face_mask3():
    global file_path
    i = cv.imread(file_path)
    gray = cv.cvtColor(i,cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(
       gray,
       scaleFactor = 1.1,       
       minNeighbors = 10,
       minSize = (100,100),
       flags = cv.CASCADE_SCALE_IMAGE
    )

    
    for(x,y,w,h) in faces:
        d = 0
        e = 0
        p3 = np.zeros((w-1,h-1),dtype = 'int32')
        for m in range(y,y+h-1):
            for n in range(x,x+w-1):
                p3[d][e] = i[m][n]
                e = e + 1
            e = 0
            d = d + 1
        p3 = handdraw(p3)
        d = 0
        e = 0
        for m in range(y,y+h-1):
            for n in range(x,x+w-1):
                i[m][n] = p3[d][e]
                e = e + 1
            e = 0 
            d = d + 1
    cv.namedWindow("1",0);
    cv.resizeWindow("1",1920,1080)
    cv.imshow("1",i)
    cv.waitKey(0)
"""  
    
def handdraw():
    global file_path
    im = cv.imread(file_path)
    gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY) # Turned the image into gray level
    data = np.array(gray).astype('float')   # Tranform it into float type 
    dp = 15. # the range is (10-100)
    grad = np.gradient(data)
    gradx, grady = grad
    gradx = gradx*dp/100
    grady = grady*dp/100
    a = np.sqrt(gradx**2 + grady**2 + 1.)
    ux = gradx/a
    uy = grady/a
    uz = 1./a
    ve = np.pi/2.2
    va = np.pi/4.
    dx = np.cos(ve)*np.cos(va)
    dy = np.cos(ve)*np.sin(va)
    dz = np.sin(ve)
    
    result = 255*(dx*ux + dy*uy + dz*uz)
    result = np.clip(result,0,255)
    result = result.astype('uint8')
   
    cv.namedWindow("1",cv.WINDOW_NORMAL)
    cv.resizeWindow("1",1920,1080)
    cv.imshow("1",result)
    cv.waitKey(10)    
