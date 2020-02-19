import smtplib
import time


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login("dimsum1246@gmail.com", "dugganschool4321")
        message = 'Subject:{}\n\n{}'.format(subject, msg)
        server.sendmail("dimsum1246@gmail.com", "dimsum1246@gmail.com", message)
        server.quit()
        print("Success")
    except:
        print("Email failed to send.")


def timer(t):
    try:
        when_to_stop = abs(int(t))

    except KeyboardInterrupt:
        return
    except:
        print("Not a number!")

    while when_to_stop > 0:
        m, s = divmod(when_to_stop, 60)
        h, m = divmod(m, 60)
        time_left = (str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2))
        print(time_left + "\r", end="")
        time.sleep(1)
        when_to_stop -= 1


subject = input("Enter Subject Line: ")
msg = input("Enter message: ")
t = input(">> ")
timer(t)
print("Sending Email")
send_email(subject, msg)
