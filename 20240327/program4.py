import cv2
def image_process (src) :
    dstx = cv2.Sobel(src,cv2.CV_32F, 1, 0)
#計算x軸影像梯度
    dsty = cv2.Sobel(src,cv2.CV_32F, 0, 1)
# 計算y 軸影像梯度
    dstx = cv2.convertScaleAbs(dstx)
# 將負值轉正值
    dsty = cv2.convertScaleAbs(dsty)
#將負值轉正值
    dst = cv2.addNeighted （dstx, 0.5,dsty,0.5,0） #影像融合
    cv2.imwrite('sobel_processsing.jpg', dst)
#source = cv2. imread ("photo.jpg")
#image_process (source)