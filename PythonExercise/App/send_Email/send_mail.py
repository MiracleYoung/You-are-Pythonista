import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

def sendMail():
    # 邮件主题/标题
    mail_title = 'Email Reminder'
    # 邮件正文
    mail_content = 'This is an email reminder from Python.'
    # 发件人邮箱账号
    Sender = '*********@qq.com'
    # 收件人邮箱账号
    Receiver = '***********@126.com'
    # 发送邮件正文内容
    msg = MIMEText(mail_content, "plain", 'utf-8')
    # 发送邮件主题/标题
    msg["Subject"] = Header(mail_title, 'utf-8')
    # 发件人姓名  
    msg["From"] = formataddr(['＆娴敲棋子＆', Sender])
    # 收件人姓名  
    msg["To"] = formataddr(['＆娴敲棋子＆', Receiver]) 
    
    try:
        # 邮箱的传输协议，端口默认25
        e = smtplib.SMTP("smtp.qq.com", 25)   
        # 登录邮箱，第二个参数为发件人的邮箱授权码
        e.login(Sender, 'xxxxxxxxx')
        # 发送邮件，参数依次：发件人、收件人、发送消息
        e.sendmail(Sender, [Receiver, ], msg.as_string())
        # 退出邮箱
        e.quit()
        print('Email Send Successful!')
    except Exception:
        print('Email Send Failed!')


if __name__ == '__main__':
    sendMail()