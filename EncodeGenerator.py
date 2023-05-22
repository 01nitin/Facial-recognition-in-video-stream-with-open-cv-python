import os
import pickle
import cv2
import face_recognition
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# step-7
cred = credentials.Certificate("service.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-96653-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-96653.appspot.com"
})
# encoding generator
# step 3 I guess
# importing the mode students  images into a list
folderPath = r"D:\8th sem\FaceRecognition\Images"
# folderPath: str = imgFolder
PathList = os.listdir(folderPath)
# print(PathList)
imgList = []
# ['1216' , 1612]
studentId = []

# step 6 --
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    # print(os.path.splitext(path)[0])  # 1216
    studentId.append(os.path.splitext(path)[0])

    # print(studentId) # [1216 1612]

    # this step is to add the images with the dataBase
    # fileName = os.path.join(folderPath, path)
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


# --

# # print(studentId)
# # it will go all images and save it 4 images
def findEncode(imgList):
    allEncode = []
    for img in imgList:
        # open cv take bgr and face recog takes rgb
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        allEncode.append(encode)

    return allEncode


#
# we're calling the function
print("Encoding Started!...")
encodeLstKnown = findEncode(imgList)
encodeLstKnownwithIDs = [encodeLstKnown, studentId]  # it define
print("Encoding Complete!")
#
# it will save in file it's a generation of pickle file and encode all teh images one by one
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeLstKnownwithIDs, file)
file.close()
print('File Saved!')
