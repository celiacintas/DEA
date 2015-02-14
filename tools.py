#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import pygame
import matplotlib.pyplot as plt

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

def plot_ritmo(t, ecg):
	"""
	Dummy fuction, this should plot the cardio data of certain
	ritmo
	"""
	plt.plot(t, ecg)
	plt.show()
