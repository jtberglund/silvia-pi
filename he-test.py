#!/usr/bin/python3

def start_test():
    import config as conf
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(conf.he_pin, GPIO.OUT)
    GPIO.output(conf.he_pin,0)

    while True:
        try:
            userInput = input("Enter HE state (1 or 0)")
            if userInput != "0" and userInput != "1":
                print("Invalid input, exiting...")
                break
            on = int(userInput)
            if on == 1:
                print("Turning on")
            else:
                print("Turning off")
            GPIO.output(conf.he_pin, on)
        except Exception as ex:
            print('GPIO error')
            print(type(ex))
            print(ex.args)
            print(ex)
            break

if __name__ == '__main__':
    start_test()
