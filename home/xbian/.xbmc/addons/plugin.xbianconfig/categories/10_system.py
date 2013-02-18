from resources.lib.xbmcguie.xbmcContainer import *
from resources.lib.xbmcguie.xbmcControl import *
from resources.lib.xbmcguie.tag import Tag
from resources.lib.xbmcguie.category import Category,Setting

from resources.lib.xbianconfig import xbianConfig
from resources.lib.utils import *


import xbmcgui
import os

dialog=xbmcgui.Dialog()

class NewtorkLabel(Setting) :
    CONTROL = CategoryLabelControl(Tag('label','Network'))
    
class NetworkControl(MultiSettingControl):
    XBMCDEFAULTCONTAINER = False
    DHCP = 'DHCP'
    STATIC = 'Static'
    
    def onInit(self) :
        self.interface = SpinControlex(Tag('label','Interface'))
        self.addControl(self.interface)
        self.interfacelist = xbianConfig('network','list')
        self.interfaceValue = {}

        for interface in self.interfacelist :
             self.interfaceValue[interface] = {}
             self.interfaceValue[interface]['content'] = Content(Tag('label',interface),defaultSKin=False)
             self.interface.addContent(self.interfaceValue[interface]['content'])
             
             #create the interface group
             self.interfaceValue[interface]['group'] = MultiSettingControl(Tag('visible','Container(%d).HasFocus(%d)'%(self.interface.getWrapListId(),self.interfaceValue[interface]['content'].getId())))
             self.addControl(self.interfaceValue[interface]['group'])
             
             #add status control
             self.interfaceValue[interface]['status'] = ButtonControl(Tag('label',' -Status'))
             self.interfaceValue[interface]['group'].addControl(self.interfaceValue[interface]['status'])
             
             #check if Wifi
             self.interfaceValue[interface]['wifi'] = False
             if xbianConfig('network','type',interface)[0] == '1':
                 self.interfaceValue[interface]['wifi'] = True
                 self.interfaceValue[interface]['ssid'] = ButtonControl(Tag('label',' -Ssid'))
                 self.interfaceValue[interface]['ssid'].onClick = lambda wifi : self.wifi(interface) 
                 self.interfaceValue[interface]['group'].addControl(self.interfaceValue[interface]['ssid'])
                 
             
             #add interface mode Control (static/dhcp)
             self.interfaceValue[interface]['mode'] = SpinControlex(Tag('label',' -Mode'))
             dhcp = Content(Tag('label',self.DHCP),defaultSKin=False)
             static = Content(Tag('label',self.STATIC),defaultSKin=False)
             self.interfaceValue[interface]['mode'].addContent(dhcp)
             self.interfaceValue[interface]['mode'].addContent(static)
             self.interfaceValue[interface]['group'].addControl(self.interfaceValue[interface]['mode'])
             
             #add Static Group
             self.interfaceValue[interface]['staticgroup'] = MultiSettingControl(Tag('visible','Container(%d).HasFocus(%d)'%(self.interfaceValue[interface]['mode'].getWrapListId(),static.getId())))
             self.interfaceValue[interface]['ipadress'] = ButtonControl(Tag('label','  -Adress'))
             self.interfaceValue[interface]['ipadress'].onClick = lambda ipadress: ipadress.setValue(getIp('Ip adress',ipadress.getValue()))
             self.interfaceValue[interface]['subnet'] = ButtonControl(Tag('label','  -Subnet'))
             self.interfaceValue[interface]['subnet'].onClick = lambda subnet: subnet.setValue(getIp('Subnet',subnet.getValue()))
             self.interfaceValue[interface]['gateway'] = ButtonControl(Tag('label','  -Gateway'))
             self.interfaceValue[interface]['gateway'].onClick = lambda gateway: gateway.setValue(getIp('Gateway',gateway.getValue()))
             self.interfaceValue[interface]['dns1'] = ButtonControl(Tag('label','  -Primary Dns'))
             self.interfaceValue[interface]['dns1'].onClick = lambda dns1: dns1.setValue(getIp('Primary Dns',dns1.getValue()))
             self.interfaceValue[interface]['dns2'] = ButtonControl(Tag('label','  -Secondary Dns'))
             self.interfaceValue[interface]['dns2'].onClick = lambda dns2: dns2.setValue(getIp('Primary Dns',dns2.getValue()))
             self.interfaceValue[interface]['staticgroup'].addControl(self.interfaceValue[interface]['ipadress'])
             self.interfaceValue[interface]['staticgroup'].addControl(self.interfaceValue[interface]['subnet'])
             self.interfaceValue[interface]['staticgroup'].addControl(self.interfaceValue[interface]['gateway'])
             self.interfaceValue[interface]['staticgroup'].addControl(self.interfaceValue[interface]['dns1'])
             self.interfaceValue[interface]['staticgroup'].addControl(self.interfaceValue[interface]['dns2'])
             self.interfaceValue[interface]['group'].addControl(self.interfaceValue[interface]['staticgroup'])
             
                
    def setValue(self,values):        
        default = values[0]
        #self.interface.setValue(default)
        networkValue = values[1]
        for key in networkValue :
            value = networkValue[key]           
            if value[0] == 'static' :
                self.interfaceValue[key]['mode'].setValue(self.STATIC)
            else:
                self.interfaceValue[key]['mode'].setValue(self.DHCP)
         
            self.interfaceValue[key]['status'].setValue(value[1])    
            self.interfaceValue[key]['ipadress'].setValue(value[2])            
            self.interfaceValue[key]['subnet'].setValue(value[3])
            self.interfaceValue[key]['gateway'].setValue(value[4])
            self.interfaceValue[key]['dns1'].setValue(value[5])            
            self.interfaceValue[key]['dns2'].setValue(value[6])
            
            if self.interfaceValue[key]['wifi'] :
                self.interfaceValue[key]['ssid'].setValue('%s'%value[7]) 
               
   
    def wifi(self,interface) :
        pass
        
    def getValue(self) :
       default = self.interface.getValue()
       networkValue = {}
       for interface in self.interfacelist :           
           networktmp = self.interfaceValue[interface]['group'].getValue()
           #sort to be compliant to xbianconfig
           networkValue[interface] = []           
           if self.interfaceValue[interface]['wifi'] :
               networkValue[interface].append(networktmp[2].lower())
               networkValue[interface].append(networktmp[0])
               networkValue[interface].append(networktmp[3])
               networkValue[interface].append(networktmp[4])
               networkValue[interface].append(networktmp[5])
               networkValue[interface].append(networktmp[6])
               networkValue[interface].append(networktmp[7])
               networkValue[interface].append(networktmp[1])
           else :
               networkValue[interface].append(networktmp[1].lower())
               networkValue[interface].append(networktmp[0])
               networkValue[interface].append(networktmp[2])
               networkValue[interface].append(networktmp[3])
               networkValue[interface].append(networktmp[4])
               networkValue[interface].append(networktmp[5])
               networkValue[interface].append(networktmp[6])
       return [default,networkValue]
        
class NetworkSetting(Setting) :
    CONTROL = NetworkControl()
    DIALOGHEADER = "Network Settings"
    ERRORTEXT = "Error on updating"
    OKTEXT = "Update ok"
    SAVEMODE = Setting.ONUNFOCUS
    
#    def setControlValue(self,value): 
#            self.getControl().setValue(val)
    
    def onInit(self) :
        self.control.wifi = self.connectWifi
        
    def connectWifi(self,interface) :
        self.userValue = self.getUserValue()
        if self.isModified() :
            progress = dialogWait('Updating','Updating settings for %s'%(interface))
            progress.show()              
            self.setXbianValue(self.userValue)
            progress.close()
            
        if wifiConnect(interface) :
            progress = dialogWait('Refresh','Reloading values for %s'%(interface))
            progress.show()              
            interface_config = xbianConfig('network','status',interface)
            lanConfig = []
            for config in interface_config :
                try :            
                    val = config.split(' ')             
                    if val[0] == 'mode' and val[1] == 'manual':
                        val[1] = 'dhcp'      
                    if val[0] == 'ssid' and not val[1]:
                        val[1] = 'Not connected'               
                    if not val[0] in ('protection','key') :
                        lanConfig.append(val[1])                                    
                except :
                    print 'XBian : Cannot refreh wifi settings'
                    lanConfig.append(None)    
            self.xbianValue[interface] = lanConfig 
            progress.close()
            #sleep a bit otherwise windows is not ready, and there's a xbmc bug i think.
            time.sleep(0.6)
            self.setControlValue({interface : lanConfig})
            self.OKTEXT = '%s successfully connected'%interface
            self.notifyOnSuccess()
        else :
            self.ERRORTEXT = 'Cannot connect %s'%interface
            self.notifyOnError()    
        
    def setControlValue(self,value) :
        self.control.setValue([self.default,value])
    
    def isModified(self) :
        equal = False
        for key in self.userValue :
            if self.xbianValue[key][0] != self.userValue[key][0] :
                equal = True
                break
            if self.userValue[key][0] != 'dhcp' :
                j = (0,2,3,4,5,6)
                for i in j :
                    if self.xbianValue[key][i] != self.userValue[key][i] :
                        equal = True
                        break
        return equal 
    
    def getUserValue(self):
        tmp = self.getControl().getValue()
        self.default = tmp[0]
        return tmp[1]
    
    def getXbianValue(self):
        self.default = False
        self.lanConfig={}
        for interface in self.getControl().interfacelist :
            interface_config = xbianConfig('network','status',interface)
            if interface_config[2] == 'UP' or not self.default :
                self.default = interface
            self.lanConfig[interface] = []
            for config in interface_config :
                try :
                    val = config.split(' ')             
                    if val[0] == 'mode' and val[1] == 'manual':
                        val[1] = 'static'      
                    if val[0] == 'ssid' and not val[1]:
                        val[1] = 'Not connected'               
                    if not val[0] in ('protection','key') :
                        self.lanConfig[interface].append(val[1])                    
                except :
                    self.lanConfig[interface].append(None)    
        return self.lanConfig
    
    def setXbianValue(self,values):
        ok = True
        for interface in values :
            if values[interface] != self.xbianValue[interface]:
                if values[interface][0].lower() == NetworkControl.DHCP.lower() :
                    mode = 'dhcp'
                    cmd = [mode,interface]
                else :
                     mode = 'static'
                     cmd = [mode,interface,values[interface][2],values[interface][3],values[interface][4],values[interface][5],values[interface][6]]
                rc = xbianConfig('network',*cmd)                
                if not rc :
                    ok = False
                    self.ERRORTEXT = "No return code from xbian-config"
                elif rc[0] != '1' : 
                    ok = False
                    self.ERRORTEXT = rc[1]
        return ok           
        
        
class LicenceLabel(Setting) :
    CONTROL = CategoryLabelControl(Tag('label','Licenses'))

class mpeg2License(Setting) :
    CONTROL = ButtonControl(Tag('label','MPG2'))
    DIALOGHEADER = "MPEG2 license"
    ERRORTEXT = "Error updating"
    OKTEXT = "Update ok"
    BADUSERENTRYTEXT = "A license must be 9 or 10 characters long and looks like 0x00000000"
    
    def onInit(self) :
        self.xbiankey = 'licensempg2'
        
    def getUserValue(self):
        return getText(self.DIALOGHEADER,self.getControlValue())
        
    def checkUserValue(self,value):
        try :
            hexvalue = int(value,16)
            keyok = ((len(value) == 10) or (len(value) == 9))  and value[:2] == '0x'
        except :
            keyok = False   
        return keyok
    
    def getXbianValue(self):
        licenseValue =xbianConfig(self.xbiankey,'select')
        if licenseValue and licenseValue[0][:2] == '0x' :
            self.XbianLicenseCmd = 'update'
            return licenseValue[0]
        else :
            if len(licenseValue) == 0 or licenseValue[0] == "" :
                self.XbianLicenseCmd = 'insert'
            else :
                self.XbianLicenseCmd = 'update'
            return '0x'                  
    
        
    def setXbianValue(self,value):
        rc = xbianConfig(self.xbiankey,self.XbianLicenseCmd,value)
        ok = True
        if not rc: 
            ok = False
        elif rc[0] != '1' :
            ok = False
        return ok       
        
    
class vc1License(mpeg2License) :
    CONTROL = ButtonControl(Tag('label','VC1'))
    DIALOGHEADER = "VC1 license"
    
    def onInit(self) :
        self.xbiankey = 'licensevc1'
    
class connectivityLabel(Setting) :
    CONTROL = CategoryLabelControl(Tag('label','Connectivity'),Tag('visible','skin.hasSetting(advancedmode)'))

class videooutputControl(MultiSettingControl):
    XBMCDEFAULTCONTAINER = False
    
    def onInit(self) :
        self.videooutputlist = xbianConfig('videoflags','list')
        self.videooutputcontrol = {}
        for videooutput in self.videooutputlist :
            guiname = videooutput.replace('_',' ').capitalize()
            self.videooutputcontrol[videooutput] = RadioButtonControl(Tag('label',guiname))
            self.videooutputcontrol[videooutput].onClick = lambda forwardclick : self.onClick(self)
            self.addControl(self.videooutputcontrol[videooutput])
        
    def setValue(self,values) :
        for key in values :
            if values[key] == '1' :
                boolvalue = True
            else :
                boolvalue = False
            self.videooutputcontrol[key].setValue(boolvalue)
            
    def getValue(self) :
        rc = {}
        for videooutput in self.videooutputlist :
            rc[videooutput] = str(self.videooutputcontrol[videooutput].getValue())
        return rc
            
            
            

class videooutput(Setting) :
    CONTROL = videooutputControl(Tag('visible','skin.hasSetting(advancedmode)'))
    DIALOGHEADER = "Video output "
    ERRORTEXT = "Error on updating"
    OKTEXT = "Update ok"
                    
    def onInit(self) :
        self.listvalue = xbianConfig('videoflags','list')
        self.value = {}
        
    def getUserValue(self):
        return self.getControlValue()
    
    def getXbianValue(self):
        for value in self.listvalue :
            if not self.value.has_key(value) :
                self.value[value] = xbianConfig('videoflags','select',value)[0]
        return self.value
        
    def setXbianValue(self,value):
        #set xbian config here
        for key in value :
            if value[key] != self.xbianValue[key] :
                 rc = xbianConfig('videoflags','update',key,value[key])
                 self.DIALOGHEADER = key.replace('_',' ').title()
                 break
        if rc and rc[0] == '1' :
            return True
        else :
            return False

class SytemLabel(Setting) :
    CONTROL = CategoryLabelControl(Tag('label','System'),Tag('visible','skin.hasSetting(advancedmode)'))
            
    
class hostname(Setting) :
    CONTROL = ButtonControl(Tag('label','Hostname'),Tag('visible','skin.hasSetting(advancedmode)'))
    DIALOGHEADER = "Hostname"
    ERRORTEXT = "Error updating"
    OKTEXT = "Update ok"
    BADUSERENTRYTEXT = "You used invalid characters in the new hostname"
        
    def getUserValue(self):
        return getText(self.DIALOGHEADER,self.getControlValue())
        
    def checkUserValue(self,value):
        return value.isalnum()
    
    def getXbianValue(self):
        licenseValue =xbianConfig('hostname','select')
        if licenseValue :
            return licenseValue[0]
        else :
            return ''                
        
    def setXbianValue(self,value):
        rc = xbianConfig('hostname','update',value)
        ok = True
        if not rc: 
            ok = False
        elif rc[0] != '1' :
            ok = False
        return ok       

class kernel(Setting) :
    CONTROL = SpinControlex(Tag('label','Kernel'),Tag('visible','skin.hasSetting(advancedmode)'))
    DIALOGHEADER = "Kernel Version"
    ERRORTEXT = "Error updating"
    OKTEXT = "Update ok"
    SAVEMODE = Setting.ONUNFOCUS
    
    def onInit(self):
        kernellist =xbianConfig('kernel','list')
        for kernel in kernellist :
            content = Content(Tag('label',kernel),defaultSKin=False)
            self.control.addContent(content)

    def getUserValue(self):
        return self.control.getValue()
        
    def getXbianValue(self):
        kernelVersion =xbianConfig('kernel','select')
        if kernelVersion :
            return kernelVersion[0]
        else :
            return ''                
        
    def setXbianValue(self,value):
        rc = xbianConfig('kernel','update',value)
        ok = True
        if not rc: 
            ok = False
        elif rc[0] != '1' :
            if rc[0] == '-1' :
                self.ERRORTEXT = 'Insufficient number of arguments'
            elif rc[0] == '-2' :
                self.ERRORTEXT = 'Already running this kernel'
            elif rc[0] == '-3' :
                self.ERRORTEXT = "Kernel version doesn't exist"
            ok = False
        return ok

class OverclockControl(MultiSettingControl):
    XBMCDEFAULTCONTAINER = False
    
    def onInit(self) :
        self.overclockMode = SpinControlex(Tag('label','Overclocking'))
        self.addControl(self.overclockMode)
        self.overclockinglist = xbianConfig('overclocking','list')

        for mode in self.overclockinglist :
             content = Content(Tag('label',mode),defaultSKin=False)
             self.overclockMode.addContent(content)
             if mode == 'Custom' :
                 self.customOverclock = MultiSettingControl(Tag('visible','Container(%d).HasFocus(%d)'%(self.overclockMode.getWrapListId(),content.getId())))
                 self.Arm = ButtonControl(Tag('label',' -Arm'))
                 self.Core = ButtonControl(Tag('label',' -Core'))
                 self.Sdram = ButtonControl(Tag('label',' -SDram'))
                 self.Overvoltage = ButtonControl(Tag('label',' -Overvoltage'))
                 self.customOverclock.addControl(self.Arm)
                 self.customOverclock.addControl(self.Core)
                 self.customOverclock.addControl(self.Sdram)
                 self.customOverclock.addControl(self.Overvoltage)
                 self.addControl(self.customOverclock)
    
    def setValue(self,value):
        if value :            
            #trick to get list in lower case
            for val in self.overclockinglist :
                if value[0] == val.lower() :
                    break
            self.overclockMode.setValue(val)
            self.Arm.setValue(value[1])
            self.Arm.onClick = lambda arm: self.Arm.setValue(getNumeric('Arm Overclocking',value[1],400,1200))
            self.Core.setValue(value[2])    
            self.Core.onClick = lambda core: self.Core.setValue(getNumeric('Arm Overclocking',value[2],100,600))
            self.Sdram.setValue(value[3])
            self.Sdram.onClick = lambda sdram: self.Sdram.setValue(getNumeric('Arm Overclocking',value[3],100,600))
            self.Overvoltage.setValue(value[4])
            self.Overvoltage.onClick = lambda overvolt: self.Overvoltage.setValue(getNumeric('Arm Overclocking',value[4],0,12))

class overclocking(Setting) :
    CONTROL = OverclockControl(Tag('visible','skin.hasSetting(advancedmode)'))
    DIALOGHEADER = "Overclocking"
    ERRORTEXT = "Error updating"
    OKTEXT = "Update ok"
    SAVEMODE = Setting.ONUNFOCUS
            
    def getUserValue(self):
        values =  self.control.getValue()
        if values :
            values[0] = values[0].lower()
        return values
        
    def getXbianValue(self):
        overclock =xbianConfig('overclocking','select')
        value = xbianConfig('overclocking','values')       
        if overclock and value:
            overclock.extend(value[0].split(' '))          
            return overclock
        else :
            return []                
        
    def setXbianValue(self,value):
        if value[0] != 'custom' :
            val = [value[0]]
        else :
            val = value
        
        rc = xbianConfig('overclocking','update',*val)
        ok = True
        if not rc: 
            ok = False
        elif rc[0] != '1' :
            if rc[0] == '-1' :
                self.ERRORTEXT = "preset doesn't exist"
            elif rc[0] == '-2' :
                self.ERRORTEXT = 'invalid number of arguments'
            elif rc[0] == '-3' :
                self.ERRORTEXT = "non-numeric arguments"
            ok = False
        return ok


class timezone(Setting) :
    CONTROL = ButtonControl(Tag('label','Timezone'),Tag('visible','skin.hasSetting(advancedmode)'))
    DIALOGHEADER = "Timezone"
    ERRORTEXT = "Error updating"
    OKTEXT = "Update ok"
    
    def setControlValue(self,value) :
        self.control.setValue('%s / %s'%(value[0].title(),value[1].title()))
            
    def getUserValue(self):
        continentList = xbianConfig('timezone','list')
        continentgui = []
        have_to_stop = False
        while not have_to_stop :
            for continent in continentList :
                continentgui.append(continent.replace('_',' ').title())
            rcr = dialog.select('Region',continentgui)
            if rcr == -1 :
                have_to_stop = True
            else :
                countrylist = xbianConfig('timezone','list',continentList[rcr])
                countrygui = []
                for country in countrylist :
                    countrygui.append(country.replace('_',' ').title())
                rcc = dialog.select('Location',countrygui)
                if rcc != -1 :
                   return [continentList[rcr],countrylist[rcc]]
        return self.xbianValue
        
    def getXbianValue(self):
        timezone =xbianConfig('timezone','select')
        if timezone and timezone[0] != '-1':
            return(timezone[0].split(' '))          
        else :
            return ['Not Set','Not Set']                
        
    def setXbianValue(self,value):
        rc = xbianConfig('timezone','update',*value)
        ok = True
        if not rc or not rc[0]: 
            ok = False
        return ok

class AccountLabel(Setting) :
    CONTROL = CategoryLabelControl(Tag('label','Account'),Tag('visible','skin.hasSetting(advancedmode)'))
    
    def onInit(self):
        #check if advanced mode is set
        #must check here and not in preference since value are read one by one when plugin start.
        #and this setting is read before preference - advanced mode
        key = 'advancedmode'
        rc = self.getSetting(key)
        if rc == '1' :
            xbmc.executebuiltin('Skin.SetBool(%s)'%key)
        else :
            xbmc.executebuiltin('Skin.Reset((%s)'%key)
    
class rootpwd(Setting) :
    CONTROL = ButtonControl(Tag('label','root password'),Tag('visible','skin.hasSetting(advancedmode)'))
    DIALOGHEADER = "User root password"
    ERRORTEXT = "Error updating"
    OKTEXT = "Update ok"
    BADUSERENTRYTEXT = "Passwords don't match"
        
    def onInit(self):
        self.forceUpdate = True
        self.password = None
        self.key = 'rootpass'
        
    def checkUserValue(self,value):
        return self.password == self.confirmpwd
    def getUserValue(self):
        self.password = getText(self.DIALOGHEADER,hidden=True)
        self.confirmpwd = getText('Confirm ' + self.DIALOGHEADER,hidden=True)
        return '*****'
        
    def getXbianValue(self):
        return '*****'                
        
    def setXbianValue(self,value):
        rc = xbianConfig(self.key,'update',self.password)
        ok = True
        if not rc: 
            ok = False
        elif rc[0] != '1' :
            ok = False
        return ok       

class xbianpwd(rootpwd) :
    CONTROL = ButtonControl(Tag('label','xbian password'),Tag('visible','skin.hasSetting(advancedmode)'))
    DIALOGHEADER = "User xbian Password"
    
    def onInit(self):
        self.forceUpdate = True
        self.password = None
        self.key = 'xbianpass'
    
class sshroot(Setting) :
    CONTROL = RadioButtonControl(Tag('label','Allow SSH root login'),Tag('visible','skin.hasSetting(advancedmode)'))
    DIALOGHEADER = "SSH root"
    ERRORTEXT = "Error on updating"
    OKTEXT = "Update ok"
    
                    
    def getUserValue(self):
        return str(self.getControlValue())
    
    def setControlValue(self,value) :
        if value == '1' :
            value = True
        else :
            value = False
        self.control.setValue(value)
    
    def getXbianValue(self):
        rc = xbianConfig('sshroot','status')
        return rc[0]
        
    def setXbianValue(self,value):
        if value == '1':
            cmd = 'enable'
        else :
            cmd = 'disable'
        rc = xbianConfig('sshroot',cmd)
        ok = True
        if not rc: 
            ok = False
        elif rc[0] != '1' :
            ok = False
        return ok       

#CATEGORY CLASS
class system(Category) :
    TITLE = 'System'
    SETTINGS = [SytemLabel,hostname,timezone,kernel,overclocking,AccountLabel,rootpwd,xbianpwd,sshroot,NewtorkLabel,NetworkSetting,connectivityLabel,videooutput,LicenceLabel,mpeg2License,vc1License]
