import cv2

# it will open live camera 
cap = cv2.VideoCapture(0)
i = 0 

while(cap.isOpened()):
    ret , frame = cap.read()

    if ret == False:
        break

# Save Frame by Frame into disk using imwrite method
    cv2.imwrite('./data/Frame'+str(i)+'.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()   