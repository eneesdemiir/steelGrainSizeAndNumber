import cv2

threshold = 140 # this changes pic-to-pic
numberOfLines=10 # how many line you want to draw
imageFile='pictures/1.png'
width=900 # image width after resizing
height=900 # image height after resizing

def main():
    pixelDifOfEachLine=height//(numberOfLines+1)
    startPixel=pixelDifOfEachLine
    img = cv2.imread(imageFile)  # image file
    image = cv2.resize(img, (width,height), interpolation = cv2.INTER_AREA)
    blur = cv2.medianBlur(image, 5)
    blur2 = cv2.medianBlur(blur, 5) ## this picture needs double blur
    gray = cv2.cvtColor(blur2, cv2.COLOR_BGR2GRAY)
    bitmap = cv2.threshold(gray,threshold,255, cv2.THRESH_BINARY)[1]
    backToRgbForLines = cv2.cvtColor(bitmap,cv2.COLOR_GRAY2RGB)
    countOfHorizontalRisingEdge=0
    countOfVerticalRisingEdge=0
    print("Calculation started from the upper-left side!")
    print("Horizontal Lines Starting!")
    for Y in range(startPixel,width-1,pixelDifOfEachLine): # horizontal lines
        countOfRisingEdge = 0
        for X in range(0,height):
            backToRgbForLines[Y][X]=(255,0,0)
            locatedPixel = bitmap[Y][X-1]
            nextPixel = bitmap[Y][X]
            if(locatedPixel==255 and nextPixel==0): # white to black 
                countOfHorizontalRisingEdge+=1
                countOfRisingEdge +=1
    
        print("Y:",Y," finished!")
        print("How Many Edges Passed On This Line : ",countOfRisingEdge)
    
    print("Horizontal Lines DONE!")
    print("------------------------")
    print("Vertical Lines Starting!")
    for X in range(startPixel,height-1,pixelDifOfEachLine): # vertical lines
        countOfRisingEdge = 0
        for Y in range(0,width):
            backToRgbForLines[Y][X]=(255,0,0)
            locatedPixel = bitmap[Y-1][X]
            nextPixel = bitmap[Y][X]
            if(locatedPixel==255 and nextPixel==0): # white to black 
                countOfVerticalRisingEdge+=1
                countOfRisingEdge +=1
        print("X:",X," finished!")
        print("How Many Edges Passed On This Line : ",countOfRisingEdge)
    print("Vertical Lines DONE!")
    print("------------------------")
    print("How Many On Y (Horizontal)? :",countOfHorizontalRisingEdge)
    print("How Many On X (Vertical)? :",countOfVerticalRisingEdge)
    cv2.imshow('backToRgb', backToRgbForLines)
    
    cv2.imshow('bitmap', bitmap)
    cv2.waitKey() 

if __name__ == '__main__':
    main()