#make the google loggin for less secure connection
#https://myaccount.google.com/lesssecureapps

import smtplib

#smtpobj = smtplib.SMTP('smtp.gmail.com',587)
smtpobj = smtplib.SMTP('smtp.gmail.com',587)
smtpobj.ehlo()

smtpobj.starttls()
my_password = raw_input("password:")
smtpobj.login('chi@gmail.com',my_password)

smtpobj.sendmail('chi@gmail.com','chir6@gmail.com','Subject: automated mail\n\nThis is just a automated mail\n\nRegards,\nChiranjib Goswami')
{}
smtpobj.quit()
