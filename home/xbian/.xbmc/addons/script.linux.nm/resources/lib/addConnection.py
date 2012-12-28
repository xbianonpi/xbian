import xbmc
import xbmcaddon
import xbmcgui
import qfpynm
import time
import sys

#enable localization
getLS   = sys.modules[ "__main__" ].__language__
__cwd__ = sys.modules[ "__main__" ].__cwd__
__addon__      = xbmcaddon.Addon()


class GUI(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)
        self.doModal()


    def onInit(self):
        self.disable_ipv6 = __addon__.getSetting( "disable_ipv6" )
        if self.disable_ipv6 == "true":
            self.disable_ipv6 = True
        else:
            self.disable_ipv6 = False
            
        self.defineControls()

        self.msg = ""
        self.status_label.setLabel(self.msg)
        
        self.showDialog()
                
        self.status_label.setLabel(self.msg)
        self.remove_auto_button.setEnabled(False)
        #self.disconnect_button.setEnabled(False)
       
        
    def defineControls(self):
        #actions
        self.action_cancel_dialog = (9, 10)
        #control ids
        self.control_heading_label_id         = 2
        self.control_list_label_id            = 3
        self.control_list_id                  = 10
        self.control_add_hidden_button_id     = 11
        self.control_refresh_button_id        = 13
        self.control_remove_auto_button_id    = 14
        self.control_install_button_id        = 18
        self.control_cancel_button_id         = 19
        self.control_status_label_id          = 100
        
        #controls
        self.heading_label      = self.getControl(self.control_heading_label_id)
        self.list_label         = self.getControl(self.control_list_label_id)
        self.list               = self.getControl(self.control_list_id)
        self.control_add_hidden_button = self.getControl(self.control_add_hidden_button_id)
        self.remove_auto_button = self.getControl(self.control_remove_auto_button_id)
        self.refresh_button  = self.getControl(self.control_refresh_button_id)
        self.install_button     = self.getControl(self.control_install_button_id)
        self.cancel_button      = self.getControl(self.control_cancel_button_id)
        self.status_label       = self.getControl(self.control_status_label_id)

    def showDialog(self):
        self.updateList()
        self.setFocus(self.list )

    def closeDialog(self):        
        import gui
        mainUI = gui.GUI("script_linux_nm-main.xml", __cwd__, "default",msg=self.msg, first=False)
        self.close()
        del mainUI

    def onClick(self, controlId):
        self.msg = ""
        self.status_label.setLabel(self.msg)
        
        #Add connection from list
        if controlId == self.control_list_id:
            position = self.list.getSelectedPosition()
            #Get SSID!!
            item = self.list.getSelectedItem()

            ssid =  item.getLabel2()  
            encryption = item.getProperty('encryption')
            connection_created = self.add_wireless(ssid,encryption)       
            if connection_created == True:
                self.closeDialog()
       
        #Refresh
        elif controlId == self.control_refresh_button_id:
            self.msg = getLS(30115) #Refreshing
            self.status_label.setLabel(self.msg)
            self.updateList()
            self.msg = ""
            self.status_label.setLabel(self.msg)
        
        #Add hidden button
        elif controlId == self.control_add_hidden_button_id:
            connection_created = self.add_hidden()
            if connection_created == True:
                self.closeDialog()

        #cancel dialog
        elif controlId == self.control_cancel_button_id:
            self.closeDialog()

    
    def onAction(self, action):
        if action in self.action_cancel_dialog:
            self.closeDialog()

    def onFocus(self, controlId):
        msg = ""
        if hasattr(self, 'status_label'):
            self.status_label.setLabel(msg)

    def add_hidden(self):
        ssid = ''
        kb = xbmc.Keyboard("", getLS(30123), False)
        kb.doModal()
        if (kb.isConfirmed()):
            ssid=kb.getText()
        if ssid == '':
            self.msg = getLS(30108)  
            self.status_label.setLabel(self.msg)
            return False       
        
        encryption = ''
        kb = xbmc.Keyboard("", getLS(30124), False)
        kb.doModal()
        if (kb.isConfirmed()):
            encryption=kb.getText()
            if encryption != '':
                encryption = encryption.upper()
                
        if encryption == '' or not any(encryption in s for s in ['NONE', 'WEP', 'WPA']):
            self.msg = getLS(30125)  
            self.status_label.setLabel(self.msg)
            return  False
        return self.add_wireless(ssid, encryption)
        
    def add_wireless(self, ssid, encryption):
        finished = False
        connection_created = False
        con_path = ''
        while not finished  :
            finished, connection_created, con_path = self.add_wireless_sub(ssid, encryption, connection_created, con_path)
        return connection_created
    
    def add_wireless_sub(self, ssid, encryption, connection_created, con_path):
        #Prompt for key
        key = ""
        if not encryption == 'NONE':
            kb = xbmc.Keyboard("", getLS(30104), False)
            kb.doModal()
            if (kb.isConfirmed()):
                key=kb.getText()
                errors = qfpynm.validate_wifi_input(key,encryption)
           
            if key == "" or errors != '':
                self.msg = getLS(30109)  
                self.status_label.setLabel(self.msg)
                return True, connection_created, con_path
        if encryption == 'WEP':
            wep_alg = 'shared'
        else:
            wep_alg = ''
        if connection_created == False:
            con_path = qfpynm.add_wifi(ssid,key,encryption,wep_alg,self.disable_ipv6 )
        else:
            aUUID = qfpynm.get_con_uuid_by_path(con_path)
            qfpynm.update_wifi(aUUID, key, encryption)
            qfpynm.activate_connection(aUUID)
            
        for i in range(1, 150):
            state,stateTXT = qfpynm.get_device_state(qfpynm.get_wifi_device())
            self.msg = stateTXT
            self.status_label.setLabel(self.msg)
            # Do not exit directly just to be sure.
            # If trying with a bad key when wifi is disconnected do not give state 60 but 30....
            # better never to disconnect wifi and only deactivate c
            if (i > 10 and state == 60) or (i > 10 and state == 30)  or (state == 100 and i >2):
                break
            time.sleep(1)
            self.msg = ''
            self.status_label.setLabel(self.msg)
            time.sleep(1)
        if state == 100:
            self.msg = getLS(30120) #"Connected!"
            self.status_label.setLabel(self.msg)
            return True, True, con_path
        if (state == 60  or state == 30) and encryption != "NONE":
            self.msg = getLS(30121) #"Not Autorized!"
            self.status_label.setLabel(self.msg)
            return False, True, con_path
        
        self.msg = getLS(30122) #"Connection failed"
        self.status_label.setLabel(self.msg)      
        return True, True, con_path


    def updateList(self):
        print "updating list"
        self.list.reset()
        
        #qfpynm.scan_wireless()
        wlessL = qfpynm.get_wireless_networks()        
        for net_dict in wlessL:
            if net_dict['connected'] == True:
                sts = '>'
            elif net_dict['automatic'] == '1':
                sts = 'a'
            else:
                sts = ''
                
            item = xbmcgui.ListItem (label=sts, label2 = net_dict['essid'])
            item.setProperty('channel',str(net_dict['channel']))
            item.setProperty('encryption',str(net_dict['encrypt']))
            item.setProperty('signal',str(net_dict['signal']))
            self.list.addItem(item)
    
    
            
