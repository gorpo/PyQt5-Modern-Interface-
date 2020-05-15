import face_recognition
import cv2
import numpy as np

"""
Para este codigo rodar direto dele basta comentar ou remover o "return face_names"
Caso queira rodar este codigo de forma externa, basta dar um return no face_names na linha 63 e ele retorna o nome 

codigo de exemplo para chamar este script com return:
---------------------------------------------------------
from testes_gorpo import teste
a = teste()
b = 1
while b:
    if a == ['gorpo']:
        print('gato D+')
        b = b - 1
    else:
        pass
-----------------------------------------------------------

"""

def teste():
    video_capture = cv2.VideoCapture('http://localhost:4747/video')
    # Load a sample picture and learn how to recognize it.
    gorpo_image = face_recognition.load_image_file("gorpo.jpg")
    gorpo_face_encoding = face_recognition.face_encodings(gorpo_image)[0]
    # Load a second sample picture and learn how to recognize it.
    biden_image = face_recognition.load_image_file("biden.jpg")
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
    # Create arrays of known face encodings and their names
    known_face_encodings = [
        gorpo_face_encoding,
        biden_face_encoding
    ]
    known_face_names = [
        "gorpo",
        "Joe Biden"
    ]
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

            #return face_names

        process_this_frame = not process_this_frame
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        # Display the resulting image
        cv2.imshow('Video', frame)




        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()


teste()
