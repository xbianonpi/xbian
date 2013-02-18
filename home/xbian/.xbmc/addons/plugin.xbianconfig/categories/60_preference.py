from resources.lib.xbmcguie.xbmcContainer import *
from resources.lib.xbmcguie.xbmcControl import *
from resources.lib.xbmcguie.tag import Tag
from resources.lib.xbmcguie.category import Category,Setting

import os

from resources.lib.xbianconfig import xbianConfig

import xbmcgui

dialog=xbmcgui.Dialog()

class advancedLabel(Setting) :
    CONTROL = CategoryLabelControl(Tag('label','Advanced'))

class advancedMode(Setting) :
    CONTROL = RadioButtonControl(Tag('label','Advanced mode'))
    DIALOGHEADER = "Advanced Mode"
    ERRORTEXT = "Error on updating"
    OKTEXT = "Update ok"
    
    def onInit(self) :
        self.key = 'advancedmode'
                    
    def getUserValue(self):
        return str(self.getControlValue())
    
    def setControlValue(self,value) :
        if value == '1' :
            value = True
        else :
            value = False
        self.control.setValue(value)
    
    def getXbianValue(self):
        rc = self.getSetting(self.key)
        if rc == '1' :              
              xbmc.executebuiltin('Skin.SetBool(%s)'%self.key)
        else :              
              xbmc.executebuiltin('Skin.Reset(%s)'%self.key)
        return rc
        
    def setXbianValue(self,value):
        self.setSetting(self.key,str(value))
        xbmc.executebuiltin('Skin.ToggleSetting(%s)'%self.key)
        return True

class notificationLabel(Setting) :
    CONTROL = CategoryLabelControl(Tag('label','Notification'))

class notifyonError(advancedMode) :
    CONTROL = RadioButtonControl(Tag('label','Notify on error'))
    DIALOGHEADER = "Notification on Error"
    def onInit(self) :
        self.key = 'notifyonerror'
    
class notifyonSuccess(advancedMode) :
    CONTROL = RadioButtonControl(Tag('label','Notify on success'))
    DIALOGHEADER = "Notification on Success"
    def onInit(self) :
        self.key = 'notifyonsuccess'

class confirmonChange(advancedMode) :
    CONTROL = RadioButtonControl(Tag('label','Ask confirmation before saving'))
    DIALOGHEADER = "Confirm Modification"
    
    def onInit(self) :
        self.key = 'confirmationonchange'

class UpdateLabel(Setting) :
    CONTROL = CategoryLabelControl(Tag('label','Update'))

class updateonBoot(advancedMode) :
    CONTROL = RadioButtonControl(Tag('label','Check update on boot'))
    DIALOGHEADER = "Check Update on Boot"
    def onInit(self) :
        self.key = 'updateonboot'

class updateTimer(advancedMode) :
    CONTROL = RadioButtonControl(Tag('label','Check update every'))
    DIALOGHEADER = "Check Update Every"
    def onInit(self) :
        self.key = 'notifyonerror'

class updateAuto(advancedMode) :
    CONTROL = RadioButtonControl(Tag('label','Automatic update'))
    DIALOGHEADER = "Automatic Update"
    def onInit(self) :
        self.key = 'updateauto'

#CATEGORY CLASS
class preference(Category) :
    TITLE = 'Preferences'
    SETTINGS = [advancedLabel,advancedMode,notificationLabel,confirmonChange,notifyonError,notifyonSuccess]
    
    
