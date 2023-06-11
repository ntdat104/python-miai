import cv2
import imutils

# Đọc ảnh
def read_image(image):
    source_image = cv2.imread(image)
    gray_image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    # Show Ảnh
    cv2.imshow("Anh goc", source_image)
    cv2.imshow("Anh gray", gray_image)

    # Dừng màn hình
    cv2.waitKey()

    # Đóng các cửa sổ
    cv2.destroyAllWindows()

# Đọc camera
def read_camera(camera_id):
    capture = cv2.VideoCapture(camera_id)
    # Đọc ảnh từ camera
    while True:
        # Đọc ảnh
        ret, frame = capture.read()
        # Hiện ảnh
        cv2.imshow('Cam', frame)
        # Kiểm tra nếu bấm Q thì thoát
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    # Giải phóng camera
    capture.release()
    cv2.destroyAllWindows()

# Đọc video
def read_video(video):
    capture = cv2.VideoCapture(video)
    # Đọc ảnh từ video
    while True:
        # Đọc ảnh
        ret, frame = capture.read()
        # Hiện ảnh
        cv2.imshow('Cam', frame)
        # Kiểm tra nếu bấm Q thì thoát
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    # Giải phóng camera
    capture.release()
    cv2.destroyAllWindows()

# Chuyển sang ảnh xám và ghi ảnh
def convert_to_gray_and_write_image(image):
    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('src/opencv/assets/sample_gray.png', image)

# Chuyển sang ảnh gray và hsv
def convert_to_gray_and_hsv(image):
    image = cv2.imread(image)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("Anh mau", image)
    cv2.imshow("Anh xam", image_gray)
    cv2.imshow("Anh hsv", image_hsv)
    cv2.waitKey()
    cv2.destroyAllWindows()

# Resize ảnh
def resize_image(image):
    image = cv2.imread(image)
    image_resize1 = cv2.resize(image, dsize=(200,200))
    image_resize2 = cv2.resize(image, dsize=None, fx=0.5, fy=0.5)
    cv2.imshow("Anh mau", image)
    cv2.imshow("Anh resize 1", image_resize1)
    cv2.imshow("Anh resize 2", image_resize2)
    cv2.waitKey()
    cv2.destroyAllWindows()

# Xoay ảnh
def rotate_image(image):
    image = cv2.imread(image)
    image_rotate = imutils.rotate(image, 90)
    cv2.imshow("Anh mau", image)
    cv2.imshow("Anh rotate", image_rotate)
    cv2.waitKey()
    cv2.destroyAllWindows()

# Xử lý ảnh (binary-threshold)
def threshold_image(image):
    image = cv2.imread(image)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("Anh mau", image)
    cv2.imshow("Anh threshold", thresh_binary)
    cv2.waitKey()
    cv2.destroyAllWindows()

# Xử lý ảnh (canny)
def canny_image(image):
    image = cv2.imread(image)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(image_gray, threshold1=100, threshold2=200)
    cv2.imshow("Anh mau", image)
    cv2.imshow("Anh gray", image_gray)
    cv2.imshow("Anh edges", edges)
    cv2.waitKey()
    cv2.destroyAllWindows()

# GaussianBlur ảnh
def blur_image(image):
    image = cv2.imread(image)
    blur = cv2.GaussianBlur(image, ksize=(31,31), sigmaX=0)
    cv2.imshow("Anh mau", image)
    cv2.imshow("Anh blur", blur)
    cv2.waitKey()
    cv2.destroyAllWindows()

# gray camera
def gray_camera(camera_id):
    video = cv2.VideoCapture(camera_id)
    while True:
        ret, frame = video.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Anh tu webcam", frame)
        if cv2.waitKey(1) == ord ('q'):
            break
    video.release()
    cv2.destroyAllWindows()

# rotate with key
def rotate_with_key(camera_id):
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

if __name__ == "__main__":
    pass
