import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
class servo():
    def __init__(self,S):
        self.S = S
        GPIO.setup(self.S,GPIO.OUT)
        self.pwm = GPIO.PWM(self.S, 50)
        GPIO.output(self.S, True)
        self.pwm.start(0)
    def SetAngle(self,angle):
        duty = angle / 18 + 2
        self.pwm.ChangeDutyCycle(duty)
        sleep(0.25)
        GPIO.output(self.S, False)
        self.pwm.ChangeDutyCycle(0)

# servoH= servo(18)
# servoV= servo(16)
# ah=0
# av=0
# while True:
#     servoH.SetAngle(70)
#     sleep(0.5)
#     servoV.SetAngle(70)
#     sleep(0.5)
#      servoH.SetAngle(90)
#      sleep(0.5)
#      servoV.SetAngle(90)
#      sleep(0.5)
#     



# motor1 = motor(2,3,4)
# motor2 = motor(17,22,27)
#  
# while True:
#     
#     motor1.moveF(x=100)
#     motor2.moveF(x=100)
#     sleep (2)
#     motor1.stop()
#     motor2.stop()
#     sleep (2)
#     motor1.moveB(x=100)
#     motor2.moveB(x=100)
#     sleep (2)
#     motor1.stop()
#     motor2.stop()
#     sleep (2)
# 
#     for x in range(20,100):
#         motor1.moveF(x,0.05)
#         print(x)
#     for x in range(100,20,-1):
#         motor1.moveF(x,0.05)
#         print(x)
#     motor1.stop(5)
