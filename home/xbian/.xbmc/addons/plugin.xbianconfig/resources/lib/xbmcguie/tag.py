#CLASS TAG
#contains all xbmc windows xml tag
#use tag = Tag('posx',0,[{'key' : 'condition', 'value' : 'xbmc boolean condition'}])

class Tag :
    def __init__(self,key,value=None,properties=None):
        self.key = key
        self.tags = []
        if value != None :
            self.addValue(value,properties)
        else:
            self.tags.append({'value':None,'properties':[]})

    def addValue(self,value,properties=None):
        tag = {}
        tag['value'] = value
        tag['properties'] = self._toDictProperties(properties)
        self.tags.append(tag)
        return len(self.tags) -1

    def setValue(self,value,properties=None,id=0):
        self.tags[id]['value'] = value
        self.tags[id]['properties'].extend(self._toDictProperties(properties))

    def getValue(self,id=0):
        return self.tags[id]

    def getKey(self) :
        return self.key

    def toXml(self) :
        xml = ""
        for tag in self.tags :
            #create the property string
            properties = ""
            for property in tag['properties'] :
                properties += ' %s="%s"'%(property['key'],property['value'])
            if tag['value'] != None :
                xml += "<%s%s>%s</%s>\n"%(self.key,properties,tag['value'],self.key)
        return xml


    def _toDictProperties(self,properties) :
        ArrayProperties =[]
        if properties != None :
            if type(properties) == type(ArrayProperties) : #TODO : do a better way after
                ArrayProperties  = properties
            else :
                ArrayProperties.append(properties)
        return ArrayProperties

