#-*- coding:utf-8 -*-

"""This is an abstract model"""

class AbstractModel(object):
	def __init__(self):
		self.listeners = []

	def addListener(self, callFunc):
		self.listeners.append(callFunc)

	def removeListener(self, callFunc):
		self.listeners.remove(callFunc)

	def update(self):
		for listenerFunc in self.listeners:
			listenerFunc(self)