import xbmcgui
import xbmc
from resources.lib.service import service
from resources.lib.xbianconfig import xbianConfig

class resize(service):
    def onStart(self):
        #check if resize sd is needed
        rc = xbianConfig('resizesd','check')
        if rc and rc[0] == '1' :
			dialog = xbmcgui.Dialog()
			if dialog.yesno('Resize SD','Your SD card is not resized','Do you want to resize now?') :
				rc = xbianConfig('resizesd','resize')
				if rc and rc[0] == '1' :
					if dialog.yesno('Resize SD','Resize SD card will be done on next reboot','Do you want to reboot now?') :
						xbmc.executebuiltin('Reboot')
				else :
					xbmc.executebuiltin("Notification(%s,%s)"%('Resize SD','Something went wrong when resizing SD'))
