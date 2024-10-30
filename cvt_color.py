import cv2
img = cv2.imread("/Users/chandusaini/pictures/cv-demo.webp")
if img is None:
    print("img not found")
else:
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("original img",img)
    cv2.imshow("gray img",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()