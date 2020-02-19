import smtplib


def send_email(subject, msg):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login("dimsum1246@gmail.com", "dugganschool4321")
		message = 'Subject:{}\n\n{}'.format(subject,msg)
		server.sendmail( "dimsum1246@gmail.com","williamhholee@gmail.com", message)
		server.quit()
		print("Success")
	except:
		print("Email failed to send.")

subject = "Test"
msg = "renrekgod"

send_email(subject, msg)
