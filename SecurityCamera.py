from twilio.rest import Client
from gpiozero import MotionSensor
import picamera
from time import sleep

#Import smtplib for the sending function 
import smtplib
 
# Here are the email package modules we'll need
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# put your own credentials here

account_sid = "AC906bcccd0b5b545210b7260719a04884"
auth_token = "39e44534a38eae8efa388eaee1ca5a8c"

pir = MotionSensor(4)
client = Client(account_sid, auth_token)
camera = picamera.PiCamera()
camera.vflip = True
sleep(2)
while True:
    pir.wait_for_motion()
    print("Camera motion and message all are working togather:)")
    camera.capture('image.jpg')    
    client.messages.create(to="+15305917112",
  		           from_="+15309240922",
 			   body="You Moved!")


    # Create the container (outer) email message.
    msg = MIMEMultipart()
    msg['Subject'] = 'For the Project'
    msg['From'] = 'deepansh.agr@gmail.com'
    msg['To'] = 'dagrawal1@mail.csuchico.edu'
    msg.preamble = 'Project almost done'
 
    # Open the files in binary mode.  Let the MIMEImage class automatically
    # guess the specific image type.
    fp = open('/home/pi/Documents/FinalProject/image.jpg','rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    # Send the email via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.sendmail('deepansh.agr@gmail.com', 'dagrawal1@mail.csuchico.edu', msg.as_string())
    s.quit()
    pir.wait_for_no_motion()



