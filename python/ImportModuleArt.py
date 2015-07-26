#!/usr/bin/env python

class ImportModuleArt:
	def __init__(self, moduleFrom, moduleLine ):
		self.moduleFrom = moduleFrom.strip()
		self.moduleName = ''
		self.moduleAs = ''
		self.AnalyesModuleLine(moduleLine)
	
	def AnalyesModuleLine(self, moduleLine ):
		moduleLine = self.FormatModuleLine(moduleLine)
		if( moduleLine.find(' as ') == -1 ):
			self.moduleAs = self.moduleName = moduleLine
		else:
			self.moduleName, self.moduleAs = moduleLine.split(' as ',1)
	
	def FormatModuleLine(self,moduleLine ):
		if( moduleLine.find('#') != -1 ):
			moduleLine = moduleLine[1:moduleLine.find('#')]
		return moduleLine

	def tostring(self):
		return "%s/%s as %s"%( self.moduleFrom, self.moduleName, self.moduleAs)
