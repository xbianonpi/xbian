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


class PackagesControl(MultiSettingControl):
    XBMCDEFAULTCONTAINER = False
   

    def onInit(self) :
        tmp = xbianConfig('packages','list')
        self.packages = {}               
        if tmp and tmp[0] == '-3' :
            rc = xbianConfig('packages','updatedb')
            if rc[0] == '1' :
                tmp = xbianConfig('packages','list')
            else :
                tmp = []
        for cat in tmp :
            t = cat.split(',')
            tmp_cat = {}
            self.packages[t[0]] = {}
            self.packages[t[0]]['available'] = int(t[1])
            self.packages[t[0]]['installed'] = int(t[2])                        
            
        for key in self.packages :                
            self.packages[key]['group'] = MultiSettingControl()
            self.packages[key]['label'] = CategoryLabelControl(Tag('label','%s [COLOR lightblue](%d/%d)[/COLOR]'%(key.title(),self.packages[key]['installed'],self.packages[key]['available'])))
            self.packages[key]['group'].addControl(self.packages[key]['label'])
            self.packages[key]['visible'] = 0            
            self.packages[key]['set'] = []           
            self.packages[key]['list'] = []
            for i in range(self.packages[key]['available']) :
                xbmc.executebuiltin('Skin.Reset(%s%d)'%(key,i))
                package = ButtonControl(Tag('label','temp'),Tag('visible','skin.hasSetting(%s%d)'%(key,i)))
                package.onClick = lambda select : self.selectClick(self.getCurrentCat(select),select.getLabel())
                self.packages[key]['list'].append(package)
                self.packages[key]['group'].addControl(package)
                self.packages[key]['set'].append(False)
                
            
            #add Get more Button
            xbmc.executebuiltin('Skin.SetBool(more%s)'%key)
            self.packages[key]['getmore'] = ButtonControl(Tag('label','Get more...'),Tag('visible','skin.hasSetting(more%s)'%key))
            self.packages[key]['getmore'].onClick = lambda getmore : self.getmoreClick(self.getCurrentCat(getmore))
            self.packages[key]['group'].addControl(self.packages[key]['getmore'])
            self.addControl(self.packages[key]['group'])
            
    def getCurrentCat(self,control) :
        for key in self.packages :
            if self.packages[key]['getmore'] == control :
                return key
            for ctrl in self.packages[key]['list'] :
                if control == ctrl :
                    return key
               
    def addPackage(self,category,package) :                        
        for i,tmp in enumerate(self.packages[category]['set']) :
            if not tmp :                
                break            
        self.packages[category]['set'][i] = True
        self.packages[category]['list'][i].setLabel(package)
        xbmc.executebuiltin('Skin.SetBool(%s%d)'%(category,i))
        self.packages[category]['visible'] += 1
        self.packages[category]['label'].setLabel('%s [COLOR lightblue](%d/%d)[/COLOR]'%(category.title(),self.packages[category]['visible'],self.packages[category]['available']))
        if self.packages[category]['visible'] == self.packages[category]['available'] :
            #hide get More button
            xbmc.executebuiltin('Skin.Reset(more%s)'%category)
    
    def removePackage(self,category,package)  :
        for i,pack in enumerate(self.packages[category]['list']) :
            if package == pack.getLabel() :
                break        
        self.packages[category]['set'][i] = False
        self.packages[category]['visible'] -= 1  
        self.packages[category]['label'].setLabel('%s [COLOR lightblue](%d/%d)[/COLOR]'%(category.title(),self.packages[category]['visible'],self.packages[category]['available']))      
        xbmc.executebuiltin('Skin.Reset(%s%d)'%(category,i))
        if self.packages[category]['visible'] < self.packages[category]['available'] :
            #hide get More button
            xbmc.executebuiltin('Skin.SetBool(more%s)'%category)
    
    
    def selectClick(self,package,value):
        pass
    
    def getmoreClick(self,package) :
        pass  
                    

class packagesManager(Setting) :
    CONTROL = PackagesControl()
    DIALOGHEADER = "XBian Package Manager"
    ERRORTEXT = "Error"
    OKTEXT = "OK"
    APPLYTEXT = "Apply"
    
    INSTALLED = 'Installed'
    NOTINSTALLED = 'Not installed'

    def onInit(self) :   
        pass    
        self.control.getmoreClick = self.onGetMore
        self.control.selectClick = self.onSelect        
        
    def showInfo(self,package) :
        progress = dialogWait('Loading','Please wait while loading the information for %s'%package)
        progress.show() 
        rc = xbianConfig('packages','info',package)
        progress.close() 
        if rc :         
            PackageInfo(package,rc[0].partition(' ')[2],rc[1].partition(' ')[2],rc[2].partition(' ')[2],rc[3].partition(' ')[2],rc[4].partition(' ')[2],rc[5].partition(' ')[2],rc[6].partition(' ')[2])
    def onSelect(self,cat,package) :
        choice = ['Informations','Remove Package']
        select = dialog.select('Select',choice)
        if select == 0 :
            #display info dialog
            self.showInfo(package)
        elif select == 1 :
            #remove package
            self.APPLYTEXT = 'Do you want to remove the %s package?'%package
            if self.askConfirmation(True) :
                progressDlg = dialogWait('Removing','Please wait while uninstalling %s ...'%package)
                progressDlg.show()         
                rc = xbianConfig('packages','removetest',package)
                if rc and rc[0] == '3' :
                   rc = xbianConfig('packages','updatedb')
                   if rc and rc[0] == '1' :
                      rc = xbianConfig('packages','removetest',package)
                if rc and rc[0] == '1' :                                                                
                   rc = xbianConfig('packages','remove',package)
                if rc and rc[0] == '1' :
                    #remove package
                    waitRemove = True
                    progress = 1
                    status = 1                    
                    while waitRemove : 
                            if progress != 0 :
                                progress = int(xbianConfig('packages','progress')[0])                                                        
                            if status != 0 :    
                                status = int(xbianConfig('packages','status',package)[0])                            
                            if progress != 1 and status != 1 :
                                waitRemove = False
                            else :
                                time.sleep(5)
                        #refresh service list                    
                    progressDlg.close()
                    self.control.removePackage(cat,package)
                    self.globalMethod['Services']['refresh']()
                    self.OKTEXT = 'Package %s successfully removed'%package
                    self.notifyOnSuccess()
                    
                else :
                    if rc and rc[0] == '2' :
                         #normally never pass here                     
                         self.ERRORTEXT = 'Package %s is not installed'%package                    
                    elif rc and rc[0] == '3' :                     
                         self.ERRORTEXT = 'Package %s is an essential package and cannot be removed'%package                     
                    else :                      
                         #normally never pass here
                         self.ERRORTEXT = 'Unknown error while removing %s'%package
                    progressDlg.close()
                    self.notifyOnError()
                     
            
    def onGetMore(self,cat) :
        progress = dialogWait('Loading','Please wait while loading packages for %s'%cat)
        progress.show() 
        tmp = xbianConfig('packages','list',cat)
        if tmp and tmp[0] == '-3' :
            rc = xbianConfig('packages','updatedb')
            if rc[0] == '1' :
                tmp = xbianConfig('packages','list')
            else :
                tmp = []
        progress.close()
        if tmp[0]!= '-2' and tmp[0]!= '-3' :
           package = []
           for packag in tmp :
             packageTmp = packag.split(',')
             if packageTmp[1] == '0' :
                package.append(packageTmp[0])
           select =dialog.select('Select Package',package)
           if select != -1 :
                choice = ['Informations','Install Package']
                sel = dialog.select('Select',choice)
                if sel == 0 :
                    #display info dialog
                    self.showInfo(package[select])
                elif sel == 1 :
                    self.APPLYTEXT = 'Do you want to install the package: %s?'%package[select]
                    if self.askConfirmation(True) :                
                        progressDlg = dialogWait('Installing','Please wait while installing %s ...'%package[select])
                        progressDlg.show() 
                        rc = xbianConfig('packages','installtest',package[select])
                        if rc and rc[0] in ('3','4') :
                            rc = xbianConfig('packages','updatedb')
                            if rc and rc[0] == '1' :
                                rc = xbianConfig('packages','installtest',package[select])
                        if rc and rc[0] == '1' :                                                                
                             rc = xbianConfig('packages','install',package[select])
                        if rc and rc[0] == '1' :                        
                            waitInstall = True
                            progress = 1
                            status = 0                        
                            while waitInstall : 
                                if progress != 0 :
                                    progress = int(xbianConfig('packages','progress')[0])                            
                                if status != 1 :    
                                    status = int(xbianConfig('packages','status',package[select])[0])
                                
                                if progress !=1 and status != 0 :
                                    waitInstall = False
                                else :
                                    time.sleep(5)


                            progressDlg.close()                                                
                            time.sleep(0.5)
                            self.control.addPackage(cat,package[select])
                            self.globalMethod['Services']['refresh']()                                                  
                            self.OKTEXT = 'Package %s successfully installed'%package[select]
                            self.notifyOnSuccess()                        
                        else :
                            if rc and rc[0] == '2' :
                                self.ERRORTEXT = 'Package %s is already installed'%package[select]                          
                            elif rc and rc[0] == '3' :                          
                                self.ERRORTEXT = 'Package %s not found in apt-repository'%package[select]                       
                            elif rc and rc[0] == '4' :                          
                                self.ERRORTEXT = 'Package not found in apt repository'                             
                            elif rc and rc[0] == '5' :                          
                                self.ERRORTEXT = 'A newer version of this package is already installed'                         
                            elif rc and rc[0] == '6' :                          
                                self.ERRORTEXT = 'There is a size mismatch for the remote package'                          
                            elif rc and rc[0] == '7' :                          
                                self.ERRORTEXT = 'The package itself got an internal error'
                            else :                          
                                #normally never pass here
                                self.ERRORTEXT = 'Unknown error while installing %s'%package
                            progressDlg.close()
                            self.notifyOnError()                                        
                        
            
    def getXbianValue(self):
        packages = self.control.packages
        for key in packages :
            if packages[key]['installed'] > 0 :
                tmp = xbianConfig('packages','list',key)
                if tmp[0]!= '-2' and tmp[0]!= '-3' :
                    for packag in tmp :
                        packageTmp = packag.split(',')
                        if packageTmp[1] == '1' :
                            self.control.addPackage(key,packageTmp[0])                  

class packages(Category) :
    TITLE = 'Packages'
    SETTINGS = [packagesManager]



