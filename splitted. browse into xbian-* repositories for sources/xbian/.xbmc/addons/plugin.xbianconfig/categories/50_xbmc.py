from resources.lib.xbmcguie.xbmcContainer import *
from resources.lib.xbmcguie.xbmcControl import *
from resources.lib.xbmcguie.tag import Tag
from resources.lib.xbmcguie.category import Category,Setting

import os

from resources.lib.xbianconfig import xbianConfig

import xbmcgui

dialog=xbmcgui.Dialog()

class xbmcLabel(Setting) :
    CONTROL = CategoryLabelControl(Tag('label','Xbmc'))

class xbmcGui(Setting) :
    CONTROL = SpinControlex(Tag('label','XBMC GUI resolution'))
    DIALOGHEADER = "XBMC GUI resolution"
    ERRORTEXT = "Error updating"
    OKTEXT = "Update ok"
    SAVEMODE = Setting.ONUNFOCUS
    
    def onInit(self):
        resolutionlist =xbianConfig('xbmc','guires','list')
        if resolutionlist :
            for resolution in resolutionlist :
                content = Content(Tag('label','%sp'%resolution),defaultSKin=False)
                self.control.addContent(content)

    def getUserValue(self):
        return self.control.getValue()
        
    def getXbianValue(self):
        resolution =xbianConfig('xbmc','guires','select')
        if resolution :
            return '%sp'%resolution[0]
        else :
            return ''                
        
    def setXbianValue(self,value):
        value = value[:-1]
        rc = xbianConfig('xbmc','guires','update',value)
        if rc and rc[0] == '1' :
            return True
        else :
            return False
        
#CATEGORY CLASS
class xbmc(Category) :
    TITLE = 'XBMC'
    SETTINGS = [xbmcLabel,xbmcGui]
    
    
