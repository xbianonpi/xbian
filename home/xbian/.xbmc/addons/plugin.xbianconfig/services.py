import xbmc
import xbmcgui
import os

onRun = os.path.join('/','tmp','.xbian_config_python')
if os.path.isfile(onRun) :
	os.remove(onRun)
	
from services.firstrun import firstrun
firstrun_thread = firstrun()     
firstrun_thread.onStart()

from services.upgrade import upgrade
upgrade_thread = upgrade()     
upgrade_thread.onStart()

from services.resize import resize
resize_thread = resize()     
resize_thread.onStart()

