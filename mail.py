# coding=utf-8
import smtplib
from email.mime.text import MIMEText
def send_mail(msg_to = '352326430@qq.com',subject = "python邮件测试",content = "这是我使用python smtplib及email模块发送的邮件"):
    msg_from = '352326430@qq.com'  # 发送方邮箱
    passwd = 'jblyokdxpwxtbgbh'  # 填入发送方邮箱的授权码
    # msg_to = '352326430@qq.com'  # 收件人邮箱

    # subject = "python邮件测试"  # 主题
    # content = "这是我使用python smtplib及email模块发送的邮件"  # 正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465) # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")

    except s.SMTPException as e:
        print("发送失败")

    finally:
        s.quit()