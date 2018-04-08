from PIL import Image, ImageDraw

#image_file = VisionTesting.image_path_here(



def map_facial_landmarks(image_file, faces, output_file):
    image = Image.open(image_file)
    draw = ImageDraw.Draw(image)

    #points = list()

    for face in faces:
        for landmark in face.landmarks:
            #print(landmark.type)
            pos = landmark.position
            posX = pos.x
            posY = pos.y
            posTuple = (posX,posY)
            posTuple2 = (posX+10,posY+10)
            draw.ellipse((posTuple,posTuple2),'red','red')
            #points.append(posTuple)

    #draw.point(points)

    image.save(output_file)


def map_facial_borderPoly(image_file, faces, output_file):
    image = Image.open(image_file)
    draw = ImageDraw.Draw(image)
    
    for face in faces:
        vertices = face.boundingPoly.vertices
        drawVerts = list()
        for vertex in vertices:
            x = vertex.x
            y = vertex.y
            vertTup = (x,y)
            drawVerts.append(vertTup)
        draw.polygon(drawVerts,'red','red')

    image.save(output_file)
            
            
                                
