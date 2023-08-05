import sys
import os
from PIL import Image

#__new__='__main__'
image=sys.argv[1]
new=sys.argv[2]
print (image,new)
if not os.path.exists(new):
    os.makedirs(new)
    
for i in os.listdir(image):
    img=Image.open(f'{image}{i}')
    clean_img=os.path.splitext(i)[0]
    img.save(f'{new}{clean_img}.png','png')
    print("image converted")

