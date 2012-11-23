
# if we got here then someone tried to import pysqlite.dbapi2
# this will only be allowed if the script is greater that version 1.0

import warnings
import re

# Credit gnud on stackoverflow:
#  see http://stackoverflow.com/questions/1714027/version-number-comparison/1714190#1714190
def xbmcVerCmp(version1, version2):
    def normalize(v):
        return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
    return cmp(normalize(version1), normalize(version2))

# Not sure why this might fail but ....
try:
    import __main__
    xbmcapiversion = __main__.__xbmcapiversion__
except:
    xbmcapiversion = "1.0"
    warnings.warn("For some reason the module '" + str(__name__) + "' couldn't get access to '__main__'. This may prevent certain backward compatility modes from operating correctly.")

# if the xbmcapiversion is either not set (because trying to get it failed or 
#  the script was invoked in an odd manner from xbmc) ...
if (xbmcVerCmp(xbmcapiversion,"1.0") <= 0):
    # then import sqlite3 in place of dbapi2
    try:
        import sqlite3 as dbapi2
    except Exception, e:
        warnings.warn("Unable to import sqlite3. This probably means you're on a version of python prior to 2.5 and trying to run an old script.")
        raise e

    # ask politely :)
    warnings.warn("DeprecationWarning: the pysqlite2 module is deprecated; please change your script to use sqlite3.")
else:
    raise DeprecationWarning("You cannot use pysqlite2 while depending on version " + str(xbmcapiversion) + " of the xbmc.python api. Please use sqlite3 instead.")

