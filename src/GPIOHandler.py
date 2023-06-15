import RPi.GPIO as GPIO
import time

#---Input GPIO Pin Numbers arranged by wire color---#
I_Black = 14  # 1 - 9, 14, 22
I_White = 15  # 2 - 12, 11, 21
I_Purple = 17 # 3 - 5, 8
I_Gray = 27   # 4 - 20, 16
I_Orange = 22 # 5 - 15, 10
#---#
I_Green = 10  # 6 - 2, 6
I_Yellow = 9  # 7 - 17, 13
I_Blue = 11   # 8 - 3, 4
I_Red = 13    # 9 - 19, 18
I_Brown = 19  # 10 - 7, 1
num_input_pins = 10
input_pins = [I_Black, I_White, I_Purple, I_Gray, I_Orange, I_Green, I_Yellow, I_Blue, I_Red, I_Brown]

#---Output GPIO Pin Numbers arranged by wire color---#
O_Orange = 20 # 1 - Triple 9 - 10 on the board
O_Green = 26  # 2 - Double "" 
O_Blue = 16   # 3 - Single ""
O_Purple = 12 # 4 - Bullseye 14 and 15
O_Red = 8     # 5 - Single 14 - 15 on the board
O_Yellow = 25 # 6 - Double ""
O_Brown = 24  # 7 - Triple ""
num_output_pins = 7
output_pins = [O_Orange, O_Green, O_Blue, O_Purple, O_Red, O_Yellow, O_Brown]

#---Associating values with proper outputs---#
first_half_dic = {I_Black: 14, I_White: 11, I_Purple: 8, I_Gray: 16, I_Orange: 15, I_Green: 2, I_Yellow: 17, I_Blue: 3, I_Red: 19, I_Brown: 7}
second_half_dic = {I_Black: 9, I_White: 12, I_Purple: 5, I_Gray: 20, I_Orange: 10, I_Green: 6, I_Yellow: 13, I_Blue: 4, I_Red: 18, I_Brown: 1}
bullseye_dic = {I_Black: 22, I_White: 21}

#---Setup---#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(input_pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(output_pins, GPIO.OUT, initial = GPIO.HIGH)

#---Execution---#
def collect_scores ():
    score_and_multiplier = {}
    hits_read = 0
    while hits_read < 10:
        for o_pin in output_pins:
            #print(str(o_pin))
            GPIO.output(o_pin, GPIO.HIGH)
            #time.sleep(.001)
            for i_pin in input_pins:
                if GPIO.input(i_pin) == GPIO.HIGH:
                    print("Hit detected by pin " + str(i_pin) + " and sent by pin " + str(o_pin))
                    score = interpret_input(i_pin, o_pin)
                    multiplier = get_multiplier(score, o_pin, score_and_multiplier)
                    print("Score: " + str(score) + "\nMultiplier: " + str(multiplier))
                    score_and_multiplier[score] = multiplier
                    #score_and_multiplier[interpret_input(i_pin, o_pin)] = get_multiplier(i_pin, o_pin, score_and_multiplier)
                    hits_read += 1
                    time.sleep(0.5)
            GPIO.output(o_pin, False)
            #time.sleep(.001)
    print(str(score_and_multiplier))
    cleanup()
    return(score_and_multiplier)
    
def interpret_input (i_pin, o_pin):
    if o_pin == O_Orange or o_pin == O_Green or o_pin == O_Blue :
        return second_half_dic[i_pin]
    elif o_pin == O_Red or o_pin == O_Yellow or o_pin == O_Brown :
        return first_half_dic[i_pin]
    elif o_pin == O_Purple :
        return bullseye_dic[i_pin]

def get_multiplier (score, o_pin, score_and_multiplier):
    multiplier = 0
    
    if score in list(score_and_multiplier.keys()):
        multiplier = score_and_multiplier[score]
        
    if o_pin == O_Orange or o_pin == O_Brown or (score == 22 and o_pin == O_Purple):
        multiplier += 3
    elif o_pin == O_Green or o_pin == O_Yellow or (score == 21 and o_pin == O_Purple):
        multiplier += 2
    elif o_pin == O_Blue or o_pin == O_Red:
        multiplier += 1
    return multiplier
    
def cleanup ():
    GPIO.cleanup()
    
#collect_scores()