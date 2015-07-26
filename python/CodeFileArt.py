#!/usr/bin/env python

import CodeSentenceArt
import ImportModuleArt

class CodeFileArt:

	def __init__(self, fileName):
		self.fileName = fileName
		self.importModule = {}
		self.classes = {}
		self.functions = {}
		self.attributes = {}
		self.structStack = []
		self.structStack.append(self)
		self.depth = -1


	def TraveFile(self):
		try:
			codeFile = file(self.fileName,'U',0)
		except:
			print "open file err %s"%(self.fileName)
			return False

		for fileLine in codeFile:
			sentence = CodeSentenceArt.CodeSentenceArt( fileLine )
			self.AnalyseSentence(sentence)

	def AnalyseSentence(self, sentence ):

		if( sentence.IsEmptySentence() or sentence.IsNoteSentence() ):
			return False
		
		if( sentence.sentence.startswith('import') ):
			#print "%d %s"%(sentence.depth,sentence.sentence)
			self.AddImportModule(sentence)
		elif( sentence.sentence.startswith('from') ):
			#print "%d %s"%(sentence.depth,sentence.sentence)
			self.AddImportModule(sentence)
		elif( sentence.sentence.startswith('class') ):
			self.CreateClassArt(sentence)
			print "%d %s"%(sentence.depth,sentence.sentence)
		elif( sentence.sentence.startswith('def') ):
			#self.CreateFunctionArt( sentence )
			print "%d %s"%(sentence.depth,sentence.sentence)

			#print "%d %s"%(sentence.depth,sentence.sentence)

	def AddImportModule( self, sentence ):
		moduleFrom = ''	
		if( sentence.sentence.startswith('from') ):
			moduleFrom = sentence.sentence[len('from')+1:sentence.sentence.index(' import ')+1]
			modules = sentence.sentence[sentence.sentence.index(' import ')+len(' import '):]
		else:
			modules = sentence.sentence[sentence.sentence.index('import ')+len('import '):]

		importModules = modules.split(',')
		for importModule in importModules:
			imModule = ImportModuleArt.ImportModuleArt(moduleFrom,importModule)	
			self.importModule[imModule.moduleAs] = imModule

	def CreateClassArt( self, sentence ):
		codeClass = CodeClassArt( sentence )
		while self.structStack[-1].depth > codeClass.depth:
			self.structStack.pop()
		self.structStack[-1].AddClassArt( codeClass )
		self.structStack.append( codeClass )

	def CreateFunctionArt( self. sentence ):
		codeFunction = CodeFunctionArt( sentence )
		while self.structStack[-1].depth > codeFunction.depth:
			self.structStack.pop()
		self.structStack[-1].AddFunctionArt( codeFunction )
		self.structStack[-1].append( codeClass )
	
	def AddClassArt( self. codeClass ):
		self.classes[codeClass.name] = codeClass

	def AddFunctionArt( self, codeFunction ):
		self.functions[codFunction.name] = codeFunction
	
	def AddFunctionn( self, function ):
		self.functions[function.name] = function
	
	def AddAttribute( self, attribute ):
		self.atrributes[attribute.name] = attribute

	def PrintInfo(self):
		print self.fileName
		for artmodule in self.importModule:
			print self.importModule[artmodule].tostring()
		print self.classes
		print self.functions

if __name__ == "__main__":
	codeFile = CodeFileArt('/home/dong/project/ulteo4Kode4kids/OvdServer/ulteo-ovd-slaveserver')
	#sigm.PrintInfo()
	codeFile.TraveFile()
	codeFile.PrintInfo()
	

