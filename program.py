#from threading import Thread

import multiprocessing as mp
import face_recognition
import cv2
import numpy as np
from tkinter import *




def inputs(x):
    if x =="1":
        video = cv2.VideoCapture(0)
        address = "url of second video stream"
        video.open(address)
        on_cam = "Cam 2"
        recognise_face(video,on_cam)
    if x =="2":
        video = cv2.VideoCapture(0)
        on_cam = "Cam 2"
        recognise_face(video,on_cam)
        
    else:
        print("something wrong")

def cam1():
    #cam1 = mp.Process(target=inputs("1"),args=[1])
    #cam1.start()
    video = cv2.VideoCapture(0)
    address = "url of second video stream"
    video.open(address)
    face = face_recognition.load_image_file("1.jpg")
    faceencoding = face_recognition.face_encodings(face)[0]

    face_encodings_list = [
        faceencoding]

    face_encodings = []
    s = True
    face_coordinates=[]
    try:

        while True:
            _,frame = video.read()

            resized_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            resized_frame_rgb = resized_frame[:, :, ::-1]


            if s:
                face_coordinates = face_recognition.face_locations(resized_frame_rgb)
                face_encodings = face_recognition.face_encodings(resized_frame_rgb, face_coordinates)

                for faces in face_encodings:
                    matches = face_recognition.compare_faces(face_encodings_list, faces)
                    if matches[0] == True:
                        video.release()
                        cv2.destroyAllWindows()
                        print("found on cam 1 ")
            cv2.imshow('Face Scan', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except:
        print("empty frame")

    video.release()
    cv2.destroyAllWindows()

#def cam2():
#    cam2 = mp.Process(target=inputs("2"),args=[1])
#    cam2.start()




def cam2():
    #cam1 = mp.Process(target=inputs("1"),args=[1])
    #cam1.start()
    video = cv2.VideoCapture(0)
    face = face_recognition.load_image_file("1.jpg")
    faceencoding = face_recognition.face_encodings(face)[0]

    face_encodings_list = [
        faceencoding]

    face_encodings = []
    s = True
    face_coordinates=[]
    try:

        while True:
            _,frame = video.read()

            resized_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            resized_frame_rgb = resized_frame[:, :, ::-1]


            if s:
                face_coordinates = face_recognition.face_locations(resized_frame_rgb)
                face_encodings = face_recognition.face_encodings(resized_frame_rgb, face_coordinates)

                for faces in face_encodings:
                    matches = face_recognition.compare_faces(face_encodings_list, faces)
                    if matches[0] == True:
                        video.release()
                        cv2.destroyAllWindows()
                        print("found on cam 1 ")
            cv2.imshow('Face Scan', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except:
        print("empty frame")

    video.release()
    cv2.destroyAllWindows()








'''

def recognise_face(video,on_cam):

   # video = cv2.VideoCapture(0)

    face = face_recognition.load_image_file("1.jpg")
    faceencoding = face_recognition.face_encodings(face)[0]

    face_encodings_list = [
        faceencoding]

    face_encodings = []
    s = True
    face_coordinates=[]
    try:

        while True:
            _,frame = video.read()

            resized_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            resized_frame_rgb = resized_frame[:, :, ::-1]


            if s:
                face_coordinates = face_recognition.face_locations(resized_frame_rgb)
                face_encodings = face_recognition.face_encodings(resized_frame_rgb, face_coordinates)

                for faces in face_encodings:
                    matches = face_recognition.compare_faces(face_encodings_list, faces)
                    if matches[0] == True:
                        video.release()
                        cv2.destroyAllWindows()
                        print("found on cam 1 ")
            cv2.imshow('Face Scan', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except:
        print("empty frame")

    video.release()
    cv2.destroyAllWindows()
'''

root=Tk()
root.geometry("300x500")
root.config(bg="white")

buttons=Button(root,text="Cam 1 ",command=cam1,borderwidth=0)
buttons.place(x=90,y=10)

sendmessagebutton=Button(root,text="cam 2 ",command=cam2,borderwidth=0)
sendmessagebutton.place(x=260,y=440)


root.mainloop()
os._exit(1)



#cam1 = Thread(target=inputs("1"),args=[1])
#cam1.run()