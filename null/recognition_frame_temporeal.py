import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
from time import sleep

key = cv2.waitKey(1)
webcam = cv2.VideoCapture('http://192.168.0.4:4747/mjpegfeed')  # bote 0 caso use webcam do pc ou endereço da camera
sleep(2)

while True:
    try:
        check, frame = webcam.read()
        # print(check)  # prints true as long as the webcam is running
        # print(frame)  # prints matrix values of each framecd

        bbox, label, conf = cv.detect_common_objects(frame,confidence=0.25, model='yolov3')#0.25  model="yolov3"
        output_image = draw_bbox(frame, bbox, label, conf)


        cv2.imshow("Capturando", output_image)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(filename='images/captura.jpg', img=frame)
            webcam.release()
            print("Processando...")


        elif key == ord('k'):
            imagem = cv2.imread('images/captura.jpg')
            convertida = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
            bbox, label, conf = cv.detect_common_objects(convertida)
            output_image = draw_bbox(convertida, bbox, label, conf)
            plt.imshow(output_image)
            plt.show()



        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break

    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break






