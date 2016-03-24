# -*- coding:utf-8 -*-

import abstractmodel

class NameModel(abstractmodel.AbstractModel):
	def __init__(self, firstName, lastName):
		abstractmodel.AbstractModel.__init__(self)
		self.set(firstName, lastName)

	def set(self, first, last):
		self.firstName = first
		self.lastName = last
		self.update()