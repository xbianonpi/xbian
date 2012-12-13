import sys
import xbmc
import xbmcaddon
import xbmcgui
import qfpynm
import time

#enable localization
getLS   = sys.modules[ "__main__" ].__language__
__cwd__ = sys.modules[ "__main__" ].__cwd__


#Longer term
#TODO Build a service that monitor state and display a notification about changes
#TODO Display network detail window
#TODO Create a new con name if name=ssid is taken
#TODO the > only indicates active connection. would be nice to show connectivity status as well


class GUI(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)
        self.msg = kwargs['msg']
        self.first = kwargs['first']
        self.doModal()


    def onInit(self):
        self.defineControls()

        self.status_label.setLabel(self.msg)
        
        self.showDialog()
        
        if self.first == True:
            nm_OK, err = self.check_nm() 
            if nm_OK == True:
                devlist = qfpynm.list_wifi_devices()        
                if len(devlist) > 1:
                    self.msg = getLS(30127)
                elif len(devlist) == 0:
                    self.msg = getLS(30128)
            else:
                self.msg = getLS(err)
        
        self.status_label.setLabel(self.msg)
        
        #self.disconnect_button.setEnabled(False)
        #self.delete_button.setEnabled(False)
        
    def check_nm(self):
        try:
            import dbus
        except:
            # dbus not available
            err = 30130
            return False, err
        
        try:
            bus = dbus.SystemBus()
        except:
            # could not connect to dbus
            err =  30131
            return False, err
            
        try:
            nm_proxy = bus.get_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager")
            nm_iface = dbus.Interface(nm_proxy, "org.freedesktop.NetworkManager")
        except:
            # could not connect to network-manager
            err = 30132    
            return False, err
        
        return True, ''
        
    def defineControls(self):
        #actions
        self.action_cancel_dialog = (9, 10)
        #control ids
        self.control_heading_label_id         = 2
        self.control_list_label_id            = 3
        self.control_list_id                  = 10
        self.control_delete_button_id           = 11
        self.control_disconnect_button_id     = 13
        self.control_add_connection_button_id = 14
        self.control_status_button_id           = 15       
        self.control_install_button_id        = 18
        self.control_cancel_button_id         = 19
        self.control_status_label_id          = 100
        
        #controls
        self.heading_label      = self.getControl(self.control_heading_label_id)
        self.list_label         = self.getControl(self.control_list_label_id)
        self.list               = self.getControl(self.control_list_id)
        self.delete_button        = self.getControl(self.control_delete_button_id)
        self.control_add_connection_button = self.getControl(self.control_add_connection_button_id)
        self.status_button        = self.getControl(self.control_status_button_id)
        self.disconnect_button  = self.getControl(self.control_disconnect_button_id)
        self.install_button     = self.getControl(self.control_install_button_id)
        self.cancel_button      = self.getControl(self.control_cancel_button_id)
        self.status_label       = self.getControl(self.control_status_label_id)

    def showDialog(self):
        self.updateList()
        #state,stateTXT = qfpynm.get_nm_state()
        #msg = stateTXT
        #self.status_label.setLabel(msg)

    def closeDialog(self):
        self.close()

    def onClick(self, controlId):
        self.msg = ""
        self.status_label.setLabel(self.msg)
        
                    
        #Activate connection from list
        if controlId == self.control_list_id:
            #position = self.list.getSelectedPosition()
            
            #Get UUID
            item = self.list.getSelectedItem()

            uuid =  item.getProperty('uuid') 
            encryption = item.getProperty('encryption') 
            #print uuid
            
            self.activate_connection(uuid)
            for i in range(1, 100):
                state,stateTXT = qfpynm.get_device_state(qfpynm.get_wifi_device())
                msg = stateTXT
                self.status_label.setLabel(msg)
                if (state == 100 and i >2):
                    break
                if (i > 2 and state == 60):
                    if encryption not in ['WPA','WEP']:
                        print ("Strange encryption:" + encryption)
                        break
                    #Prompt for key
                    key = ""
                    kb = xbmc.Keyboard("", getLS(30104), False)
                    kb.doModal()
                    if (kb.isConfirmed()):
                        key=kb.getText()
                        errors = qfpynm.validate_wifi_input(key,encryption)
                   
                    if key == "" or errors != '':
                        self.msg = getLS(30109)  
                        self.status_label.setLabel(self.msg)
                        break

                    qfpynm.update_wifi(uuid, key, encryption)
                    qfpynm.activate_connection(uuid)     
                    continue                 
                time.sleep(1)
                msg = ''
                self.status_label.setLabel(msg)
                time.sleep(1)
            if state == 100:
                msg = getLS(30120) #"Connected!"
 
            elif state == 60:    
                msg = getLS(30121) #"Not Autorized!"
            else:    
                msg = getLS(30122) #"Connection failed"
            self.updateList()
            self.status_label.setLabel(msg)
            

        #Add connection button
        elif controlId == self.control_add_connection_button_id:
            import addConnection
            addConnectionUI = addConnection.GUI("script_linux_nm-add.xml", __cwd__, "default")
            self.close()
            del addConnectionUI
            
        #disconnect button
        elif controlId == self.control_disconnect_button_id:
            self.disconnect()
                        
            for i in range(1, 20):
                state,stateTXT = qfpynm.get_device_state(qfpynm.get_wifi_device())
                self.msg = stateTXT
                self.status_label.setLabel(self.msg)
           
                if (state == 30):
                    break
                time.sleep(1)
            self.updateList()
            
            
        #Delete button
        elif controlId == self.control_delete_button_id:
            item = self.list.getSelectedItem()

            uuid =  item.getProperty('uuid') 
            
            self.delete_connection(uuid)
            
            msg = getLS(30115) #Refreshing
            self.status_label.setLabel(msg)
        
            time.sleep(2)
            self.updateList()
            
            msg = getLS(30126) #Done
            self.status_label.setLabel(msg)           
            self.setFocus(self.control_add_connection_button)
        
        #Status button
        elif controlId == self.control_status_button_id:         
            state,stateTXT = qfpynm.get_nm_state()
            msg = stateTXT
            self.status_label.setLabel(msg)
               
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

    def disconnect(self):
        qfpynm.deactive_wifi()
        
    def activate_connection(self,uuid):
        qfpynm.activate_connection(uuid)

    def delete_connection(self,uuid):
        qfpynm.delete_connection(uuid)
            
    def updateList(self):
        print "updating list"
        self.list.reset()

        connection_list = qfpynm.get_connections()
    
        for  connection_dict in connection_list:
            if connection_dict['active']== True:
                sts = ">"
            elif connection_dict['auto'] == 1:
                sts = "a"
            else:
                sts = ""
        
            item = xbmcgui.ListItem (label=sts, label2 = connection_dict['id'])
            item.setProperty('ssid',connection_dict['ssid'])
            item.setProperty('uuid',connection_dict['uuid'])
            item.setProperty('encryption',connection_dict['encryption'])
            self.list.addItem(item)
    
    
            
