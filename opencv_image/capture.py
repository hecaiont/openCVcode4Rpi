import cv2

filename = input('type filename : ')
no = input('type cam no : 0(ir), 1(rgb)')


print(filename, no)

cam = cv2.VideoCapture(int(no))
ret, image = cam.read()


if ret:
    cv2.imwrite('./'+str(filename)+'.jpg', image)
cam.release()
