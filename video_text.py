import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")
cap = cv2.VideoCapture('assets/video.mp4')
while (cap.isOpened()):
    _, frame =cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h_img = frame.shape[0]
    w_img = frame.shape[1]
    boxes = pytesseract.image_to_boxes(frame)
    text=''
    for b in boxes.splitlines():
        b = b.split(' ')
        print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(frame, (x, h_img - y), (w, h_img - h), (0, 0, 255), 2)

        #cv2.putText(frame, b[0], (x, h_img - y + 120), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Video', frame)
    text += pytesseract.image_to_string(frame)
    if cv2.waitKey(1)==ord('q'):
        break
print(text)
cap.release()
cv2.destroyAllWindows()