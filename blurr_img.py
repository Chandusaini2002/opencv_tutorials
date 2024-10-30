import  cv2
img = cv2.imread("/Users/chandusaini/pictures/cv-demo.webp")
if img is None:
    print("img is not found")
else :
    grayscale = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
    blurr_img = cv2.GaussianBlur(grayscale,(5,5),0)
    cv2.imshow("original img",img)
    cv2.imshow("gray img",grayscale)
    cv2.imshow("blurring and smoothing img",blurr_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()