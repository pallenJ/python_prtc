import smtplib
from email.mime.text import MIMEText

sendEmail = 'pallenstudy@gmail.com'
recvEmail = 'pallennellap17@gmail.com'
password  = ''

smtpName = 'smtp.gmail.com' #smtp 서버주소
smtPort  = 587              #smtp 포트번호

text = "python Email Test"
msg  = MIMEText(text)

msg['Subject'] = sendEmail
msg['from'] = recvEmail
print(msg.as_string())

