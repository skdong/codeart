#!/usr/bin/env python


class SingalModule:

	def __init__(self, moduleName):
		self.moduleName = moduleName
		self.importModule = []
		self.classes = []
		self.functions = []


	def TraveModule(self):
		try:
			modueFile = file(self.moduleName,'U',0)
		except:
			print "open file err %s"%(self.moduleName)
			return False

		for fileLine in modueFile:
			formatLine = fileLine.strip(' ').strip('\t')
			if formatLine[0:1] != '#' and len(formatLine) != 1:
				endIndex = fileLine.find('#')
				if( endIndex != -1 ):
					oneLine = fileLine[0:endIndex-1]
				else:
					oneLine = fileLine[0:len(fileLine)-1]
				self.BuildCodeArt( oneLine )
	
	def BuildCodeArt(self, oneLine ):
		depth = self.GetDepthOfLine(oneLine)
		print "%d %s"%(depth,oneLine)
	
	def GetDepthOfLine(self,oneLine ):
		depth = 0
		blankNum = 0
		tabNum = 0

		for character in oneLine:
			if character != ' ' and character != '\t':
				break

			if character == ' ':
				blankNum+=1

			if character == '\t':
				if blankNum%4 != 0:
					return -1
				tabNum+=1

		if( (blankNum != 0 and tabNum != 0) or blankNum%4 != 0 ):
			return -1

		return tabNum + blankNum/4


	
	def PrintInfo(self):
		print self.modulename
		print self.importmodule
		print self.classes
		print self.functions

if __name__ == "__main__":
	sigm = SingalModule('/home/dong/project/ulteo4Kode4kids/OvdServer/ulteo-ovd-slaveserver')
	#sigm.PrintInfo()
	sigm.TraveModule()
	

