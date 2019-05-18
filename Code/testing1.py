import cv2
import os
import xml.etree.ElementTree as ET
import glob
cas_path = 'C:\\University Of Houston\\SPRING - 18 Semester 2\\Computer Vision\\Assignment-3\\PKLot\\trial-1LBP(50k)\\cascade.xml'
img_path = 'C:\\University Of Houston\\SPRING - 18 Semester 2\\Computer Vision\\Assignment-3\\PKLot\\parking1b\\rainy\\2013-04-12\\2013-04-12_17_55_13.jpg'
car_detector = cv2.CascadeClassifier(cas_path)
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold = 60
cars = car_detector.detectMultiScale(gray,scaleFactor = 1.7, minNeighbors = 8, minSize = (20,20), maxSize = (75,75))
tp = 0
fp = 0
for (xc,yc,w,h) in cars:
    cv2.rectangle(img,(xc,yc),(xc+w,yc+h),(0,0,255),2)

cv2.imwrite("result18LBP(50k).jpg",img)
xml_path = os.path.splitext(img_path)[0] + '.xml'
for filename in glob.iglob(xml_path, recursive=False):

    tree = ET.parse(filename)
    root = tree.getroot()

    dictoc = {}
    ctrp = 0
    ctrn = 0

    for space in root.findall('space'):
         id = space.get('id')
         oc = space.get('occupied')
         if (oc == '1'):
             ctrp = ctrp + 1
         else:
             ctrn = ctrn + 1
             #if(oc == '1'):
         dictoc[id] = []
         x1 = []
         y1 = []
         for point in space.iter('point'):
             x = point.attrib.get('x')
             y = point.attrib.get('y')
             dictoc[id].append((int(x),int(y)))
             x1.append(int(x))
             y1.append(int(y))
         xmin = min(x1)
         ymin = min(y1)
         xmax = max(x1)
         ymax = max(y1)
         len = xmax - xmin
         wid = ymax - ymin
         area1 = len * wid
         for (xc, yc, w, h) in cars:
             area2 = w * h
             if (((xmin + xmax) / 2) > xc and ((xmin + xmax) / 2) < xc + w and ((ymin + ymax) / 2) > yc and ((ymin + ymax) / 2) < yc + h):
                 ratio = area2/area1
                 #print(q)
                 if ((ratio*100) > threshold):
                     if(oc=='1'):
                         tp = tp + 1
                         break
                     elif(oc=='0'):
                         fp = fp + 1
                         break



    fn = ctrp - tp
    tn = ctrn - fp
    print("cars detected",tp+fp)
    print("vacant spots detected",tn+fn)
    print(tp,fp,tn,fn)
    accuracy = ((tp + tn) / (tp + tn + fp + fn)) * 100
    print(accuracy)