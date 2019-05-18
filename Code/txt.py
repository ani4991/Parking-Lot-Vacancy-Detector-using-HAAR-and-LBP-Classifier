import glob
import cv2
f = open("info.dat",'w')

for filename in glob.iglob('negative_training_images\\*.jpg', recursive=True):
    """img=cv2.imread(filename)

    w= img.shape[0]
    h=img.shape[1]"""

    f.write(filename +" 1 0 0 "+str(w)+" "+str(h)+"\n")
    