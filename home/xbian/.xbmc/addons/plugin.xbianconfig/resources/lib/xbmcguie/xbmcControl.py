import xbmc

from virtualControl import ControlXml
from tag import Tag
from xbmcContainer import *

class scrollbarControl(ControlXml):
    FOCUSABLE = True
    XBMCDEFAULTCONTROL = 'scrollbar'
    additional_tag = ('texturesliderbackground','texturesliderbar','texturesliderbarfocus','textureslidernib','textureslidernibfocus','orientation','showonepage')
        
class ButtonControl(ControlXml) :
    FOCUSABLE = True
    ACTION = True
    XBMCDEFAULTCONTROL = 'button'
    additional_tag = ('texturefocus','texturenofocus','label','label2','font','textcolor','focusedcolor','disabledcolor','shadowcolor','angle','align','aligny','textoffsetx','textoffsety','textwidth')
    
    def getValue(self):
        if hasattr(self,'Controlinstance') :
            return self.Controlinstance.getLabel2()
    
    def setValue(self,value):
        if hasattr(self,'Controlinstance') :
            self.Controlinstance.setLabel(label=self.Controlinstance.getLabel(),label2=str(value))
    
    def setLabel(self,value):
        if hasattr(self,'Controlinstance') :
            self.Controlinstance.setLabel(label=str(value),label2=self.Controlinstance.getLabel2())
    def getLabel(self):
        if hasattr(self,'Controlinstance') :
            return self.Controlinstance.getLabel()
    
class ApplyButtonControl(ControlXml) :
    FOCUSABLE = True
    ACTION = True
    XBMCDEFAULTCONTROL = None
    #additional_tag = ('texturefocus','texturenofocus','label','label2','font','textcolor','focusedcolor','disabledcolor','shadowcolor','angle','align','aligny','textoffsetx','textoffsety','textwidth')
    additional_tag = ('label','label2')
    def onInit(self) :
        self.controls = {}
        if not self.hasTag('onup') :
            #create a fake button to allow scroll up
            #print 'create onup'
            self.controls['FakebtnUp'] = ButtonControl(Tag('description','hidden button to scroll up the list'),Tag('visible','false'),defaultSKin=False)
            ControlXml.setTag(self,Tag('onup',self.controls['FakebtnUp'].getId()))
            #print self.tags

        if not self.hasTag('ondown')  :
            #create a fake button to allow scroll down
            self.controls['FakebtnDown'] = ButtonControl(Tag('description','hidden button to scroll down the list'),Tag('visible','false'),defaultSKin=False)
            ControlXml.setTag(self,Tag('ondown',self.controls['FakebtnDown'].getId()))

        #print self.tags
        #create the groupControl
        self.controls['groupControl'] = GroupControl(*self.getArrayTags())
        self.controls['ApplyButtonControl'] = ButtonControl(*self.getArrayTags(),defaultSKin=False)
        self.controls['ApplyButtonControl'].setTag(Tag('align','center'))
        self.controls['ApplyButtonControl'].setTag(Tag('width','150'))
        self.controls['ApplyButtonControl'].setTag(Tag('height','%d'%(self.getTag('height').getValue()['value']-10)))
        self.controls['ApplyButtonControl'].setTag(Tag('posy','5'))
        self.controls['ApplyButtonControl'].setTag(Tag('posx','%d'%(self.getTag('width').getValue()['value'] - 160)))
        self.controls['groupControl'].addControl(self.controls['ApplyButtonControl'])
        #self.setTag(Tag('texturefocus',None))
        #self.setTag(Tag('texturenofocus',None))
    
    def getId(self) :
        return self.controls['ApplyButtonControl'].getId()

    def setTag(self,tag,append=False) :
        if tag.getKey() in self.common_tag :
            self.controls['groupControl'].setTag(tag)
        if tag.getKey() in self.focusable_tag :
            self.controls['ApplyButtonControl'].setTag(tag)

    def toXml(self) :
        xml = ''
        xml += self.controls['FakebtnUp'].toXml()
        xml += self.controls['groupControl'].toXml()
        xml += self.controls['FakebtnDown'].toXml()
        return xml
    


class CategoryLabelControl(ControlXml) :
    FOCUSABLE = False
    ACTION = False
    XBMCDEFAULTCONTROL = 'label'
    additional_tag = ('align','aligny','scroll','label','info','number','angle','haspath','font','textcolor','shadowcolor','wrapmultiline','scrollspeed','scrollsuffix')

    def onInit(self):
        self.setTag(Tag('height','%d'%(self.getTag('height').getValue()['value']+5)))
        self.setTag(Tag('font','font13_title'))
        self.setTag(Tag('textcolor','blue'))
        self.setTag(Tag('shadowcolor','black'))
        self.setTag(Tag('align','left'))
        self.setTag(Tag('aligny','center'))             
    
    def setLabel(self,value):
        if hasattr(self,'Controlinstance') :
            self.Controlinstance.setLabel(str(value))
    
                        
class SpinControl(ControlXml) :
    FOCUSABLE = True
    ACTION = False
    XBMCDEFAULTCONTROL = 'spincontrol'
    additional_tag = ('textureup','textureupfocus','texturedown','texturedownfocus','font','textcolor','disabledcolor','shadowcolor','subtype','align','aligny','textoffsetx','textoffsety')

class LabelControl(ControlXml) :
    FOCUSABLE = False
    ACTION = False
    XBMCDEFAULTCONTROL = 'label'
    additional_tag = ('align','aligny','scroll','label','info','number','angle','haspath','font','textcolor','shadowcolor','wrapmultiline','scrollspeed','scrollsuffix')


class RadioButtonControl(ControlXml) :
    FOCUSABLE = True
    ACTION = True
    XBMCDEFAULTCONTROL = 'radiobutton'
    additional_tag = ('texturefocus','texturenofocus','textureradioon','textureradiooff','label','font','textcolor','focusedcolor','disabledcolor','shadowcolor','align','aligny','textoffsetx','textoffsety','selected','radioposx','radioposy','radiowidth','radioheight')

    def getValue(self):
        if hasattr(self,'Controlinstance') :
            return self.Controlinstance.isSelected()
    
    def setValue(self,value):
        if hasattr(self,'Controlinstance') :
            self.Controlinstance.setSelected(value)


class SpinControlex(ControlXml) :
    FOCUSABLE = True
    ACTION = False
    XBMCDEFAULTCONTROL = None
    additional_tag = SpinControl.additional_tag + ButtonControl.additional_tag

    def onInit(self):
        self.controls = {}
        
        if not self.hasTag('onup') :
            #create a fake button to allow scroll up
            #print 'create onup'
            self.controls['FakebtnUp'] = ButtonControl(Tag('description','hidden button to scroll up the list'),Tag('visible','false'),defaultSKin=False)
            ControlXml.setTag(self,Tag('onup',self.controls['FakebtnUp'].getId()))
            #print self.tags

        if not self.hasTag('ondown')  :
            #create a fake button to allow scroll down
            self.controls['FakebtnDown'] = ButtonControl(Tag('description','hidden button to scroll down the list'),Tag('visible','false'),defaultSKin=False)
            ControlXml.setTag(self,Tag('ondown',self.controls['FakebtnDown'].getId()))

        #print self.tags
        #create the groupControl
        self.controls['groupControl'] = GroupControl(*self.getArrayTags())


        #create the spin control
        self.controls['SpinControlButton'] = SpinControl(*self.getArrayTags())
        self.controls['SpinControlButton'].setTag(Tag('posx',self.controls['groupControl'].getTag('width').getValue()['value'] - 80))
        self.controls['SpinControlButton'].setTag(Tag('posy',8))
        self.controls['SpinControlButton'].setTag(Tag('height',None))
        self.controls['SpinControlButton'].setTag(Tag('width',None))
        self.controls['SpinControlButton'].setTag(Tag('subtype','page'))
        self.controls['SpinControlButton'].setTag(Tag('textoffsetx',5000))
        if not self.hasTag('onleft')  :
            #hardcode on left value - don't find how to do
            self.controls['SpinControlButton'].setTag(Tag('onleft',9000))
        if not self.hasTag('onright')  :
            #hardcode on right value - don't find how to do
            #maybe do a group list, but have to change all the control
            self.controls['SpinControlButton'].setTag(Tag('onright',9000))
            
            
        self.controls['groupControl'].addControl(self.controls['SpinControlButton'])

        #create 3 fake button control for checking focus+enabled and have label
        #MainControl visible conditon
        
        self.controls['FakebtnLabelFocus'] = ButtonControl(*self.getArrayTags())
        self.controls['FakebtnLabelFocus'].setTag(Tag('enable',"false"))
        self.controls['FakebtnLabelFocus'].setTag(Tag('posx',0))
        self.controls['FakebtnLabelFocus'].setTag(Tag('posy',0))
        self.controls['FakebtnLabelFocus'].setTag(Tag('disabledcolor',self.getTag('focusedcolor').getValue()['value']))
        self.controls['FakebtnLabelFocus'].setTag(Tag('visible','Control.HasFocus(%d) + Control.IsEnabled(%d) + control.IsVisible(%d)'%(self.controls['SpinControlButton'].getId(),self.controls['SpinControlButton'].getId(),self.controls['SpinControlButton'].getId())))
        self.controls['FakebtnLabelFocus'].setTag(Tag('texturenofocus',self.controls['FakebtnLabelFocus'].getTag('texturefocus').getValue()['value']))
        self.controls['groupControl'].addControl(self.controls['FakebtnLabelFocus'])

        self.controls['FakebtnLabelNoFocus'] = ButtonControl(*self.getArrayTags())
        self.controls['FakebtnLabelNoFocus'].setTag(Tag('enable',"false"))
        self.controls['FakebtnLabelNoFocus'].setTag(Tag('disabledcolor',self.getTag('textcolor').getValue()['value']))
        self.controls['FakebtnLabelNoFocus'].setTag(Tag('posx',0))
        self.controls['FakebtnLabelNoFocus'].setTag(Tag('posy',0))
        
        self.controls['FakebtnLabelNoFocus'].setTag(Tag('visible','!Control.HasFocus(%d) + Control.IsEnabled(%d) + control.IsVisible(%d)'%(self.controls['SpinControlButton'].getId(),self.controls['SpinControlButton'].getId(),self.controls['SpinControlButton'].getId())))
        self.controls['FakebtnLabelNoFocus'].setTag(Tag('texturefocus',self.controls['FakebtnLabelFocus'].getTag('texturenofocus').getValue()['value']))
        self.controls['groupControl'].addControl(self.controls['FakebtnLabelNoFocus'])

        self.controls['FakebtnLabelDisabled'] = ButtonControl(*self.getArrayTags())
        self.controls['FakebtnLabelDisabled'].setTag(Tag('enable',"false"))
        self.controls['FakebtnLabelDisabled'].setTag(Tag('posx',0))
        self.controls['FakebtnLabelDisabled'].setTag(Tag('posy',0))
        self.controls['FakebtnLabelDisabled'].setTag(Tag('visible','!Control.IsEnabled(%d) + control.IsVisible(%d)'%(self.controls['SpinControlButton'].getId(),self.controls['SpinControlButton'].getId())))
        self.controls['groupControl'].addControl(self.controls['FakebtnLabelDisabled'])

        #create the wraplist Control (contain different choice)
        self.controls['wraplistControl'] = WrapListControl(*self.getArrayTags())
        self.controls['wraplistControl'].setTag(Tag('width',225))
        self.controls['wraplistControl'].setTag(Tag('height',40))
        self.controls['wraplistControl'].setTag(Tag('enable','false'))
        self.controls['wraplistControl'].setTag(Tag('posy',0))
        self.controls['wraplistControl'].setTag(Tag('posx',450))
        self.controls['wraplistControl'].setTag(Tag('pagecontrol',self.controls['SpinControlButton'].getId()))
        self.controls['wraplistControl'].setTag(Tag('scrolltime',0))

        #create 3 label (focus,nofocus,disable) to handle different text color
        self.controls['labelbtndisable']  = LabelControl(*self.getArrayTags())
        self.controls['labelbtndisable'].setTag(Tag('posx',215))
        self.controls['labelbtndisable'].setTag(Tag('posy',0))
        self.controls['labelbtndisable'].setTag(Tag('posy',0))
        self.controls['labelbtndisable'].setTag(Tag('width',225))
        self.controls['labelbtndisable'].setTag(Tag('align','right'))
        self.controls['labelbtndisable'].setTag(Tag('aligny','center'))
        self.controls['labelbtndisable'].setTag(Tag('textcolor',self.getTag('disabledcolor').getValue()['value']))
        self.controls['labelbtndisable'].setTag(Tag('label','$INFO[ListItem.Label]'))
        self.controls['labelbtndisable'].setTag(Tag('visible','!Control.IsEnabled(%d)'%self.controls['SpinControlButton'].getId()))
        self.controls['wraplistControl'].addFocusedLayout(self.controls['labelbtndisable'])

        self.controls['labelbtnfocus']  = LabelControl(*self.getArrayTags())
        self.controls['labelbtnfocus'].setTag(Tag('posx',215))
        self.controls['labelbtnfocus'].setTag(Tag('posy',0))
        self.controls['labelbtnfocus'].setTag(Tag('posy',0))
        self.controls['labelbtnfocus'].setTag(Tag('width',225))
        self.controls['labelbtnfocus'].setTag(Tag('align','right'))
        self.controls['labelbtnfocus'].setTag(Tag('aligny','center'))
        self.controls['labelbtnfocus'].setTag(Tag('textcolor',self.getTag('focusedcolor').getValue()['value']))
        self.controls['labelbtnfocus'].setTag(Tag('label','$INFO[ListItem.Label]'))
        self.controls['labelbtnfocus'].setTag(Tag('visible','Control.HasFocus(%d) + Control.IsEnabled(%d)'%(self.controls['SpinControlButton'].getId(),self.controls['SpinControlButton'].getId())))
        self.controls['wraplistControl'].addFocusedLayout(self.controls['labelbtnfocus'])

        self.controls['labelbtnnofocus']  = LabelControl(*self.getArrayTags())
        self.controls['labelbtnnofocus'].setTag(Tag('posx',215))
        self.controls['labelbtnnofocus'].setTag(Tag('posy',0))
        self.controls['labelbtnnofocus'].setTag(Tag('posy',0))
        self.controls['labelbtnnofocus'].setTag(Tag('width',225))
        self.controls['labelbtnnofocus'].setTag(Tag('align','right'))
        self.controls['labelbtnnofocus'].setTag(Tag('aligny','center'))
        self.controls['labelbtnnofocus'].setTag(Tag('textcolor',self.getTag('textcolor').getValue()['value']))
        self.controls['labelbtnnofocus'].setTag(Tag('label','$INFO[ListItem.Label]'))
        self.controls['labelbtnnofocus'].setTag(Tag('visible','!Control.HasFocus(%d) + Control.IsEnabled(%d)'%(self.controls['SpinControlButton'].getId(),self.controls['SpinControlButton'].getId())))
        self.controls['wraplistControl'].addFocusedLayout(self.controls['labelbtnnofocus'])


        self.controls['groupControl'].addControl(self.controls['wraplistControl'])

    def getId(self) :
        return self.controls['SpinControlButton'].getId()

    def setTag(self,tag,append=False) :
        if tag.getKey() in self.common_tag :
            self.controls['groupControl'].setTag(tag)
        if tag.getKey() in self.focusable_tag :
            self.controls['SpinControlButton'].setTag(tag)

    def addContent(self,content):		
        self.controls['wraplistControl'].addContent(content)

    def getWrapListId(self):
        return self.controls['wraplistControl'].getId()

    def getOnUpId(self):
        return self.controls['FakebtnDown'].getId()
        
    def getOnDownId(self):
        return self.controls['FakebtnUp'].getId()
    
    def getValue(self):
        return xbmc.getInfoLabel('Container(%d).ListItem.Label'%self.controls['wraplistControl'].getId())
    
    def setValue(self,value):
        nbItem = xbmc.getInfoLabel('Container(%d).NumItems'%self.controls['wraplistControl'].getId())        
        find = False
        for i in range(int(nbItem)):
            if value == xbmc.getInfoLabel('Container(%d).ListItem(%d).Label'%(self.controls['wraplistControl'].getId(),i)) :
                find = True
                break
        if find :
            xbmc.executebuiltin('Control.Move(%d,%d)'%(self.controls['wraplistControl'].getId(),i))
        
    
 
    def toXml(self):
        xml = ''
        if self.controls.has_key('FakebtnUp') :
            xml += self.controls['FakebtnUp'].toXml()
        #create the group container
        xml += self.controls['groupControl'].toXml()

        if self.controls.has_key('FakebtnDown') :
            xml += self.controls['FakebtnDown'].toXml()
        return xml
