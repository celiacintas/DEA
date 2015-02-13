#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import pygame

def blink(num_times,speed, output_pin):
	"""
	blink #num_times times at a #speed in the pin #output_pin
	"""
	for i in range(0,numTimes):
		GPIO.output(output_pin, True)
		time.sleep(speed)
		GPIO.output(output_pin, False)
		time.sleep(speed)
	GPIO.cleanup()

def led_on(output_pin):
	"""
	set on 1 the led at the #output_pin
	"""
	GPIO.output(output_pin, True)

def play_audio(audio_file):
	"""
	play #audio_file
	"""
	pygame.init()
	song = pygame.mixer.Sound(audio_file)
	clock = pygame.time.Clock()
	song.play()
	while True:
	    clock.tick(60)
	pygame.quit()

def plot_ritmo(ritmo=2):
	"""
	Dummy fuction, this should plot the cardio data of certain
	ritmo
	"""
	x = np.linspace(0.0, 5.0, 100)
	y = np.cos(ritmo * np.pi * x) * np.exp(-x)
	plt.plot(x, y)
	plt.show()