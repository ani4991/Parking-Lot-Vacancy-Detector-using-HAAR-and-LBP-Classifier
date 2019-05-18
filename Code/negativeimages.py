import cv2
import glob
ctr=0
for filename in glob.iglob('C:\\University Of Houston\\SPRING - 18 Semester 2\\Computer Vision\\Assignment-3\\101_ObjectCategories\\*\\*.jpg', recursive=True):
    img = cv2.imread(filename)
    cv2.imwrite("C:\\University Of Houston\\SPRING - 18 Semester 2\\Computer Vision\\Assignment-3\\PKLot\\negative_training_images_2\\negative" + str(ctr) + ".jpg",img)
    ctr = ctr+1