import cv2
import numpy as np 

from PIL import Image,ImageTk
from tkinter import Tk, Button,Frame,Label
window = Tk()

#window title
window.title('dataset')

#window size
window.geometry('600x400+30+30')

#window color
window.config(background='pink')

window.iconbitmap('E:\\yolo_obj_detction\\aa.ico')



# Load Yolo model from open cv
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
# Load coco names dataset
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Loading image
t=1
while t<100:
    im="test/("+str(t)+").jpg"
    img = cv2.imread(im)    
    height, width, _ = img.shape
    count=0
    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    # input
    net.setInput(blob)
    outs = net.forward(output_layers)
    #th output after the forward

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
        
            class_id = np.argmax(scores)
        
            confidence = scores[class_id]
            vehicles = [ 'car','truck','motorbike','bus' ]
            if (classes[class_id] in vehicles):
            #if (classes[class_id]=="car") or (classes[class_id]=="truck")or (classes[class_id]=="bicycle"):
            # Object detected
                
                print("confi",confidence)
                print(class_id,"class id")
                #print("scores",scores)
                print(detection)
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                print(detection[0])
                print(detection[1])
                print(detection[2])
                print(detection[3])
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    print(indexes)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            count=count+1
            x, y, w, h = boxes[i]
            #label = str(classes[class_ids[i]])
            label = str(confidences[i])
            label2 = str(classes[class_ids[i]])
            #color = colors[class_ids[i]]
            color=(0,0,255)
            color2=(255,0,0)
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 1, color2, 2)
            cv2.putText(img, label2, (x, y + h-10), font, 1, color2, 2)
    label3= str(count)
    scale_percent = 50 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    cv2.putText(img, label3, (int(width/2), 100 ), font,4, color, 4)
    def valider():
    
        cv2.imwrite("sort/("+str(t)+").jpg",img)
        #cv2.imshow("Image", resized)
    #imggg=ImageTk.PhotoImage(Image.open("sort\\("+str(t)+").jpg"))
   
    #cv2.imshow("Image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    def next():
        t=t+1
    
    