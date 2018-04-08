from PIL import Image, ImageDraw


#This file calculates the landmarks and border and draws onto the image

#image_file = VisionTesting.image_path_here(



def map_facial_landmarks(points, numFaces, image_file, output_file):
    image = Image.open(image_file)
    draw = ImageDraw.Draw(image)

    faceNum = 0

    for j in range(numFaces):
        faceNum+=1
        for i in range(35):
            posTuple = points[i*faceNum]
            posTuple2 = (posTuple[0]+10,posTuple[1]+10)
            draw.ellipse((posTuple,posTuple2),'red','red')

    image.save(output_file)


def map_facial_borderPoly(polygons, numFaces, image_file, output_file):
    image = Image.open(image_file)
    draw = ImageDraw.Draw(image)

    faceNum = 0
    
    for j in range(numFaces):
        faceNum+=1
        drawVerts = polygons[faceNum-1]
        draw.polygon(drawVerts,outline='red')

    image.save(output_file)


def crop_face(polygons, numFaces, image_path):
    for i in range(numFaces):
        image = Image.open(image_path)
        xVals = list()
        yVals = list()
        drawVerts = polygons[i]
        for val in drawVerts:
            xVals.append(val[0])
            yVals.append(val[1])
        xMin = min(xVals)
        xMax = max(xVals)
        yMin = min(yVals)
        yMax = max(yVals)
        boxTup = (xMin,yMin,xMax,yMax)
        cropImage = image.crop(boxTup)
        cropImage.save(image_path[:len(image_path)-4]+str(i)+'.jpg') 
        
            
            
            
                                
