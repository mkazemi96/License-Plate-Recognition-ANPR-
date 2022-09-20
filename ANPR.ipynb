# Automatic number Plate Recognition

import cv2
import imutils
import pytesseract

image=cv2.imread('test3.jpg')
resized_image = imutils.resize(image, width=300 )
cv2.imshow("original image",resized_image)
cv2.waitKey(0)

#### converting image to grayscale

gray_image=cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",gray_image)
cv2.waitKey(0)

#### reducing noise in grayscale image

filtered_image=cv2.bilateralFilter(gray_image,11,17,17)
cv2.imshow("filtered image",filtered_image)
cv2.waitKey(0)

edged = cv2.Canny(filtered_image, 30, 200) 
cv2.imshow("edged image", edged)
cv2.waitKey(0)

cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
image1=resized_image.copy()
cv2.drawContours(image1,cnts,-1,(0,255,0),3)
cv2.imshow("contours",image1)
cv2.waitKey(0)

cnts = sorted(cnts, key = cv2.contourArea, reverse = True) [:30]
screenCnt = None
image2 = resized_image.copy()
cv2.drawContours(image2,cnts,-1,(0,255,0),3)
cv2.imshow("Top 30 contours",image2)
cv2.waitKey(0)

for c in cnts:
    perimeter=cv2.arcLength(c , True)
    if len(cv2.approxPolyDP(c, 0.018 * perimeter, True))==4:
        print("****")

 perimeter=cv2.arcLength(cnts[1], True)
len(cv2.approxPolyDP(c, 0.018 * perimeter, True))

i=7
for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4: 
                print("**")
                screenCnt = approx
                x,y,w,h = cv2.boundingRect(c) 
                new_img=resized_image[y:y+h,x:x+w]
                cv2.imwrite('./'+str(i)+'.png',new_img)
                i+=1
                break

detected_license=cv2.drawContours(resized_image, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("image with detected license plate", detected_license)
cv2.waitKey(0)

Cropped_loc = './7.png'
cv2.imshow("cropped", cv2.imread(Cropped_loc))
cv2.waitKey(0)

import base64
with open('./7.png', "rb") as image:
    b64string = base64.b64encode(image.read())



cv2.destroyAllWindows()

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'

# Cropped_loc = './7.png'
# cv2.imshow("cropped", cv2.imread(Cropped_loc))
plate = pytesseract.image_to_string(Cropped_loc, lang='eng')
print("Number plate is:", plate)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

