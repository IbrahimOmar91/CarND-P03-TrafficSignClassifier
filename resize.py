import cv2
import glob

for i, img in enumerate(glob.glob('myData/*.jpg')):
    image = cv2.imread(img)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (32, 32))
    print ('32\\' + img.split('\\')[1].split('.')[0] + '.png')    
    cv2.imwrite( '32\\' + img.split('\\')[1].split('.')[0] + '.png' , image)
    