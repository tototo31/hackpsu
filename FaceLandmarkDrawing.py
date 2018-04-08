from PIL import Image, ImageDraw


#This file calculates the landmarks and border and draws onto the image

#image_file = VisionTesting.image_path_here(



def map_facial_landmarks(points, numFaces, image_file, output_file):
    image = Image.open(image_file)
    draw = ImageDraw.Draw(image)

    faceNum = 0

    for face in faces:
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
    
    for face in faces:
        faceNum+=1
        drawVerts = polygons[faceNum-1]
        draw.polygon(drawVerts,'red','red')

    image.save(output_file)
            
            
                                
