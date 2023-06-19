import RPi.GPIO as GPIO
import smbus
import time


GPIO.setmode(GPIO.BOARD)
bus = smbus.SMBus(1)

DEVICE_IC_1 = 0x21  # Device address (A0-A2)
DEVICE_IC_2 = 0x22
	
drv_on = 18
# pcf_on = 16
#power = 12

GPIO.setup(drv_on, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(pcf_on, GPIO.OUT)
# GPIO.output(pcf_on, 1)
GPIO.setup(power, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(power, 0)
time.sleep(0.1)

bus.write_byte_data(DEVICE_IC_1, 0x06, 0x00)
bus.write_byte_data(DEVICE_IC_2, 0x06, 0x00)
bus.write_byte_data(DEVICE_IC_1, 0x07, 0x00)
bus.write_byte_data(DEVICE_IC_2, 0x07, 0x00)


time.sleep(0.001)

bus.write_byte_data(DEVICE, 0x02, 0x00) # setting it for write operation
bus.write_byte_data(DEVICE, 0x03, 0x00) # same as above

time.sleep(0.001)


a_up = [0b0100000000000000, 0b0001000000000000, 0b0000010000000000, 0b0000000100000000, 0b0000000010000000, 0b0000000000100000]
a_down = [0b1000000000000000, 0b0010000000000000, 0b0000100000000000, 0b0000001000000000, 0b0000000001000000, 0b0000000000010000]


relay_switch = 13
drv_on = 18


def up(cell, up_val):
	if cell == bc1:
		bus.write_byte_data(IC_1, 0x02, up_val)
	else:
		bus.write_byte(IC_2, 0x02, up_val)
    		    	    
def down(cell, down_val):
	if cell == bc1:
		bus.write_byte_data(IC_1, 0x02, down_va)
	else:
		bus.write_byte(IC_2, 0x02, up_val)

def relay_up(relay_switch):
    GPIO.output(relay_switch, 0)
    time.sleep(relay_delay)

def relay_down(relay_down):
    GPIO.output(relay_switch, 1)
    time.sleep(relay_delay)

def pulse_off(DEVICE):
        bus.write_word_data(DEVICE, 0x02, 0b0)

def drv_on_off(on_off, DEVICE):
    GPIO.output(drv_on, on_off)

def pulse_off(DEVICE):
    bus.write_word_data(DEVICE, 0x02, 0b0)



bc1_list = [0x00]*6
bc2_list = [0x00]*6
bc1_up_list = [0x00]*6
bc2_up_list = [0x00]*6
bc1_down_list = [0x00]*6
bc2_down_list = [0x00]*6

for dot in binary_list2[0]:
    bc2_list[dot-1] = a_up[dot-1]
    bc2_up_list[dot-1] = a_up[dot-1]

for dot in binary_list1[0]:
    bc1_list[dot-1] = a_up[dot-1]
    bc1_up_list[dot - 1] = a_up[dot - 1]

for dot in binary_list2[1]:
    bc2_list[dot-1] = a_down[dot-1]
    bc2_down_list[dot - 1] = a_down[dot - 1]

for dot in binary_list1[1]:
    bc1_list[dot-1] = a_down[dot-1]
    bc1_down_list[dot - 1] = a_down[dot - 1]

if bc1_down_list != [0x00] * 6 or bc2_down_list != [0x00] * 6:
        relay_down(IC_1)
        relay_down(IC_2)
        for i in range(6):
            if bc1_down_list[i] != 0x00:
                down(bc1_down_list[i])
                time.sleep(pulse_width)
                pulse_off(IC_1)
                time.sleep(0.0001)
            if bc2_down_list[i] != 0x00:
                down(bc2_down_list)
                time.sleep(pulse_width)
                pulse_off(IC_2)
                time.sleep(0.001)
        relay_up(IC_1)
        relay_up(IC_2)

if bc1_up_list != [0x00]*6 or bc2_up_list != [0x00]*6:
    relay_up(IC_1)
    relay_up(IC_2)
    for i in range(6):
        if bc1_up_list[i] != 0x00:
            up(bc1_up_list[i])
            time.sleep(pulse_width)
            pulse_off()
            time.sleep(0.001)
        if bc2_up_list[i] != 0x00:
            up(bc2_up_list[i])
            time.sleep(pulse_width)
            pulse_off()
            time.sleep(0.001)
        relay_down(IC_1)
        relay_down(IC_2)
