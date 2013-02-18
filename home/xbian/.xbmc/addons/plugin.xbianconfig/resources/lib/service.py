import xbmc

class service(xbmc.Monitor) :
	def __init__(self):
		xbmc.Monitor.__init__(self)
		self.onInit()
	
	def onInit(self):
		pass
			
	def onStart(self):
		pass
	
	def onAbortRequested(self):
		pass
	
	def onDatabaseUpdated(self,database):
		#database - video/music as string
		pass
	
	def onScreensaverActivated(self):
		pass
	
	def onScreensaverDeactivated(self):
		pass

	def isPlaying(self):
		pass
