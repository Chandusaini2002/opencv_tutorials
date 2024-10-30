import cv2
img = cv2.imread("/Users/chandusaini/pictures/cv-demo.webp")
if img is None:
    print("img not found")
else:
    resize=cv2.resize(img ,(200,300))
    crop_image = resize[100:250 ,100:250] 
    cv2.imshow("real img",img)
    cv2.imshow("resize img",resize)
    cv2.imshow("crop img",crop_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
