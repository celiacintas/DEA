#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

def blink(num_times,speed, output_pin):
	for i in range(0,numTimes):## Run loop numTimes
		GPIO.output(output_pin,True)## Switch on pin 7
		time.sleep(speed)## Wait
		GPIO.output(output_pin,False)## Switch off pin 7
		time.sleep(speed)## Wait
	GPIO.cleanup()


def led_on(output_pin):
	GPIO.output(output_pin,True)
