#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
import RPi.GPIO as GPIO
import numpy as np
import scipy
import matplotlib.pyplot as plt
from multiprocessing import Process
from tools import blink, led_on, play_audio

# TODO this should have the heart fuctions
ritmos1 = {'r3':4, 'r4':5 } 
ritmos2 = {'r1':2, 'r2':3 }

# This is a physical button
palanca = True


def buttonOn(audioBienvenida='audio/1.ogg'):
	"""
	callback for on/off button
	"""
	play_audio(audioBienvenida)

def plugedIn(audioAnalisis='audio/2.ogg'):
	"""
	When the cable is plugedin check if the shock button
	to look which set of rhythms we should use,
	and if we should turn on the leds
	"""
	play_audio(audioAnalisis)
	led_on(19) # this should not be hardcoded
	if palanca == True:
		# TODO shuffle of ritmos1
		audio_file = 'audio/3.ogg'
		ritmo = ritmos1['r3']
		p_blink = Process(target=blink, args=(10, 10, 19,))
		p_audio.start()

	else:
		# TODO shuffle of ritmos2
		audio_file = 'audio/4.ogg'
		ritmo = ritmos2['r2']

	p_audio = Process(target=play_audio, args=(audio_file,))
	p_audio.start()
	p_plot = Process(target=plot_ritmo, args=(ritmo,))
	p_plot.start()
	    	
def electro_button():
	"""
	after resolving the shock phase you should wait 2'
	and go back again to plugedIn fuction 
	"""
	time.sleep(120)
	# TODO make a 60' alarm
	print 'Pasaron 2 minutos!!!!'

def gpio_setup():
	"""
	This is the output/input and callbacks setup for buttons and leds.
	"""

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(19, GPIO.OUT)
	GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # boton ON/ OFF
	GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP) # cable
	# agregar palanca
	# agregar boton de descarga
	GPIO.add_event_detect(23, GPIO.RISING, callback=buttonOn, bouncetime=300)
	GPIO.add_event_detect(24, GPIO.RISING, callback=plugedIn, bouncetime=300)

def test():
	gpio_setup()
	buttonOn()
	plugedIn()
	electro_button()



if __name__ == '__main__':
	test()




