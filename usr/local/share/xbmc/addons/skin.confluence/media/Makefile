TARGET=Textures.xbt
XBMCTEX=/opt/xbmcfrodo/tools/TexturePacker/TexturePacker

IMAGES := $(shell find . -name "*jpg")
IMAGES += $(shell find . -name "*png")
IMAGES += $(shell find . -name "*gif")

all: $(TARGET)

.PHONY: force

$(TARGET): $(XBMCTEX) $(IMAGES)
ifeq (,1)
	$(XBMCTEX) -use_none -input . -output $(TARGET)
else
	$(XBMCTEX) -input . -output $(TARGET)

endif
$(XBMCTEX): force
	$(MAKE) -C /opt/xbmcfrodo/tools/TexturePacker

clean:
	rm -f $(TARGET)
distclean: clean

