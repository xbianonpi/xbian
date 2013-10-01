import os,sys
from xbmcguie.window import WindowSkinXml
import xbmcgui
import threading

class XbianWindow(WindowSkinXml):   
    def __init__(self,strXMLname, strFallbackPath, strDefaultName=False, forceFallback=False) :
        WindowSkinXml.__init__(self,strXMLname, strFallbackPath, strDefaultName=False, forceFallback=False)
        self.categories = []
        self.publicMethod = {}
        self.stopRequested = False
    
    def onInit(self):
        WindowSkinXml.onInit(self)
        #first, get all public method
        for category in self.categories :
            self.publicMethod[category.getTitle()] = {}
            for setting in category.getSettings():
                public = setting.getPublicMethod()
                for key in public :
                    self.publicMethod[category.getTitle()][key] = public[key]
        #set the windows instance in all xbmc control
        for category in self.categories :
			if self.stopRequested :
				break
			initthread  = threading.Thread(None,self.onInitThread, None, (category,))
			initthread.start()
        
    def onInitThread(self,category):                                
            #set default value to gui
            for setting in category.getSettings():                
                if self.stopRequested :
					break
                try :                                                   
                    setting.updateFromXbian()
                    setting.setPublicMethod(self.publicMethod)                                                               
                except :
                    #don't enable control if error
                    print 'Exception in updateFromXbian for setting'
                    print sys.exc_info()                      
                else :
                    setting.getControl().setEnabled(True)
    
    def addCategory(self,category):        
        self.categories.append(category)
        self.addControl(category.getCategory())
        
     
    def doXml(self,template) :       
        xmltemplate = open(template)
        xmlout = open(self.xmlfile,'w')
        for line in xmltemplate.readlines() :
            if '<control type="xbian" value="Menucategories"/>' in line :
                for category in self.categories :
                    xmlout.write(category.getTitleContent().toXml())
            elif '<control type="xbian" value="categories"/>' in line :
                for category in self.categories :
                    xmlout.write(category.getCategory().toXml())
                    #xmlout.write(category.getScrollBar().toXml())
            else :
                xmlout.write(line)
        xmltemplate.close()
        xmlout.close() 
