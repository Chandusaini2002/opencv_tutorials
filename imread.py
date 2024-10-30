import cv2
img = cv2.imread("/Users/chandusaini/Pictures/cv-demo.webp")
if img is None:
    print("img is not found")
else :
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()