import cv2
from PIL import Image
from util import get_limits

yellow = [0,255,255]
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #индекс кадра и кадр

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #преобразуем кадр из исходного цветового пространства в hvs

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit) #строит маску по предельным значениям на цилиндре hvsй

    

    mask_ = Image.fromarray(mask) #сохраняем ту же инфу, но в другом формате

    bbox = mask_.getbbox()
    
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0),5)

    cv2.imshow('frame', frame) #создаем окно с визуализацией кадра

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() #Освобождаем память

cv2.destroyAllWindows()

