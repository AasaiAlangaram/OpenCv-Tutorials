import cv2

img_path = 'C:\\Users\\aasai\\Desktop\\Logo\\5.png'

img = cv2.imread(img_path)

# cv2.imshow('original_image',img)

print('row,column,no.of.channels:',img.shape)

# Parameters for cv2.rectangle function
start_point = (10,10)
end_point = (100,100)
blue,green,red = 255,0,0
color = (blue,green,red)
thickness = 5

img = cv2.rectangle(img,start_point,end_point,color,thickness)
# cv2.imshow('Image_with_rectangle',img)

# Parameters for cv2.circle function
location = (200,180)
blue,green,red = 0,255,0
color = (blue,green,red)
radius = 30
thickness = 10
img = cv2.circle(img,location,radius,color,thickness)
# cv2.imshow('Image_with_circle',img)

# Parameters for cv2.line function
start_point = (10,400)
end_point = (500,500)
blue,green,red = 255,0,255
color = (blue,green,red)
thickness = 10
img = cv2.line(img,start_point,end_point,color,thickness)
# cv2.imshow('Image_with_line',img)

text = 'Hit the Like Button!'
location = (200,420)
font_style = cv2.FONT_ITALIC
font_size = 1
blue,green,red = 255,255,255
color = (blue,green,red)
thickness = 3
img = cv2.putText(img,text,location,font_style,font_size,color,thickness)
cv2.imshow('img with all drawings',img)

cv2.waitKey(0)

cv2.destroyAllWindows()

