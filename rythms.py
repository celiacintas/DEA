#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import scipy
import scipy.signal as sig

# TODO in this module should have 2 rythms for shock and 11 for non shock

def rythms_test1():
	rr = [1.0, 1.0, 0.5, 1.5, 1.0, 1.0] # rr time in seconds
	fs = 8000.0 # sampling rate
	pqrst = sig.wavelets.daub(10) # just to simulate a signal, whatever
	ecg = scipy.concatenate([sig.resample(pqrst, int(r*fs)) for r in rr])
	t = scipy.arange(len(ecg))/fs

	return t, ecg