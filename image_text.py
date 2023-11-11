import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd= (r"C:\Program Files\Tesseract-OCR\tesseract.exe")
img = cv2.imread('assets/7.jpg')
img = cv2.resize(img, (600, 800))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
# print(pytesseract.image_to_boxes(img))
h_img = img.shape[0]
w_img = img.shape[1]
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    #print(b)
    b = b.split(' ')
    x,y,w,h = int(b[1]), int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img, (x,h_img-y), (w, h_img-h), (0,0, 255),1)
    cv2.putText(img, b[0], (x, h_img-y+20), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255),2)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()