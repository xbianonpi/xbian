import xbmcgui
import xbmc
from resources.lib.service import service
from xbmcaddon import Addon
from resources.lib.utils import *
import os

__addonID__ = "plugin.xbianconfig"
ADDON     = Addon( __addonID__ )
ADDON_DATA  = xbmc.translatePath( "special://profile/addon_data/%s/" % __addonID__ )
ADDON_DIR = ADDON.getAddonInfo( "path" )
LangXBMC  = xbmc.getLocalizedString
ROOTDIR            = ADDON_DIR

class firstrun(service):
    def onStart(self):
        #check if first run        
        firstlock = os.path.join(ADDON_DATA,'.firstrun')
        if not os.path.isfile(firstlock) :
        	        if not os.path.exists(ADDON_DATA):
                            os.mkdir(ADDON_DATA)
			setSetting('advancedmode','0')
			setSetting('notifyonerror','1')
			setSetting('notifyonsuccess','1')
			setSetting('confirmationonchange','1')
        	#set default preference:			
			self.dlg = xbmcgui.WindowXMLDialog('welcomeDialog.xml',ROOTDIR)
			self.dlg.doModal()
			
			#xbmcgui.Dialog().ok('Welcome to XBian','Thanks to have chosen XBian','You can configure it, go to','System -> XBian')
			open(firstlock,'w').close()			
