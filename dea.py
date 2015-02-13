#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
import RPi.GPIO as GPIO
import numpy as np
import scipy
import matplotlib.pyplot as plt
from multiprocessing import Process
from tools import blink, led_on

ritmos1 = {'r3':4, 'r4':5 }
ritmos2 = {'r1':2, 'r2':3 }
palanca = True

def play_audio(audio_file):
	pygame.init()
	song = pygame.mixer.Sound(audio_file)
	clock = pygame.time.Clock()
	song.play()
	while True:
	    clock.tick(60)
	pygame.quit()

def plot_ritmo(ritmo=2):
	x = np.linspace(0.0, 5.0, 100)
	y = np.cos(ritmo * np.pi * x) * np.exp(-x)
	plt.plot(x, y)

def buttonOn(audioBienvenida='audio/1.ogg'):
	play_audio(audioBienvenida)

def plugedIn(audioAnalisis='audio/2.ogg'):
	play_audio(audioAnalisis)
	led_on(19)
	if palanca == True:
		#shuffle of ritmos1
		#lanzar hilo
		audio_file = 'audio/3.ogg'
		ritmo = ritmos1['r3']
		p_blink = Process(target=blink, args=(10, 10, 19,))
		p_audio.start()

	else:
		#shuffle of ritmos2
		audio_file = 'audio/4.ogg'
		ritmo = ritmos2['r2']

	p_audio = Process(target=play_audio, args=(audio_file,))
	p_audio.start()
	p_plot = Process(target=plot_ritmo, args=(ritmo,))
	p_plot.start()
	    	
def electro_button():
	time.sleep(120)
	print 'Pasaron 2 minutos!!!!'

def gpio_setup():
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




