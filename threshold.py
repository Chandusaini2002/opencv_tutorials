import cv2
img = cv2.imread("/Users/chandusaini/pictures/cv-demo.webp")
if img is None:
    print("img is not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _,threshold = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    cv2.imshow("original img",img)
    cv2.imshow("grayscale img",gray)
    cv2.imshow("threshold img",threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()