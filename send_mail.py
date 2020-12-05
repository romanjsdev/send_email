import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
post1 = 'youre email'
password = 'youre email password'
post2 = 'mail to send'
smtpObj.login(post1, password)
mail_to = [post2]
message = 'youre message'
message = message.encode('utf-8')
smtpObj.sendmail(post1, mail_to, message)
smtpObj.quit
print ('email delivery')