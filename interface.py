from PIL import Image,ImageTk
from tkinter import Tk, Button,Frame,Label
import cv2 as cv
from numpy import true_divide
window = Tk()

#window title
window.title('dataset')
global i   
#window size
window.geometry('300x200+1+1')

#window color
window.config(background='pink')

window.iconbitmap('E:\\yolo_obj_detction\\aa.ico')


#def fct

    #cv.imwrite(("zzzzz.jpg"),img)
    #cv.waitKey(10)
    #cv.destroyAllWindows()

    #create label


    #create button

i=0
while i<2:
    frm0=Frame(width='300',height='100',background='pink')
    frm0.place(x=1,y=1)
    frm1=Frame(width='150',height='100',background='green')
    frm1.place(x=1,y=100)
    frm2=Frame(width='150',height='100',background='blue')
    frm2.place(x=150,y=100)
    print(i)
    lab = Label( text=str(i),font=('arial bold',30),bg="yellow")
    lab.pack()
    def valider():
        cv.imwrite(("zzzzz.jpg"),img)
    def next():
        cv.imwrite(("eeeeeee.jpg"),img)
    im=(str(i))+".jpg"
    print(im)
    im2=str(i)
    img = cv.imread(im)  
    img=cv.resize(img,(600,300))
    cv.imshow(im2,img)
    butt=Button(frm1,text="next",command=next,font=('arial bold',15),bg="yellow",fg='red')
    butt.place(x=30,y=20)
    
    butt2=Button(frm2,text="valider",command=valider,font=('arial bold',15),bg="yellow",fg='red')
    butt2.place(x=30,y=20)
    #imgg=ImageTk.PhotoImage(Image.open("E:\\yolo_obj_detction\\sort\\(14).jpg"))

    #img=Label(image=img)
    #img.pack()
    #frames
    cv.waitKey(0)
    cv.destroyAllWindows()
    i=i+1
window.mainloop()