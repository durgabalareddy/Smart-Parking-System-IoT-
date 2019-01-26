from ubidots import ApiClient
import RPi.GPIO as GPIO
import time

api = ApiClient('A1E-6784a6c3b518b1fe33d4d51f2dd4fed1574e')#API_Key

#Variable IDs
variable1 = api.get_variable('5b2603bec03f970e9613cf48')
variable2 = api.get_variable('5b2603cbc03f970db08d6423')
variable3 = api.get_variable('5b27e3c1c03f975b9ce4c66d')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

a1=GPIO.input(3)
b1=GPIO.input(5)
c1=GPIO.input(7)

status1 = int (a1)
status2 =int(b1)
status3 =int(c1)
IO.output(19,status1) 
IO.output(21,status2) 
IO.output(23,status3) 
variable1.save_value({'value':status1})
variable2.save_value({'value':status2}})
variable3.save_value({'value':status3}})

while 1:
    a2=GPIO.input(3)
	IO.output(19,int(a2))
    b2=GPIO.input(5)
	IO.output(21,int(b2))
    c2=GPIO.input(7)
	IO.output(23,int(c2))
	if(a1!=a2):
	    status1= int(not status1)
        variable1.save_value({'value':status1})
	a1=a2
    if(b1!=b2):
	    status2= int(not status2)
        variable2.save_value({'value':status2})
    b1=b2
	if(c1!=c2):
	    status3= int(not status3)
        variable3.save_value({'value':status3})
    c1=c2
