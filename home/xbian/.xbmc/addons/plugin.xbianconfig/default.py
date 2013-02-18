# -*- coding: cp1252 -*-

__script__       = "Unknown"
__plugin__       = "xbian-config"
__addonID__      = "plugin.xbianconfig"
__author__       = "Belese (http://www.xbian.org)"
__url__          = "http://www.xbian.org"
__credits__      = "XBian"
__platform__     = "xbmc media center"
__date__         = "30-11-2012"
__version__      = "0.0.1"


import os
import sys
import itertools
import fnmatch
import shutil
import threading
import Queue

# xbmc modules
import xbmc
import xbmcgui
import xbmcplugin
from xbmcaddon import Addon

#xbmcguie
from resources.lib.xbianWindow import XbianWindow
from resources.lib.updateworker import Updater
from resources.lib.xbianconfig import xbianConfig
from resources.lib.utils import dialogWait
#addon module 
ADDON     = Addon( __addonID__ )
Language  = ADDON.getLocalizedString
ADDON_DIR = ADDON.getAddonInfo( "path" )
LangXBMC  = xbmc.getLocalizedString


ROOTDIR            = ADDON_DIR
BASE_RESOURCE_PATH = os.path.join( ROOTDIR, "resources" )
MEDIA_PATH         = os.path.join( BASE_RESOURCE_PATH, "media" )
ADDON_DATA  = xbmc.translatePath( "special://profile/addon_data/%s/" % __addonID__ )
CATEGORY_PATH = 'categories'
class xbian_config_python :
    def __init__(self) :              
        xbmc.log('XBian : XBian-config-python started')
        self.onRun = os.path.join('/','tmp','.xbian_config_python')
        if os.path.isfile(self.onRun) :
            xbmcgui.Dialog().ok('XBian-config','XBian-config is still running','Please wait...')
        else :      
            open(self.onRun,'w').close()
            try :            
                self.CmdQueue = Queue.Queue()
                self.updateThread = Updater(self.CmdQueue)
                self.updateThread.start()
                self.wait = xbmcgui.DialogProgress()
                self.window = XbianWindow('SettingsXbianInfo.xml',ROOTDIR)
                self.category_list = []
                self.category_list_thread = []
                self.category_list_instance = {}
                self.finished = 0
                self.stop = False
                for fn in os.listdir(os.path.join(ROOTDIR,CATEGORY_PATH)):
                    if fn[0] != '_' and fn.split('.')[-1] in ('py', 'pyw'):
                        modulename = fn.split('.')[0] # filename without extension
                        self.category_list.append(modulename)
                self.category_list.sort()
                self.total = len(self.category_list)
                self.wait.create('Generating Windows','Please wait..., this process can take up to one minute')
                self.wait.update(0)
                for module in self.category_list :
                    self.category_list_thread.append(threading.Thread(None,self.threadInitCategory, None, (module,)))
                    self.category_list_thread[-1].start()
                for i,threadInst in enumerate(self.category_list_thread):
                    if not self.stop :
                        threadInst.join()
                        try :
                            self.window.addCategory(self.category_list_instance[self.category_list[i]])
                        except:
                            xbmc.log('XBian : Cannot add category: %s \n%s'%(str(self.category_list[i]),str(sys.exc_info())))                            
                if not self.stop :
                    self.window.doXml(os.path.join(ROOTDIR,'resources','skins','Default','720p','SettingsXbianInfo.template'))
                    self.wait.close()                    
                    self.window.doModal() 
                    xbmc.log('XBian : XBian-config-python closed')
                    self.window.stopRequested = True 
                    progress = dialogWait('XBian config','Checking if reboot is needed...')
                    progress.show() 
                    rebootneeded = xbianConfig('reboot')
                    progress.close()
                    if rebootneeded and rebootneeded[0] == '1' :
                        if xbmcgui.Dialog().yesno('XBian-config','A reboot is needed','Do you want to reboot now?') :
                            #reboot
                            xbmc.executebuiltin('Reboot')
            except :
                self.window.stopRequested = True            
                xbmcgui.Dialog().ok('XBian-config','Something went wrong while creating the window','Please contact us on www.xbian.org for further support')
                xbmc.log('XBian : Cannot create Main window: %s'%(str(sys.exc_info())))                            
            finally :
                self.updateThread.stop()
                os.remove(self.onRun)
        
    def update_progress(self) :
        self.finished += 1
        if self.wait.iscanceled() :
            self.stop = True
            self.wait.close()
        else :
            perc = int((float(self.finished)/(self.total*2)) * 100)            
            self.wait.update(perc)
        
    def threadInitCategory(self,modulename) :        
        globals_, locals_ = globals(), locals()
        subpackage = ".".join([CATEGORY_PATH, modulename])
        module = __import__(subpackage, globals_, locals_, [modulename])                       
        self.update_progress()
        catInstance = getattr(module,modulename.split('_')[1])
        self.category_list_instance[modulename] = catInstance(self.CmdQueue)        
        self.update_progress()


xbian_config_python()
