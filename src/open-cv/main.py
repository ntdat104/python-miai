import cv2
import imutils

SAMPLE_IMG = "src/open-cv/assets/sample.png"

# ------------------
# Đọc ảnh
# image = cv2.imread(SAMPLE_IMG, cv2.IMREAD_GRAYSCALE)
# image = cv2.imread(SAMPLE_IMG)

# # Show Ảnh
# cv2.imshow("Anh", image)

# # Dừng màn hình
# cv2.waitKey()

# # Đóng các cửa sổ
# cv2.destroyAllWindows()

# ------------------
# camera_id = 'src/open-cv/assets/sample.avi'
# camera_id = 0
# # Mở camera
# cap = cv2.VideoCapture(camera_id)
# # Đọc ảnh từ camera
# while True:
#     # Đọc ảnh
#     ret, frame = cap.read()
#     # Hiện ảnh
#     cv2.imshow('Cam', frame)
#     # Kiểm tra nếu bấm Q thì thoát
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# # Giải phóng camera
# cap.release()
# cv2.destroyAllWindows()

# ---------------
# image = cv2.imread(SAMPLE_IMG, cv2.IMREAD_GRAYSCALE)
# cv2.imwrite('src/open-cv/assets/sample_gray.png', image)

# ---------------
# image = cv2.imread(SAMPLE_IMG)
# cv2.imshow("Anh mau", image)
# cv2.waitKey()
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Anh xam", image_gray)
# cv2.waitKey()
# image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imshow("Anh hsv", image_hsv)
# cv2.waitKey()
# cv2.destroyAllWindows()

# ---------------
# image = cv2.imread(SAMPLE_IMG)
# cv2.imshow("Anh mau", image)
# cv2.waitKey()
# # image_resize = cv2.resize(image, dsize=(200,200))
# image_resize = cv2.resize(image, dsize=None, fx=0.5, fy=0.5)
# cv2.imshow("Anh resize", image_resize)
# cv2.waitKey()
# cv2.destroyAllWindows()

# ---------------
# image = cv2.imread(SAMPLE_IMG)
# cv2.imshow("Anh mau", image)
# cv2.waitKey()

# image_rotate = imutils.rotate(image, 90)
# cv2.imshow("Anh rotate", image_rotate)
# cv2.waitKey()
# cv2.destroyAllWindows()

# ---------------
# image = cv2.imread(SAMPLE_IMG)
# cv2.imshow("Anh mau", image)
# cv2.waitKey()
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# ret, thresh_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow("Anh threshold", thresh_binary)
# cv2.waitKey()
# cv2.destroyAllWindows()

# ---------------
# image = cv2.imread(SAMPLE_IMG)
# cv2.imshow("Anh mau", image)
# cv2.waitKey()
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(image_gray, threshold1=50, threshold2=200)
# cv2.imshow("Anh edges", edges)
# cv2.waitKey()
# cv2.destroyAllWindows()

# ---------------
# image = cv2.imread(SAMPLE_IMG)
# cv2.imshow("Anh mau", image)
# cv2.waitKey()
# blur = cv2.GaussianBlur(image, ksize=(31,31), sigmaX=0)
# cv2.imshow("Anh blur", blur)
# cv2.waitKey()
# cv2.destroyAllWindows()

# ----------------
# camera_id = 0
# video = cv2.VideoCapture(camera_id)

# while True:
#     ret, frame = video.read()
#     if ret:
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow("Anh tu webcam", frame)
#     if cv2.waitKey(1) == ord ('q'):
#         break
# video.release()
# cv2.destroyAllWindows()

# ---------------
camera_id = 'src/open-cv/assets/sample.avi'
video = cv2.VideoCapture(camera_id)
rotate = 0

while True:
    ret, frame = video.read()
    if ret:
        if (rotate != 0):
            frame = imutils.rotate(frame, rotate)
        cv2.imshow("Anh tu webcam", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('a'):
        rotate = rotate + 90
    elif key == ord('d'):
        rotate = rotate - 90
video.release()
cv2.destroyAllWindows()
