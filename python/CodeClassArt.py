#!/usr/bin/env python

class CodeClassArt:
	def __init__(self, sentence ):
		self.name = ''
		self.fathers = []
		self.functions = {}
		self.classes = {}
		self.attributes = {}
		self.InitBySentence( sentence )

	def InitBySentence(self, sentence ):
		classSentence = sentence.sentence.lstrip('class').rstrip(':').strip()
		self.depth = sentence.depth
		if( classSentence.find('(') == -1 ):
			self.name = classSentence.
		else:
			self.name = classSentence[1:classSentence.find('(')].strip()
			fathersSentence = classSentence[classSentence.find('(')+1:].rstrip(')').strip()
			fathers = fathersSentence.split(',')
			for father in fathers:
				self.fathers.append( father.strip() )

	def AddClassArt(self,codeClass ):
		self.classes[codeClass.name] = codeClass

	def AddFunction(self,function ):
		self.functions[function.name] = function

	def AddAttribute(self, attribute ):
		self.attributes[attribute.name] = attribute

