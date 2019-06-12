import smtplib
import poplib
import email
from email.header import decode_header,Header
from email.mime.text import MIMEText
import datetime
import os
import time

# pw1='xm111737' # 授权码
pw2='Xm111737'

# # set sender mailbox
# sender_domain='smtp.sina.cn'
# sender=smtplib.SMTP_SSL(sender_domain)
# sender.login(user='13959253604',password=pw1)

# # write texts

# acceptor_domain='13959253604<13959253604@163.com>'
# to=[sender_domain,acceptor_domain]

# halt_text=MIMEText('报表1')
# halt_text['Subject']=Header('报表1','utf-8')
# halt_text['From']='13959253604<13959253604@sina.cn>'
# halt_text['To']=','.join(to)
# # halt_text['Date']=Header(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'utf-8') # 坑? not?

# sender.sendmail(halt_text['From'],to,halt_text.as_string())
# sender.close()



def getMsgSubject():
    mail_reader=poplib.POP3('pop.163.com')
    mail_reader.user('13959253604@163.com')
    mail_reader.pass_(pw2)

    file_parse=mail_reader.stat()
    firstline=mail_reader.top(file_parse[0],0) #服务器将返回由参数标识的邮件前0行内容，最后firstline为一个列表，有三个元素
    secondline=[]
    for x in firstline[1]: #其中firstline[1],也就是firstline中的第二个参数为第一封邮件的各种信息，在这里要给其进行编码
        try:
            secondline.append(s.decode())
        except:
            try:
                secondline.append(x.decode('gbk'))
            except:
                secondline.append(x.decode('big5'))
    msg=email.message_from_string('\n'.join(secondline)) # #这个方法能把string的邮件转换成email.message实例
    # email.message实例是把经过编码的str2转化为可识别的邮件信息，并且每行信息.join()来连接字符串

    msg_subject=decode_header(msg['Subject'])
    if msg_subject[0][1]: #如果有第二个元素，就说明有编码信息
        print('a')
        msg_info= msg_subject[0][0].decode(msg_subject[0][1])
        mail_reader.dele(mail_reader.stat()[0]) # 注意, 发过的马上删除, 避免下次再出事
        mail_reader.quit() # 关机前关闭邮箱
    else:
        print('b')
        msg_info=msg_subject[0][0]
        mail_reader.dele(mail_reader.stat()[0])
        mail_reader.quit()
    return msg_info


while True:
    msg_subject=getMsgSubject()
    if msg_subject=='果决' or msg_subject=='GoodJob': # 果决=gj=关机, 避开filters

        os.system('shutdown -s -t 1')
        break
    elif msg_subject=='彩旗' or msg_subject=='Reload': # 陈齐=cq=重启
        os.system('shutdown -r -t 1')
        break
    time.sleep(60*15)



