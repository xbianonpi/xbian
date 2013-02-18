import os
import subprocess
import time
import random
import string

from resources.lib.xbmcguie.xbmcContainer import *
from resources.lib.xbmcguie.xbmcControl import *
from resources.lib.xbmcguie.tag import Tag
from resources.lib.xbmcguie.category import Category,Setting

from resources.lib.xbianconfig import xbianConfig
from resources.lib.utils import dialogWait
import xbmcgui,xbmc
from xbmcaddon import Addon

__addonID__      = "plugin.xbianconfig"
ADDON     = Addon( __addonID__ )
ADDON_DIR = ADDON.getAddonInfo( "path" )
ROOTDIR            = ADDON_DIR
BASE_RESOURCE_PATH = os.path.join( ROOTDIR, "resources" )



class updateControl(MultiSettingControl):
    XBMCDEFAULTCONTAINER = False
   
    def onInit(self) :
        char_set = string.ascii_lowercase
        self.key = ''.join(random.sample(char_set,6))
        self.keyupdateall = '%sall'%self.key
        self.nbUpdate = 10
        self.nbcanbeupdate = 0
        self.updates = []
        for i in range(self.nbUpdate) :
            self.updates.append({})
        
        keynoupdate = ''
        for i,update in enumerate(self.updates) :
            xbmc.executebuiltin('Skin.Reset(%s%d)'%(self.key,i))
            update['name'] = ButtonControl(Tag('visible','skin.hasSetting(%s%d)'%(self.key,i)))
            update['name'].onClick = lambda update : self.onUpdateClick(self.getCurrentUpdate(update))
            self.addControl(update['name'])
            keynoupdate+='!Control.IsVisible(%d) + '%update['name'].getId()
        keynoupdate = keynoupdate[:-3]
        xbmc.executebuiltin('Skin.Reset(%s)'%(self.keyupdateall))
        self.udpateAll = ButtonControl(Tag('label','Update all'),Tag('visible','skin.hasSetting(%s)'%(self.keyupdateall)))
        self.udpateAll.onClick = lambda updateall : self.onUpdateAll()
        self.addControl(self.udpateAll)
        
        self.udpateNo = ButtonControl(Tag('label','Up-to-date'),Tag('visible','%s'%keynoupdate))
        self.addControl(self.udpateNo)
                
        
    def getCurrentUpdate(self,control):
        for i,update in enumerate(self.updates) :
            if update['name'] == control :
                return i+1
            
    def addUpdate(self,update) :        
        values = update.split(';')        
        self.updates[int(values[0])-1]['name'].setLabel(values[1])
        self.updates[int(values[0])-1]['name'].setValue(values[3])
        xbmc.executebuiltin('Skin.SetBool(%s%d)'%(self.key,int(values[0])-1))
        self.nbcanbeupdate += 1
        if self.nbcanbeupdate == 2 :
			xbmc.executebuiltin('Skin.SetBool(%s)'%self.keyupdateall)
    
    def removeUpdate(self,update)  :   
        values = update.split(';')
        xbmc.executebuiltin('Skin.Reset(%s%d)'%(self.key,int(values[0])-1))
        self.nbcanbeupdate -= 1
        if self.nbcanbeupdate == 1 :
			xbmc.executebuiltin('Skin.Reset(%s)'%self.keyupdateall)
			
    def onUpdateClick(self,updateId) :
        pass
            
    def onUpdateAll(self) :
        pass
        
class upgradeXbianLabel(Setting) :
    CONTROL = CategoryLabelControl(Tag('label','XBian'))      

class xbianUpgrade(Setting) :
    CONTROL = updateControl()
    DIALOGHEADER = "XBian Upgrade"
    ERRORTEXT = "Error"
    OKTEXT = "OK"
    APPLYTEXT = "Do you want to upgrade XBian"

    def onInit(self) :
        self.control.onUpdateClick = self.onUpdate       
        self.control.onUpdateAll = self.onUpdateAll
        self.keyword()
    
    def keyword(self) :
        self.key = 'upgrades'
                    
    def onUpdate(self,updateId):
        lockfile = '/var/lock/.%s'%self.key
        open(lockfile,'w').close()
        updateId = str(updateId)        
        if self.askConfirmation(True) :
			dlg = dialogWait('Xbian Update','Please wait while updating')
			dlg.show()			
			rc =xbianConfig('updates','install',self.key,updateId)
			if rc and rc[0] == '1' :
				#wait upgrade
				while not xbmc.abortRequested and xbianConfig('updates','progress')[0] == '1':
					time.sleep(2)
				if xbmc.abortRequested :
					return None
				else :
					os.remove(lockfile) 
					#remove update from list
					updateList = updateId.split(' ')
					for updates in updateList :
						for update in self.xbianValue :
							if update.split(';')[0] == updates :
								self.xbianValue.remove(update)
								self.control.removeUpdate(update)
								break
					dlg.close()
					self.notifyOnSuccess()
			else :
				if rc and rc[0] == '2' :
					self.ERRORTEXT = 'These packages are already updated'           
				elif rc and rc[0] == '3' :
					self.ERRORTEXT = 'Packages not found in apt repository'
				elif rc and rc[0] == '4' :
					self.ERRORTEXT = 'Packages not found in apt repository'
				elif rc and rc[0] == '5' :
					self.ERRORTEXT = 'There is a size mismatch for the remote packages'             
				elif rc and rc[0] == '6' :
					self.ERRORTEXT = 'The packages itselves got a internal error'
				else :
					self.ERRORTEXT = 'Unexpected error'            
				os.remove(lockfile)
				dlg.close()
				self.notifyOnError()    
            
    def onUpdateAll(self) :
        updates = ''
        for update in self.xbianValue :         
            updates += '%s '%(update.split(';')[0])
        self.onUpdate(updates)
        
    def getXbianValue(self):
        rc =xbianConfig('updates','list',self.key)
        if rc and rc[0] == '-3' :
            rctmp = xbianConfig('updates','updatedb')
            if rctmp and rctmp[0] == '1' :
                 rc =xbianConfig('updates','list',self.key)
            else :
                rc[0]= '0'
        if rc and rc[0] not in ('0','-2') : 
            for update in rc :
                self.control.addUpdate(update)
        return rc

class updatePackageLabel(Setting) :
    CONTROL = CategoryLabelControl(Tag('label','Packages'))      

class packageUpdate(xbianUpgrade) :
    CONTROL = updateControl()
    DIALOGHEADER = "Update Packages"
    ERRORTEXT = "Error"
    OKTEXT = "Package is successfully updated"
    APPLYTEXT = "Do you want to update this package?"


    def keyword(self) :
        self.key = 'packages'
            

class update(Category) :
    TITLE = 'Update'
    SETTINGS = [upgradeXbianLabel,xbianUpgrade,updatePackageLabel,packageUpdate]
    


