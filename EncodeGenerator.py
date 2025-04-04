import cv2
import face_recognition
import pickle
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#cant use storage because its not part of the free plan (have to pay for it)
#from firebase_admin import storage

#images in resources/modes to list imgmodeList
folderPath = "images"
pathList = os.listdir(folderPath)
imgList = []
studentIds = []

for path in pathList:
  imgList.append(cv2.imread(os.path.join(folderPath, path)))
  studentIds.append(os.path.splitext(path)[0])

  #imports images to storage db (this step doesnt work. storage is not free)
  #fileName = f'{folderPath}/{path}'
  #bucket = storage.bucket()
  #blob = bucket.block(fileName)
  #blob.upload_from_filename(fileName)

#print(len(imgList))
print(studentIds)

def findEncodings(imagesList):
  encodeList = []

  for img in imagesList:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    encodeList.append(encode)

  return encodeList

print("encoding started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("encoding complete")

file = open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("file saved")