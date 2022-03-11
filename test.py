from PIL import Image  
import PIL  
i=1
im="test/("+str(i)+").jpg"
picture = Image.open(im)  
picture = picture.save("dolls.jpg")