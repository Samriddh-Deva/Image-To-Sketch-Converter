import cv2

path="C://Users/samri/Downloads/LGMVIP-DataScience-main/f1.jpg"
image = cv2.imread(path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

inverted_image = 255 - gray_image

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
image=cv2.resize(image,(512,512))
pencil_sketch=cv2.resize(pencil_sketch,(512,512))
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)