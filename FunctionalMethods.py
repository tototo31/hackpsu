import VisionTesting
import WebcamImageScan
import FaceLandmarkDrawing
import FaceCalculation


#Create a cropped image
def crop_faces(fileName):
    face_file = VisionTesting.image_path_here(fileName)
    face = VisionTesting.detect_face(face_file)
    polygons, numFaces = FaceCalculation.map_facial_borderPoly(face)
    FaceLandmarkDrawing.crop_face(polygons, numFaces, face_file)

#TODO test this method
def crop_webcam_faces(fileName):
    file_path = VisionTesting.image_path_here(fileName)
    WebcamImageScan.take_picture_here(file_path)
    parts = file_path.split('\\')
    crop_faces(parts[-1])

def draw_landMarks(fileName):
    face_file = VisionTesting.image_path_here(fileName)
    face_finish= VisionTesting.image_path_here(fileName[:len(fileName)-4]+'Landmarks.jpg')
    face = VisionTesting.detect_face(face_file)
    points, numFaces = FaceCalculation.map_facial_landmarks(face)
    FaceLandmarkDrawing.map_facial_landmarks(points, numFaces, face_file, face_finish)

#TODO test this method    
def draw_webcam_landMarks(fileName):
    file_path = VisionTesting.image_path_here(fileName)
    WebcamImageScan.take_picture_here(file_path)
    parts = file_path.split('\\')
    draw_landmarks(parts[-1])

def crop_faces_landMarks(fileName):
    face_file = VisionTesting.image_path_here(fileName)
    face = VisionTesting.detect_face(face_file)
    points, polygons, numFaces = FaceCalculation.map_facial_landmark_border(face)
    xShift, yShift = FaceLandmarkDrawing.crop_face(polygons, numFaces, face_file)
    newPoints = list()
    for point in points:
        xVal = point[0]-xShift
        yVal = point[1]-yShift
        newPoint = (xVal, yVal)
        newPoints.append(newPoint)
    return newPoints
                    


