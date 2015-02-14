#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
import RPi.GPIO as GPIO
import numpy as np
import scipy
import matplotlib.pyplot as plt
from multiprocessing import Process
from tools import blink, led_on, play_audio


class GPIO_DEA(object):
	"""docstring for GPIO_DEA"""
	def __init__(self, pin_led, pin_onoff, pin_switch_shock, pin_cable):
		super(GPIO_DEA, self).__init__()
		self.pin_led = pin_led
		self.pin_onoff = pin_onoff
		self.pin_switch_shock = pin_switch_shock
		selg.pin_cable = pin_cable
		self.setup()

	def setup(self):
		"""
		This is the output/input and callbacks setup for buttons and leds.
		"""
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin_led, GPIO.OUT)
		GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # boton ON/ OFF
		GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP) # cable
		# agregar palanca
		# agregar boton de descarga
		GPIO.add_event_detect(, GPIO.RISING, callback=self.button_on, bouncetime=300)
		GPIO.add_event_detect(24, GPIO.RISING, callback=self.pluged_in, bouncetime=300)


	def get_switch_shock(self):
		"""
		Check if in this turn you should use shock or not
		"""
		return GPIO.input(self.pin_switch_shock)

	def button_on(self, audio_bienvenida='audio/1.ogg'):
		"""
		callback for on/off button
		"""
		play_audio(audio_bienvenida)

	def pluged_in(self, audio_analisis='audio/2.ogg'):
		"""
		When the cable is plugedin check if the shock button
		to look which set of rhythms we should use,
		and if we should turn on the leds
		"""
		play_audio(audio_analisis)
		self.led_on() # this should not be hardcoded
		if self.get_switch_shock():
			# TODO shuffle of ritmos1
			audio_file = 'audio/3.ogg'
			ritmo = ritmos1['r3']
			p_blink = Process(target=self.blink, args=(10, 10, 19,))
			p_audio.start()
		else:
			# TODO shuffle of ritmos2
			audio_file = 'audio/4.ogg'
			ritmo = ritmos2['r2']
		p_audio = Process(target=play_audio, args=(audio_file,))
		p_audio.start()
		p_plot = Process(target=plot_ritmo, args=(ritmo,))
		p_plot.start()
	
	def shock_button_pressed():
		"""
		after resolving the shock phase you should wait 2'
		and go back again to plugedIn fuction 
		"""
		time.sleep(120)
		# TODO make a 60' alarm
		print 'Pasaron 2 minutos!!!!'


	def blink(self, num_times, speed):
		"""
		blink #num_times times at a #speed in the pin #output_pin
		"""
		for i in range(num_times):
			GPIO.output(self.pin_led, True)
			time.sleep(speed)
			GPIO.output(self.pin_led, False)
			time.sleep(speed)
		GPIO.cleanup()

	def led_on(self):
		"""
		set on 1 the led at the #output_pin
		"""
		GPIO.output(self.pin_led, True)

# TODO this should have the heart fuctions
ritmos1 = {'r3':4, 'r4':5 } 
ritmos2 = {'r1':2, 'r2':3 }

def main():
	my_dea_gpio = GPIO_DEA()


if __name__ == '__main__':
	main()




