# 思路
# 1.借助opencv调用摄像头拍照保存到本地
# 2.用email库构造邮件内容,保存图像以附件形式插入到邮件当中
# 3.用smtplib库发送邮件到指定的邮箱

# 工具导入
import time
import cv2  # pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
from email.mime.image import MIMEImage  # 用来构造邮件内容的库
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib  # 发送邮件


# 授权码:WEXAWHJTLKTVKLLO
pwd = 'WEXAWHJTLKTVKLLO'

# 服务器接口
host = 'smtp.163.com'
port = 25

sender = 'qiujinghong2022@163.com'
receiver = '81207739@qq.com'



def GetPicture():
    """
    拍照保存图像
    :return:
    """
    # TODO 创建一个窗口
    cv2.namedWindow('camera',1)
    # TODO 调用摄像头
    cap = cv2.VideoCapture(0)
    while True:
        success,img = cap.read()
        cv2.imshow("camera",img)
        # TODO 按键处理
        key = cv2.waitKey(10)
        if key == 27:
            # esc
            break
        if key == 32:
            # 空格
            filename = 'photo.png'
            cv2.imwrite(filename,img)
    # TODO 释放摄像头
    cap.release()
    # TODO 关闭窗口
    cv2.destroyWindow("camera")




def SetMsg():
    """
    邮件格式设置
    :return:
    """
    msg = MIMEMultipart('mixed')
    # TODO 标题
    msg['Subject'] = '照片'
    msg['From'] = sender # 发送方邮箱
    msg['To'] = receiver  # 接收方邮箱

    # TODO 邮件正文
    text = 'python发给你的照片,请查收\n如果后缀名是.bin：那么把它下载下来的时候把后缀名改成.jpg就可以了。'
    text_plain = MIMEText(text,'plain','utf-8')  # 正文转码
    msg.attach(text_plain)

    # TODO 图片附件
    SendImageFile = open('photo.jpg', 'rb').read()
    image = MIMEImage(SendImageFile)

    # TODO 将收件人看见的附件照片名称改为people.png
    image['Content-Diposition'] = 'attachment; filename = "people.png"'
    msg.attach(image)
    return msg.as_string()


def SendEmail(msg):
    """
    发送邮件 msg:邮件内容
    :param msg:
    :return:
    """
    smtp = smtplib.SMTP()
    smtp.connect(host)
    smtp.login(sender,pwd)
    smtp.sendmail(sender,receiver,msg)
    time.sleep(2)
    smtp.quit()




if __name__ == '__main__':
    # 1.拍照保存
    GetPicture()
    # 2.设置邮件格式
    msg = SetMsg()
    # 3.发送邮件
    SendEmail(msg)









##################################################################################
# TODO Self Tests:

def GetPic(name):
    """
    拍照保存图像
    :return:
    """
    # 创建一个窗口
    cv2.namedWindow('camera',1)
    # 调用摄像头
    cap = cv2.VideoCapture(0)
    while True:
        success,img = cap.read()
        cv2.imshow("camera",img)
        # 按键处理
        key = cv2.waitKey(10)
        if key == 27:
            # esc
            break
        if key == 32:
            # 空格
            filename = f'{name}.jpg'
            cv2.imwrite(filename,img)
    # 释放摄像头
    cap.release()
    # 关闭窗口
    cv2.destroyWindow("camera")