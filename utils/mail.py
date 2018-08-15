# coding = utf-8
__author__ = 'hsl'

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from utils.config import Config
import time
from socket import gaierror, error
import re


class Mail:
    """
    发送邮件工具类
    """
    def __init__(self, attach=None):
        self.from_addr = Config().get('mail', 'from_addr')
        self.pwd = Config().get('mail', 'password')
        self.to_addr = Config().get('mail', 'to_addr')
        self.smtp_server = Config().get('mail', 'smtp_server')
        self.title = "测试报告"
        self.message = "测试报告如附件，测试执行时间：" + time.strftime("%Y-%m-%d %H:%M:%S")
        self.msg = MIMEMultipart('related')
        self.attach = attach

    def _attach_file(self, att_file):
        """
        添加附件
        :param att_file:str类型，文件名
        """
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.from_addr
        self.msg['To'] = self.to_addr
        self.msg.attach(MIMEText(self.message))

        # 添加附件，若附件有多个文件则传入list，若只有单个文件，传入str(文件名)
        if self.attach:
            if isinstance(self.attach, list):
                for a in self.attach:
                    self._attach_file(a)
            elif isinstance(self.attach, str):
                self._attach_file(self.attach)

        try:
            smtp_server = smtplib.SMTP(self.smtp_server)    # 连接服务器
        except (gaierror and error) as e:
            print("发送邮件失败，无法连接到SMTP服务器，请检查网络及SMTP服务器！", e)
        else:
            try:
                smtp_server.login(self.from_addr, self.pwd)     # 登录
            except smtplib.SMTPAuthenticationError as e:
                print("用户名密码验证失败！", e)
            else:
                smtp_server.sendmail(self.from_addr, self.to_addr.split(';'), self.msg.as_string())     # 发送邮件
                print("发送邮件【%s】成功，请检查%s收件箱！" % (self.title, self.to_addr))
            finally:
                smtp_server.quit()


if __name__ == "__main__":
    mail = Mail("D:\\Download\\export.html")
    mail.send()
