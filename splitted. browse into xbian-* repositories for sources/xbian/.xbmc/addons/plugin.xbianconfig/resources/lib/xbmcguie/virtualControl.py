import itertools
id_generator = itertools.count(36000)

from tag import Tag

#defaultSkin Control Settings
#check later if possible to get from skin
defaultSkinSetting = {'height':40,'width':750,'textcolor':'grey2','focusedcolor':'white','disabledcolor':'grey3','pulseonselect':'false','texturefocus':'MenuItemFO.png','texturenofocus':'MenuItemNF.png','font':'font13','texturesliderbackground' : 'ScrollBarV.png','texturesliderbar' : 'ScrollBarV_bar.png','texturesliderbarfocus' : 'ScrollBarV_bar_focus.png','textureslidernib':'ScrollBarNib.png','textureslidernibfocus': 'ScrollBarNib.png'}

#virtual class xbmcxml
#Base class for Control and Container
class xbmcxml :

   FOCUSABLE = False
   ACTION = False
   COMMON = True
   

   common_tag = ('description','posx','posy','height','width','visible','animation','camera','colordiffuse')
   focusable_tag = ('onup','ondown','onleft','onright','hitrect','enable','pulseonselect')
   action_tag = ('onclick','onfocus','onunfocus')
   additional_tag = ()

   def __init__(self, *args,**kwargs):
       self.id = next(id_generator)
       self.hasfocus = False

       #set available tags for this control
       self.availabletags=()

       if self.COMMON :
           self.availabletags += self.common_tag
       if self.FOCUSABLE :
           self.availabletags += self.focusable_tag
       if self.ACTION :
           self.availabletags += self.action_tag

       self.availabletags += self.additional_tag

       self.tags = {}
       #set default tag if necessary
       if not kwargs.has_key('defaultSKin') or kwargs['defaultSKin'] == True :
           for default in defaultSkinSetting :
               if default in self.availabletags  :
                   xbmcxml.setTag(self,Tag(default,defaultSkinSetting[default]))

       #set tag from args
       for tag in args :
           if tag.getKey() in self.availabletags :
               xbmcxml.setTag(self,tag)
       self.onInit()

   def onInit(self) :
       pass

   def getId(self) :
       return self.id
   
   def onFocus(self,ctrl) :
        pass
    
   def onUnFocus(self,ctrl) :
        pass
    
   def onClick(self,ctrl):
        pass
       
   def getClickID(self) :
        return self.id
   
   def getConfig(self):
       pass
    
   def onLoad(self,ctrl):
       pass

   def setValue(self,value):
        pass
           
   def getArrayTags(self) :
       arrayTags= []
       for key in self.tags :
           arrayTags.append(self.tags[key])
       return   arrayTags

   def setTag(self,tag,append=False) :
       if tag.getKey() in self.availabletags :
           if self.tags.has_key(tag.getKey()) and append:
               if self.tags[tag.getKey()].getValue()['value'] != tag.getValue()['value'] or self.tags[tag.getKey()].getValue()['properties'] !=tag.getValue()['properties'] :
                    self.tags[tag.getKey()].addValue(tag.getValue()['value'],tag.getValue()['properties'])
           else :
               self.tags[tag.getKey()] = tag

   def getTag(self,key):
       if self.tags.has_key(key) :
           return self.tags[key]

   def hasTag(self,key) :
       return self.tags.has_key(key)
       
   
   def toXml(self):
       xml = ''
       for tag in self.tags :
           xml += self.tags[tag].toXml()
       return xml


#virtualClass ControlXml
#base class for all Xbmc Control or custom Control
class ControlXml(xbmcxml):
    XBMCDEFAULTCONTROL = False
      
    def setWindowInstance(self,instance):
        self.Windowsinstance = instance
        self.Controlinstance = self.Windowsinstance.getControl(self.getId())
        
    def click(self,controlId):
       if controlId == self.getId() :
           self.onClick(self) 
    
    def focus(self,controlId) :
       if controlId == self.getId() :
           if not self.hasfocus :
                self.hasfocus = True
                self.onFocus(self)
       elif self.hasfocus :
            self.hasfocus = False
            self.onUnFocus(self)
    
    def getValue(self):
        pass
    
    def setEnabled(self,value):
        self.Controlinstance.setEnabled(value)
    
    def setVisible(self,value):
        self.Controlinstance.setVisible(value)
       
    def toXml(self):
       xml = ''
       if self.XBMCDEFAULTCONTROL :
           #write control header if default xbmc control
           xml +='<control type="%s" id="%d">\n'%(self.XBMCDEFAULTCONTROL,self.getId())

       xml+=xbmcxml.toXml(self)

       if self.XBMCDEFAULTCONTROL :
           #close control header if default xbmc control
           xml +='</control>\n'
       return xml
       

#virtual class ContainerXml
#base class for all xbmc or custom Container
class ContainerXml(xbmcxml):
    XBMCDEFAULTCONTAINER = False
    
    def __init__(self, *args,**kwargs):
        self.controls = []
        self.controlIdList = []
        xbmcxml.__init__(self,*args,**kwargs)
        
    def addControl(self,control):
        self.controls.append(control)
        
    def getControls(self):
        return self.controls
    
    def getIds(self) :
        ids = []
        for control in self.controls :
            if isinstance(control,ContainerXml) :
                ids.extend(control.getIds())
            else :
                ids.append(control.getId())
        return ids
    
    def setWindowInstance(self,instance):
        for control in self.controls :
            control.setWindowInstance(instance)
    
    
    def click(self,controlId):
       if controlId in self.getIds() :
           for control in self.controls :
               control.click(controlId)
               
    def focus(self,controlId):
        if controlId in self.getIds() :
            for control in self.controls :
                control.focus(controlId)
            if not self.hasfocus :
                self.hasfocus = True
                self.onFocus(self)
        elif self.hasfocus :
            for control in self.controls :
                control.focus(controlId)
            self.hasfocus = False
            self.onUnFocus(self)
    
    def getValue(self):
        value = []
        for control in self.controls :            
            if isinstance(control,ContainerXml) :
                value.extend(control.getValue())
            else :
                value.append(control.getValue())
        return value
    
    def setEnabled(self,value):
         for control in self.controls :
            control.setEnabled(value)
   
    def setVisible(self,value):
       for control in self.controls :
            control.setVisible(value)
    
    def toXml(self):
       xml = ''
       if self.XBMCDEFAULTCONTAINER :
           #write control header if default xbmc control
           xml +='<control type="%s" id="%d">\n'%(self.XBMCDEFAULTCONTAINER,self.getId())

       xml+=xbmcxml.toXml(self)
       
       for control in self.controls :
            xml += control.toXml() 

       if self.XBMCDEFAULTCONTAINER :
           #close control header if default xbmc control
           xml +='</control>\n'
       return xml

