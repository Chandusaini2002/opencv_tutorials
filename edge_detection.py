import cv2
img = cv2.imread("/Users/chandusaini/pictures/cv-demo.webp")
if img is None:
    print("img is  not  found")
else:
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blurr = cv2.GaussianBlur(gray,(5,5),0)
    edges = cv2.Canny(blurr,100,200)
    cv2.imshow("original img",img)
    cv2.imshow("gray img",gray)
    cv2.imshow("blurr img",blurr)
    cv2.imshow("edges detection",edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()