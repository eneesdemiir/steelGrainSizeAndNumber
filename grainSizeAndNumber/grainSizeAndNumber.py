import cv2
import numpy as np

def main():
    min_area = 80
    threshold = 140
    img = cv2.imread('pictures/1.png')
    image = cv2.resize(img, (1000,1000), interpolation = cv2.INTER_AREA)
    blur = cv2.medianBlur(image, 5)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    bitmap = cv2.threshold(gray,threshold,255, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(bitmap, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    blobs = []
    for c in cnts:
        area = cv2.contourArea(c)
        if area > min_area:
            print("Area: " + f'{area:.2f}')
            cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
            blobs.append(c)
    print("Number Of Cells: ",len(blobs))
    cv2.imshow('image', image)
    cv2.waitKey() 

if __name__ == '__main__':
    main()