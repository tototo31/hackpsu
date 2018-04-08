import VisionTesting
import WebcamImageScan
import FaceLandmarkDrawing
import FaceCalculation

file_path = VisionTesting.image_path_here('webcamPic.jpg')
file_finish = VisionTesting.image_path_here('webcamPicMarked.jpg')

#face_file = VisionTesting.image_path_here('face.jpg')
#face_finish= VisionTesting.image_path_here('faceMarked.jpg')

WebcamImageScan.take_picture_here(file_path)
faces = VisionTesting.detect_face(file_path)
polygons, numFaces = FaceCalculation.map_facial_borderPoly(faces)
#FaceLandmarkDrawing.map_facial_borderPoly(polygons, numFaces, file_path, file_finish)
FaceLandmarkDrawing.crop_face(polygons, numFaces, file_path)


#face = VisionTesting.detect_face(face_file)
#polygons, numFaces = FaceCalculation.map_facial_borderPoly(face)
#FaceLandmarkDrawing.map_facial_borderPoly(polygons, numFaces, face_file, face_finish)
#FaceLandmarkDrawing.crop_face(polygons, numFaces, face_file)



