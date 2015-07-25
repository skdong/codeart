#!/usr/bin/env python

class CodeSentenceArt:

	def __init__( self, sentence):
		self.sentence = ''
		self.depth = 0
		self.SetDepthOfSentence( sentence )
		self.SetSentence( sentence )

	def SetDepthOfSentence( self, sentence ):
		blankNum = 0
		tabNum = 0
		
		for character in sentence:
			if character != ' ' and character != '\t':
				break
			if character == ' ':
				blankNum += 1
			if character == '\t':
				if blankNum % 4 != 0 :
					return -1
				tabNum += 1

		if( blankNum % 4 != 0 ):
			return -1

		self.depth = tabNum + blankNum / 4

	def SetSentence( self, sentence ):
		self.sentence = sentence.strip()

	def IsEmptySentence( self ):
		if( len(self.sentence) == 0 ):
			return True
		else:
			return False

	def IsNoteSentence( self ):
		if( self.sentence.startswith('#') ):
			return True
		else:
			return False


