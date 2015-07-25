#!/usr/bin/env python

import CodeSentenceArt

class CodeFileArt:

	def __init__(self, fileName):
		self.fileName = fileName
		self.importModule = []
		self.classes = []
		self.functions = []


	def TraveFile(self):
		try:
			codeFile = file(self.fileName,'U',0)
		except:
			print "open file err %s"%(self.fileName)
			return False

		for fileLine in codeFile:
			sentence = CodeSentenceArt.CodeSentenceArt( fileLine )
			if( sentence.IsEmptySentence() or sentence.IsNoteSentence() ):
				continue
			print "%d %s"%(sentence.depth,sentence.sentence)

	def PrintInfo(self):
		print self.fileName
		print self.importmodule
		print self.classes
		print self.functions

if __name__ == "__main__":
	codeFile = CodeFileArt('/home/dong/project/ulteo4Kode4kids/OvdServer/ulteo-ovd-slaveserver')
	#sigm.PrintInfo()
	codeFile.TraveFile()
	

