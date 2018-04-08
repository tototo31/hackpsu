

#This file is to calculate the landmark and border values
#and puts them in text files

def map_facial_landmarks(faces):
    points = list()
    numFaces = 0
    for face in faces:
        numFaces += 1
        for landmark in face.landmarks:
            #print(landmark.type)
            pos = landmark.position
            posX = pos.x
            posY = pos.y
            posTuple = (posX,posY)
            points.append(posTuple)
    return points, numFaces
    



def map_facial_borderPoly(faces):
    polygons = list()
    numFaces = 0

    for face in faces:
        numFaces += 1
        vertices = face.bounding_poly.vertices
        drawVerts = list()
        for vertex in vertices:
            x = vertex.x
            y = vertex.y
            vertTup = (x,y)
            drawVerts.append(vertTup)
        polygons.append(drawVerts)

    return polygons, numFaces



            
            
