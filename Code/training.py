import xml.etree.ElementTree as ET
import cv2
import glob
import os
ctr = 0
for filename in glob.iglob('C:\\University Of Houston\\SPRING - 18 Semester 2\\Computer Vision\\Assignment-3\\PKLot\\*\\sunny\\*\\*.xml', recursive=True):

    tree = ET.parse(filename)
    root = tree.getroot()

    dict = {}

    for space in root.findall('space'):
         id = space.get('id')
         oc = space.get('occupied')
         if(oc == '1'):
             dict[id] = []
             for point in space.iter('point'):
                 x = point.attrib.get('x')
                 y = point.attrib.get('y')
                 dict[id].append((int(x),int(y)))

         #x.clear()

    #print(dict)
    fname = os.path.splitext(filename)[0]
    img = cv2.imread(fname + ".jpg")
    for i in dict.keys():
        x1=[d1 for (d1,d2) in dict[i]]
        y1=[d2 for (d1,d2) in dict[i]]
        xmin = min(x1)
        ymin = min(y1)
        xmax = max(x1)
        ymax = max(y1)
        crop_img = img[ymin-10:ymax+10, xmin-5:xmax+5]
        cv2.imwrite("C:\\University Of Houston\\SPRING - 18 Semester 2\\Computer Vision\\Assignment-3\\training-images\\cropped" + str(ctr) + ".jpg", crop_img)
        ctr = ctr+1