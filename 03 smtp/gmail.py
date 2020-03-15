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

s = smtplib.SMTP(smtpName, smtPort) # 메일 서버 연결(s가 구글서버와 통신하는 하는 통로)
s.starttls() # TLS 보안처리
s.login(sendEmail,password) # 계정 로그인
s.sendmail(sendEmail, recvEmail, msg.as_string()) # 메일 전송, 문자열 반환
s.close()

