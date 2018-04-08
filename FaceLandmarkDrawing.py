from PIL import Image, ImageDraw

#image_file = VisionTesting.image_path_here(



def map_facial_landmarks(image_file, faces, output_file):
    image = Image.open(image_file)
    draw = ImageDraw.Draw(image)

    #points = list()

    for face in faces:
        for landmark in face.landmarks:
            print(landmark.type)
            pos = landmark.position
            posX = pos.x
            posY = pos.y
            posTuple = (posX,posY)
            posTuple2 = (posX+10,posY+10)
            draw.ellipse((posTuple,posTuple2),'red','red')
            #points.append(posTuple)

    #draw.point(points)

    image.save(output_file)
                                
