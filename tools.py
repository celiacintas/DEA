#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import pygame


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