from virtualControl import xbmcxml,ContainerXml
from tag import Tag

class Content(xbmcxml) :
    FOCUSABLE = False
    ACTION = False
    COMMON = False
    additional_tag = ('label','label2','icon','thumb','onclick','visible','property')

    def toXml(self):
        xml =''
        xml += '<item id="%d">\n'%self.id
        if not self.hasTag('onclick') :
            self.setTag(Tag('onclick','-'))
        xml += xbmcxml.toXml(self)
        xml += '</item>\n'
        return xml



class GroupControl(ContainerXml) :
    FOCUSABLE = False
    ACTION = False
    XBMCDEFAULTCONTAINER = 'group'
    additional_tag =('enable','visible')

    
class GroupListControl(ContainerXml) :
    FOCUSABLE = True
    ACTION = False
    XBMCDEFAULTCONTAINER = 'grouplist'
    additional_tag = ('viewtype','orientation','pagecontrol','scrolltime','focusposition','itemgap')
    

class WrapListControl(ContainerXml) :
    FOCUSABLE = True
    ACTION = False
    XBMCDEFAULTCONTAINER = False
    additional_tag = ('viewtype','orientation','pagecontrol','scrolltime','focusposition','itemgap')

    def onInit(self):
        self.itemLayout= []
        self.focusedLayout= []
        self.content = []

    def addItemLayout(self,control):
        self.itemLayout.append(control)

    def addFocusedLayout(self,control):
        self.focusedLayout.append(control)
        
    def addContent(self,content):
        self.content.append(content)

    def getContent(self):
        return self.content
        
    def toXml(self):
        xml =''
        xml +='<control type="%s" id="%d">\n'%('wraplist',self.getId())
        xml += ContainerXml.toXml(self)

        #add ItemLayout
        xml += '<itemlayout width="%d" height="%d">\n'%(self.getTag('width').getValue()['value'],self.getTag('height').getValue()['value'])
        for control in self.itemLayout :
            xml += control.toXml()
        xml += '</itemlayout>\n'

        #add FocusedLayout
        xml += '<focusedlayout width="%d" height="%d">\n'%(self.getTag('width').getValue()['value'],self.getTag('height').getValue()['value'])
        for control in self.focusedLayout :
            xml += control.toXml()
        xml += '</focusedlayout>\n'

        #add Content
        xml += '<content>\n'
        for control in self.content :
            xml += control.toXml()
        xml += '</content>\n'
        xml += '</control>\n'
        return xml



class MultiSettingControl(ContainerXml) :
    FOCUSABLE = False
    ACTION = False
    XBMCDEFAULTCONTAINER = False
    additional_tag =('visible','enable')

    def toXml(self):
        xml = ""
        if hasattr(self,'save_ctrl'):
            self.addControl(self.save_ctrl)
        for control in self.controls :
            if self.hasTag('visible') :
                control.setTag(self.getTag('visible'),True)
            if self.hasTag('enable') :
                control.setTag(self.getTag('enable'),True)
            #print control
            xml += control.toXml()
        return xml
    
    def setSaveControl(self,ctrl):
        self.save_ctrl = ctrl
        ctrl.click = self.clickSave
   
    def getClickID(self) :
			return self.save_ctrl.getClickID()
        
    def clickSave(self,controlId):
       if controlId == self.save_ctrl.getId() :
           value = []
           for control in self.controls :
              if isinstance(control,ContainerXml) :
                  value.extend(control.getValue())
              else :    
                  value.append(control.getValue())
           self.onClick(self,*value)




