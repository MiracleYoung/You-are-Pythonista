from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib

account = '<发件人的QQ>@qq.com'
auth_code = 'istvzeerhoyefehc'

msg_to = '<收件人的QQ>@qq.com'

def simple_email():
    msg = MIMEText('hello, send by python...', 'plain', 'utf-8')

    server = smtplib.SMTP('smtp.qq.com', 25)
    server.login(account,auth_code)
    server.sendmail(account,[msg_to],msg.as_string())
    server.quit()

def has_subject_email():
    msg = MIMEText('hello, send by python...', 'plain', 'utf-8')
    # 主题
    msg['Subject'] = 'python 发送邮件'
    # 发件人
    msg['From'] = account
    # 收件人
    msg['To'] = msg_to

    server = smtplib.SMTP('smtp.qq.com', 25)
    server.login(account, auth_code)
    server.sendmail(account, [msg_to], msg.as_string())
    server.quit()

def has_html_email():
    text = '''
    <html>
        <body>
            <h1>
                <a href="http://ww.baidu.com">hello world</a>
            </h1>
        </body>
    </html>
    '''
    msg = MIMEText(text, 'html', 'utf-8')
    # 主题
    msg['Subject'] = 'python 发送html邮件'
    # 发件人
    msg['From'] = account
    # 收件人
    msg['To'] = msg_to

    server = smtplib.SMTP('smtp.qq.com', 25)
    server.login(account, auth_code)
    server.sendmail(account, [msg_to], msg.as_string())
    server.quit()

def has_attachment_email():
    # 构造邮件对象
    msg = MIMEMultipart()

    msg['From'] = account
    msg['To'] = msg_to
    msg['Subject'] = 'python 发送带附件的邮件'

    # 构造邮件正文
    text = MIMEText('请查看附件！！！', 'plain', 'utf-8')

    # 构造附件
    with open('attachments/test.txt', 'rb') as fp:
        file = MIMEText(fp.read(), 'base64', 'utf-8')

        # 将附件重命名
        file.add_header('Content-Disposition','attachment',filename='test.txt')

    # 添加附件到邮件中
    msg.attach(file)

    # 添加邮件正文到邮件中
    msg.attach(text)

    server = smtplib.SMTP('smtp.qq.com', 25)
    server.login(account, auth_code)
    server.sendmail(account, [msg_to], msg.as_string())
    server.quit()

def show_image_in_text():
    msg = MIMEMultipart()

    msg['From'] = account
    msg['To'] = msg_to
    msg['Subject'] = 'python 显示图片在邮件正文中'

    # 构造邮件正文
    html_text = '''
    <html>
        <body>
            <h1>
                下面是我发给你的图片
            </h1>
            <p><img src="cid:0"></p>
        </body>
    </html>
    '''
    text = MIMEText(html_text, 'html', 'utf-8')

    # 构造附件
    with open('attachments/image.jpg', 'rb') as fp:
        file = MIMEText(fp.read(), 'base64', 'utf-8')

        # 将附件重命名
        file.add_header('Content-Disposition', 'attachment', filename='image.jpg')
        # 设置附件id
        file.add_header('Content-ID','<0>')

    # 添加附件到邮件中
    msg.attach(file)

    # 添加邮件正文到邮件中
    msg.attach(text)

    server = smtplib.SMTP('smtp.qq.com', 25)
    server.login(account, auth_code)
    server.sendmail(account, [msg_to], msg.as_string())
    server.quit()

def use_MIMEImage_send_image():
    msg = MIMEMultipart()

    msg['From'] = account
    msg['To'] = msg_to
    msg['Subject'] = 'python 使用MIMEImage发送图片附件'

    # 构造邮件正文
    html_text = '''
        <html>
            <body>
                <h1>
                    下面是我发给你的图片
                </h1>
                <p><img src="cid:image1"></p>
            </body>
        </html>
        '''
    text = MIMEText(html_text, 'html', 'utf-8')

    # 构造附件
    with open('attachments/image.jpg', 'rb') as fp:
        image = MIMEImage(fp.read())

        image['Content-Type'] = 'application/octet-stream'

        # 将附件重命名
        image.add_header('Content-Disposition', 'attachment', filename='image.jpg')
        # 设置附件id
        image.add_header('Content-ID', '<image1>')

    # 添加附件到邮件中
    msg.attach(image)

    # 添加邮件正文到邮件中
    msg.attach(text)

    server = smtplib.SMTP('smtp.qq.com', 25)
    server.login(account, auth_code)
    server.sendmail(account, [msg_to], msg.as_string())
    server.quit()

if __name__ == '__main__':
    use_MIMEImage_send_image()



