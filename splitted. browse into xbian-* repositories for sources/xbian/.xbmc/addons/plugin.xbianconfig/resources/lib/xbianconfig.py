import subprocess
import xbmc

def xbianConfig(*args):
        cmd = ['sudo','/usr/local/sbin/xbian-config']
        cmd.extend(args)
        rc= subprocess.check_output(cmd)
        rcs = rc.split('\n')
        result  = filter(lambda x: len(x)>0, rcs)
        xbmc.log('XBian : xbian-config %s : %s '%(' '.join(cmd[2:]),str(result)),xbmc.LOGDEBUG)
        return result
        

