import cv2
img = cv2.imread("/Users/chandusaini/pictures/cv-demo.webp")
if img is None:
    print ("img is not found")
else:
    resize = cv2.resize(img , (400,400))
    cv2.imshow("original img",img)
    cv2.imshow("resize img",resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
