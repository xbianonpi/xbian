import os
import subprocess
import time

from resources.lib.xbmcguie.xbmcContainer import *
from resources.lib.xbmcguie.xbmcControl import *
from resources.lib.xbmcguie.tag import Tag
from resources.lib.xbmcguie.category import Category,Setting

from resources.lib.xbianconfig import xbianConfig
from resources.lib.utils import *
import xbmcgui,xbmc
from xbmcaddon import Addon

__addonID__      = "plugin.xbianconfig"
ADDON     = Addon( __addonID__ )
ADDON_DIR = ADDON.getAddonInfo( "path" )
ROOTDIR            = ADDON_DIR
BASE_RESOURCE_PATH = os.path.join( ROOTDIR, "resources" )

dialog = xbmcgui.Dialog()

RUNNING = 'running'
STOPPED = 'stopped'
RESTART = 'Restart'
STOP = 'Stop'
START = 'Start'

class ServicesControl(MultiSettingControl):
    XBMCDEFAULTCONTAINER = False
   

    def onInit(self) :
        self.nbCustom = 10
        self.serviceStatus = xbianConfig('services','status')
        self.customId = 0
        self.serviceList = []
        for service in self.serviceStatus :
            self.serviceList.append(service.split(' ')[0])
        self.services = {}
        for i in range(self.nbCustom) :
            self.serviceList.append('custom%d'%i)
        for service in self.serviceList :
            self.services[service] = {}
            xbmc.executebuiltin('Skin.Reset(%s)'%service)
            self.services[service]['group'] = MultiSettingControl(Tag('visible','skin.hasSetting(%s)'%service))
            self.services[service]['label'] = CategoryLabelControl(Tag('label',service.title()))
            self.services[service]['group'].addControl(self.services[service]['label'])
            self.services[service]['status'] = ButtonControl(Tag('label','Status'))
            self.services[service]['status'].onClick = lambda status : status.setValue(self.onStatusClick(self.getCurrentService(status),status.getValue()))
            self.services[service]['group'].addControl(self.services[service]['status'])
            self.services[service]['autostart'] = RadioButtonControl(Tag('label','Autostart'))
            self.services[service]['autostart'].onClick = lambda autostart : autostart.setValue(self.onAutostartClick(self.getCurrentService(autostart),autostart.getValue()))
            self.services[service]['group'].addControl(self.services[service]['autostart'])
            self.services[service]['daemon'] = ButtonControl(Tag('label','Daemon'),Tag('visible','skin.hasSetting(advancedmode)'))
            self.services[service]['daemon'].onClick = lambda daemon : daemon.setValue(self.onDaemonClick(self.getCurrentService(daemon),daemon.getValue()))
            self.services[service]['group'].addControl(self.services[service]['daemon'])            
            self.services[service]['delete'] = ButtonControl(Tag('label','Delete service'),Tag('visible','skin.hasSetting(advancedmode)'))
            self.services[service]['delete'].onClick = lambda delete : self.onDeleteClick(self.getCurrentService(delete))
            self.services[service]['group'].addControl(self.services[service]['delete'])
            self.addControl(self.services[service]['group'])
        #custom service
        
        
        self.services['custom'] = {}
        self.services['custom']['group'] = MultiSettingControl(Tag('visible','skin.hasSetting(advancedmode)'))
        self.services['custom']['label'] = CategoryLabelControl(Tag('label','Others' ))
        self.services['custom']['group'].addControl(self.services['custom']['label'])
        self.services['custom']['addcustom'] = ButtonControl(Tag('label','Add a custom service'))
        self.services['custom']['addcustom'].onClick = lambda addxbian : self.onAddCustomClick()
        self.services['custom']['group'].addControl(self.services['custom']['addcustom'])
        self.addControl(self.services['custom']['group'])
        
    def getCurrentService(self,control):
        for service in self.serviceList :            
            if service[:6] != 'custom' :
                for key in self.services[service] :
                    if self.services[service][key] == control :
                        return service
            
    def setCustom(self,service) :
        if service not in self.serviceList :
            self.services[service] = self.services['custom%d'%self.customId]
            self.services[service]['label'].setLabel(service.title())
            self.serviceList.append(service)
            self.customId += 1
            if self.customId > self.nbCustom :
                self.services['custom']['addcustom'].setEnabled(False)
        
    def setVisible(self,service,state):
        for serv in self.serviceList :
            if self.services[serv] == self.services[service] :
                if state :
                    xbmc.executebuiltin('Skin.SetBool(%s)'%serv)
                else :
                    xbmc.executebuiltin('Skin.Reset(%s)'%serv)
                break
        
    def onStatusClick(self,service,value) :
        pass

    def onAutostartClick(self,service,value) :
        pass
        
    def onDaemonClick(self,service,value) :
        pass
    
    def onDeleteClick(self,service) :
        pass
        
    def onAddCustomClick(self) :
        pass
        
    def setValue(self,values):
        for key in values :
            if values[key][0] :
                self.services[key]['status'].setValue(RUNNING)
            else :
                self.services[key]['status'].setValue(STOPPED)
            self.services[key]['autostart'].setValue(values[key][1])
            if values[key][2] :
                self.services[key]['daemon'].setValue(values[key][2])
            else :
                self.services[key]['daemon'].setVisible(False)
        

    def getValue(self) :
        pass
            
       

class servicesManager(Setting) :
    CONTROL = ServicesControl()
    DIALOGHEADER = "Xbian Services Manager"
    ERRORTEXT = "Error"
    OKTEXT = "OK"
    APPLYTEXT = "Apply"

    def onInit(self) :
        self.serviceInstalled = xbianConfig('services','list')
        for service in self.serviceInstalled :
            self.control.setVisible(service,True)
            #xbmc.executebuiltin('Skin.SetBool(%s)'%service)
        self.control.onStatusClick = self.onStatus
        self.control.onAutostartClick = self.onAutoStart
        self.control.onDaemonClick = self.onDaemon
        self.control.onDeleteClick = self.onDelete       
        self.control.onAddCustomClick = self.onAddCustom
        self.publicMethod['refresh'] = self.refresh
    
    def refresh(self) :
        services = xbianConfig('services','list')       
        if services != self.serviceInstalled :
            #check if i have to add service
            for service in services :
                if service not in self.serviceInstalled :
                    self.addService(service)
            #check if i have to delete service
            for service in self.serviceInstalled[:] :
                if service not in services :
                    self.deleteService(service)
                    
    def deleteService(self,service):
        self.control.setVisible(service,False)
        self.serviceInstalled.remove(service)
    
    def addService(self,name) :
        self.control.setCustom(name)                   
        #wait.update(line2='Refreshing Value')
        serviceStatus = xbianConfig('services','status')
        for service in serviceStatus :
            status = service.split(' ')
            if status[0] == name :  
               running = False
               autostart = False
               if status[1] == '3' :
                  autostart = True
               elif status[1] == '4' :
                  running = True
               elif status[1] == '5' :
                  running = True
                  autostart = True
               #get dameon:
               daemon = xbianConfig('services','select',status[0])
               if daemon :
                  daemon = daemon[0]
               else :
                  daemon = False
               self.xbianValue[status[0]] = [running,autostart,daemon]
               self.setControlValue({status[0]:[running,autostart,daemon]})
               break
        self.control.setVisible(name,True)
        self.serviceInstalled.append(status[0])

    
    def onAddCustom(self) :
        canInsert = False
        name = ""
        while not canInsert :
            name = getText('Service Name',name)
            if not name :
                canInsert = True
            else :
                daemon = getText('Daemon (leave empty if none)')               
                if daemon != None :
                    self.APPLYTEXT = 'Do you want to insert %s ?'%name
                    if self.askConfirmation() :
                        progress = dialogWait('Inserting','Please wait while inserting %s...'%name)
                        progress.show() 
                        rc = xbianConfig('services','insert',name,daemon)                                            
                        if rc and rc[0] == '1' :                       
                            self.addService(name)
                            progress.close()
                            self.OKTEXT = 'Service %s added successfully'%name
                            self.notifyOnSuccess()
                        elif rc and rc[0] == '-2':
                            progress.close()
                            self.ERRORTEXT = '%s is not installed, please install it first'%name
                            self.notifyOnError()
                        else :
                            progress.close()
                            self.ERRORTEXT = 'Unknwown error'
                            self.notifyOnError()                            
                    canInsert = True
                    
    
    
    def onDelete(self,service) :
        self.APPLYTEXT = 'Do you want to delete %s?'%service
        if self.askConfirmation() :
            #self.control.setVisible(service,False)
            rc = xbianConfig('services','delete',service)
            if rc and rc[0] != '1' :
                #self.control.setVisible(service,True)
                self.ERRORTEXT = 'Unknwown error'
                self.notifyOnError()
            else :
                self.deleteService(service)
                self.OKTEXT = 'Service %s deleted successfully'%service
                self.notifyOnSuccess()
                
        
    def onDaemon(self,service,value) :
        tmp = getText('%s daemon (separate by space)'%service,value)
        if tmp and tmp != value:
            self.APPLYTEXT = 'Do you want to udpate dameon?'
            if self.askConfirmation() :
                rc = xbianConfig('services','update',service,tmp)
                if rc and rc[0] == '1' :
                    self.OKTEXT = 'Daemon updated successfully'
                    self.notifyOnSuccess()
                    return tmp
                else :
                    self.ERRORTEXT = 'Unknwown error'
                    self.notifyOnError()
        return value
        
        
    def onAutoStart(self,service,value) :
        self.APPLYTEXT = 'Do you want to change autostart?'
        if self.askConfirmation() :        
            if value == 1 :
                value = True
                tmp = 'enable'
            else :
                value = False
                tmp = 'disable'
            rc = xbianConfig('services','autostart',service,tmp)
            if rc and rc[0] == '1' :
                self.OKTEXT = 'Autostart updated successfully'
                self.notifyOnSuccess()
                return value
            else :
                self.ERRORTEXT = 'Unknwown error'
                self.notifyOnError()
        return not value
            
    def onStatus(self,service,value) :
        #ask if we want to change
        if value == RUNNING :
            #ask if stop or restart
            select = dialog.select(service.title(),[STOP,RESTART])
            if select == -1 :
                return value
            else :
                if select == 0 :
                    self.APPLYTEXT = 'Do you want to stop %s ?'%service
                    if self.askConfirmation() :        
                        progress = dialogWait('Stopping','Please wait while stopping %s...'%service)
                        progress.show() 
                        rc = xbianConfig('services','stop',service)
                        progress.close()
                        if rc and rc[0] == '1' :
                            self.OKTEXT = '%s stop successfully'%service
                            self.notifyOnSuccess()
                            return STOPPED
                    self.notifyOnError()
                    return value
                elif select == 1 :
                    self.APPLYTEXT = 'Do you want to restart %s ?'%service
                    if self.askConfirmation() :    
                        progress = dialogWait('Restarting','Please wait while restarting %s...'%service)
                        progress.show() 
                        rc = xbianConfig('services','restart',service)
                        progress.close()
                        if rc and rc[0] == '1' :
                            self.OKTEXT = '%s restart successfully'%service
                            self.notifyOnSuccess()
                            return RUNNING
                    self.notifyOnError()
                    return value
        else :
            self.APPLYTEXT = 'Do you want to start %s ?'%service
            if self.askConfirmation() :        
                progress = dialogWait('Restarting','Please wait while starting %s...'%service)
                progress.show() 
                rc = xbianConfig('services','start',service)
                progress.close()
                if rc and rc[0] == '1' :
                    self.OKTEXT = '%s started successfully'%service
                    self.notifyOnSuccess()
                    return RUNNING
            self.notifyOnError()
            return value
                
    def getXbianValue(self):
        serviceStatus = xbianConfig('services','status')
        services = {}
        for service in serviceStatus :
            status = service.split(' ')
            running = False
            autostart = False
            if status[1] == '3' :
                autostart = True
            elif status[1] == '4' :
                running = True
            elif status[1] == '5' :
                running = True
                autostart = True
            #get dameon:
            daemon = xbianConfig('services','select',status[0])
            if daemon :
                daemon = daemon[0]
            else :
                daemon = False
            services[status[0]] = [running,autostart,daemon]
        return services            
        
    
    
    def setXbianValue(self,value):
        pass


class services(Category) :
    TITLE = 'Services'
    SETTINGS = [servicesManager]



