import cv2
car_detector = cv2.CascadeClassifier('C:\\University Of Houston\\SPRING - 18 Semester 2\\Computer Vision\\Assignment-3\\PKLot\\trial-1LBP(50k)\\cascade.xml')
img = cv2.imread('C:\\University Of Houston\\SPRING - 18 Semester 2\\Computer Vision\\Assignment-3\\PKLot\\parking2\\rainy\\2012-11-10\\2012-11-10_11_12_51.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cars = car_detector.detectMultiScale(gray,scaleFactor =5, minNeighbors = 10, maxSize = (75,75), minSize = (20,20))

for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


