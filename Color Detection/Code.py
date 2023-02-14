import pandas as pd #this is just used to read the dataset
import cv2 #this is used to read the image





#the dataset used here is downloded from kagale the link is here itself https://www.kaggle.com/datasets/adityabhndari/color-detection-data-set
index = ["Color","Color_Name","Hexadecimal_value","r","g","b"]
dataset = pd.read_csv('colors.csv',names=index,header=None)





imagepath = r'TEAM EMERGENCE.jpg'


#we have created an object 'image' image here and we are just reading the image
image = cv2.imread(imagepath)




#declaring the global variables
clicked = False
r=g=b=xpos=ypos=0




#as the dataset contains almost 864 rows i.e. the dataset not have all the color values there we need to chooose the color such that the r,g,b value is nearest to the any colour and it will return that color

def get_colorname(r,g,b):
  minimum=10000 #i.e. here we have taken the min threshold value as 10000

  for i in range(len(dataset)):
    d = abs(r-int(dataset.loc[i,"r"])) + abs(g-int(dataset.loc[i,"g"])) + abs(b-int(dataset.loc[i,"b"]))
    if d<=minimum:
      minimum=d
      Color_Name=dataset.loc[i,"Color_Name"]
  return Color_Name

  #here the abs function will return the absolute value that is the if the value is -ve it will make it +ve




#function to get x,y coordinates of mouse double click i.e when we click with left
#button of our mouse then it will return some x and y position this function will return those position
def draw_func(event,x,y,flags,param):
  if event == cv2.EVENT_LBUTTONDBLCLK:
    global b,g,r,xpos,ypos,clicked
    clicked=True
    xpos = x
    ypos = y
    b,g,r = image[y,x]
    b=int(b)
    g=int(g)
    r=int(r)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_func)



while True:
  cv2.imshow("image",image)
  if clicked:
    # cv2.rectangle(image,start point,endpoint,color,thickness and rgb values),-1 fills entire rectangle
    cv2.rectangle(image,(20,20),(750,60),(b,g,r),-1)

    #creating text string to display (color name and rgb values)
    text = get_colorname(r,g,b)+' R = '+str(r)+' G = '+str(g)+' B = '+str(b)

    #cv2.puttext(image,text,start,font(0-7),fontscale,color,thickness,linetype)
    cv2.putText(image,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

    #for very light colors we will display text in black color

    if r+g+b>=600:
      cv2.putText(image,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)

    clicked=False


 # exit the loop when the user hits the exsit key

  if cv2.waitKey(20) | 0xFF==27:
   break

cv2.destroyWindows()

