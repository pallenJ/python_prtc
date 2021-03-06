import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sendEmail = 'pallenstudy@gmail.com'
recvEmail = 'pallennellap17@gmail.com'
password  = ''

smtpName = 'smtp.gmail.com' #smtp 서버주소
smtPort  = 587              #smtp 포트번호

#여러 MIME을 넣기위한 MIMEMultipart 객체 생성
msg  = MIMEMultipart()

# 본문추가
text = 'python Email Test2'
contentPart = MIMEText(text)
msg.attach(contentPart)

# 파일추가
etcFileName = 'smtpEmail.png'
with open(etcFileName, 'rb') as etcFD:
    etcPart = MIMEApplication(etcFD.read())
    # 첨부파일 정보를 헤더로 추가
    etcPart.add_header('Content-Disposition', 'attachment', filename = etcFileName)
    msg.attach(etcPart)

msg['Subject'] = 'test2'
msg['From'] = sendEmail
msg['To'] = recvEmail

print(msg.as_string())

s = smtplib.SMTP(smtpName, smtPort) # 메일 서버 연결(s가 구글서버와 통신하는 하는 통로)
s.starttls() # TLS 보안처리
s.login(sendEmail,password) # 계정 로그인
s.sendmail(sendEmail, recvEmail, msg.as_string()) # 메일 전송, 문자열 반환
s.close()

