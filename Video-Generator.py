import cv2
from PIL import Image
import os


path = 'C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Pictures for Video-Generator'
os.chdir(path)

av_h = 0
av_w = 0

length = len(os.listdir('.'))
for i in os.listdir('.'):
    img = Image.open(os.path.join(path,i))
    width,height = img.size
    av_h += height
    av_w += width

av_h = av_h//length
av_w = av_w//length

for i in os.listdir('.'):
    if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
        img = Image.open(os.path.join(path,i))
        width,height = img.size
        print(width,height)
        img_resized = img.resize((av_w,av_h),Image.LANCZOS)
        img_resized.save(i,"png",quality=95)

def generate_video():
    video_name = "Slideshow Video.mp4"
    os.chdir(path)
    images = []
    for i in os.listdir("."):
        if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
            images.append(i)
    frame = cv2.imread(os.path.join(".",images[0]))
    height,width,layers = frame.shape
    video=cv2.VideoWriter(video_name,0,1,(width,height))
    for i in images:
        video.write(cv2.imread(os.path.join(".",i)))
    cv2.destroyAllWindows()
    video.release()

generate_video()


#print(os.listdir('.')) #Prints a list of items in the current directory

