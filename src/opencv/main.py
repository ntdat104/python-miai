import utils
import constants

def main():
    utils.read_image(constants.SAMPLE_IMG)
    utils.read_camera(constants.CAMERA_ID_WEBCAM)
    utils.read_video(constants.CAMERA_ID_VIDEO)
    utils.convert_to_gray_and_write_image(constants.SAMPLE_IMG)
    utils.convert_to_gray_and_hsv(constants.SAMPLE_IMG)
    utils.resize_image(constants.SAMPLE_IMG)
    utils.rotate_image(constants.SAMPLE_IMG)
    utils.threshold_image(constants.SAMPLE_IMG)
    utils.canny_image(constants.SAMPLE_IMG)
    utils.blur_image(constants.SAMPLE_IMG)
    utils.gray_camera(constants.CAMERA_ID_WEBCAM)
    utils.rotate_with_key(constants.CAMERA_ID_WEBCAM)

if __name__ == "__main__":
    main()