import VisionTesting
import WebcamImageScan
import FaceLandmarkDrawing
import FaceCalculation

#file_path = VisionTesting.image_path_here('webcamPic.jpg')
#file_finish = VisionTesting.image_path_here('webcamPicMarked.jpg')

face_file = VisionTesting.image_path_here('face.jpg')
face_finish= VisionTesting.image_path_here('faceMarked.jpg')

#WebcamImageScan.take_picture_here(file_path)
#faces = VisionTesting.detect_face(file_path)
#FaceLandmarkDrawing.map_facial_landmarks(file_path, faces, file_finish)
face = VisionTesting.detect_face(face_file)
polygons, numFaces = FaceCalculation.map_facial_borderPoly(face)
FaceLandmarkDrawing.map_facial_borderPoly(polygons, numFaces, face_file, face_finish)



