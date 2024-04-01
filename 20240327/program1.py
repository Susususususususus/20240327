import cv2
import program3 as t3
def main():
    # 打开摄像头，参数 0 表示第一个摄像头，如果有多个摄像头，可以尝试不同的编号
    cap = cv2.VideoCapture(0)

    # 检查摄像头是否成功打开
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    # 循环读取视频帧
    while True:
        # 读取一帧
        ret, frame = cap.read()

        # 检查是否成功读取帧
        if not ret:
            print("无法读取视频帧")
            break

        # 显示帧
        cv2.imshow('Camera', frame)
        cv2.imwrite('test.jpg', frame)
        t3.image_process(frame)
        # 检测按键，如果按下 q 键则退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放摄像头资源
    cap.release()
    # 关闭所有 OpenCV 窗口
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
