#
#Copyright 2012 Koen Kanters, Raspbian
#This file is part of XBian - XBMC on the Raspberry Pi.
#
#XBian is free software: you can redistribute it and/or modify it under the 
#terms of the GNU General Public License as published by the Free Software 
#Foundation, either version 3 of the License, or (at your option) any later 
#version.
#
#XBian is distributed in the hope that it will be useful, but WITHOUT ANY 
#WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
#FOR A PARTICULAR PURPOSE. See the GNU General Public License for more 
#details.
#
#You should have received a copy of the GNU General Public License along 
#with XBian. If not, see <http://www.gnu.org/licenses/>
#

# Make sure you alloc mininum amount of memmory to the GPU, this will speed up the compilation time
# Use the xbian user.

# Chapters
# 1. Cloning XBMC repo & installing needed packages and creating a bigger swap file
# 2. Compiling taglib (XBMC dependency)
# 3. Compiling libcec 
# 4. Compiling libshairport
# 5. Compiling XBMC
# 6. Compiling PVR Addons

# Make sure you run the resize sd in xbian-config. 8GB+ SD Card recommended.

# 1. Cloning XBMC repo & installing needed packages
   	# Updating all packages & installing the ones who are needed    
	sudo su

  	apt-get update 
   	apt-get upgrade

        apt-get install autotools-dev comerr-dev dpkg-dev libalsaplayer-dev libapt-pkg-dev:armhf libasound2-dev libass-dev:armhf libatk1.0-dev libavahi-client-dev libavahi-common-dev libavcodec-dev libavformat-dev libavutil-dev libbison-dev:armhf libbluray-dev:armhf libboost1.49-dev \
        libbz2-dev:armhf libc-dev-bin libc6-dev:armhf libcaca-dev libcairo2-dev libcdio-dev libclalsadrv-dev libcrypto++-dev libcups2-dev libcurl3-gnutls-dev \
        libdbus-1-dev libdbus-glib-1-dev libdirectfb-dev libdrm-dev libegl1-mesa-dev libelf-dev libenca-dev libept-dev libevent-dev libexpat1-dev libflac-dev:armhf \
        libfontconfig1-dev libfreetype6-dev libfribidi-dev libgconf2-dev libgcrypt11-dev libgdk-pixbuf2.0-dev libgl1-mesa-dev libgles2-mesa-dev \
        libglew-dev:armhf libglewmx-dev:armhf libglib2.0-dev libglu1-mesa-dev libgnome-keyring-dev libgnutls-dev libgpg-error-dev libgtk2.0-dev libhal-dev \
        libhunspell-dev:armhf libice-dev:armhf libicu-dev libidn11-dev libiso9660-dev libjasper-dev libjbig-dev:armhf libjconv-dev libjpeg8-dev:armhf libkrb5-dev \
        libldap2-dev:armhf libltdl-dev:armhf liblzo2-dev libmad0-dev libmicrohttpd-dev libmodplug-dev libmp3lame-dev:armhf libmpeg2-4-dev libmysqlclient-dev \
        libncurses5-dev libnspr4-dev libnss3-dev libogg-dev:armhf libopenal-dev:armhf libp11-kit-dev libpam0g-dev:armhf libpango1.0-dev libpcre++-dev libpcre3-dev \
        libpixman-1-dev libpng12-dev libprotobuf-dev libpthread-stubs0-dev:armhf libpulse-dev:armhf librtmp-dev libsamplerate0-dev:armhf \
        libsdl-image1.2-dev:armhf libsdl1.2-dev libslang2-dev:armhf libsm-dev:armhf libsmbclient-dev:armhf libspeex-dev:armhf \
        libsqlite3-dev libssh-dev libssh2-1-dev libssl-dev libstdc++6-4.6-dev libtagcoll2-dev libtasn1-3-dev libtiff4-dev libtinfo-dev:armhf libtinyxml-dev \
        libts-dev:armhf libudev-dev libv8-dev libva-dev:armhf libvdpau-dev:armhf libvorbis-dev:armhf libvpx-dev:armhf libwebp-dev:armhf libwibble-dev \
        libx11-dev:armhf libx11-xcb-dev libxapian-dev libxau-dev:armhf libxcb-glx0-dev:armhf libxcb-render0-dev:armhf libxcb-shm0-dev:armhf \
        libxcb1-dev:armhf libxcomposite-dev libxcursor-dev:armhf libxdamage-dev libxdmcp-dev:armhf libxext-dev:armhf libxfixes-dev libxft-dev libxi-dev \
        libxinerama-dev:armhf libxml2-dev:armhf libxmu-dev:armhf libxrandr-dev libxrender-dev:armhf libxslt1-dev libxss-dev:armhf libxt-dev:armhf \
        libxtst-dev:armhf libxxf86vm-dev libyajl-dev libzip-dev linux-libc-dev:armhf lzma-dev mesa-common-dev python-dev python2.7-dev x11proto-composite-dev \
        x11proto-core-dev x11proto-damage-dev x11proto-dri2-dev x11proto-fixes-dev x11proto-gl-dev x11proto-input-dev x11proto-kb-dev x11proto-randr-dev \
        x11proto-record-dev x11proto-render-dev x11proto-scrnsaver-dev x11proto-xext-dev x11proto-xf86vidmode-dev x11proto-xinerama-dev xtrans-dev \
        libnfs-dev libplist-dev avahi-daemon zlib1g-dev:armhf swig java-package libafpclient-dev liblockdev1-dev autoconf automake libtool gcc udev openjdk-6-jre \
        cmake g++ libudev-dev build-essential autoconf ccache gawk gperf mesa-utils zip unzip curl 

   	apt-get clean
	
	# Copying libraries
	cp -R /opt/vc/include/* /usr/include

	# Creating symbolic links
	ln -fs /opt/vc/lib/libEGL.so /usr/lib/libEGL.so
	ln -fs /opt/vc/lib/libEGL.so /usr/lib/arm-linux-gnueabihf/libEGL.so
	ln -fs /opt/vc/lib/libEGL.so /usr/lib/arm-linux-gnueabihf/libEGL.so.1
	ln -fs /opt/vc/lib/libEGL_static.a /usr/lib/libEGL_static.a
	ln -fs /opt/vc/lib/libEGL_static.a /usr/lib/arm-linux-gnueabihf/libEGL_static.a
	ln -fs /opt/vc/lib/libGLESv2.so /usr/lib/libGLESv2.so
	ln -fs /opt/vc/lib/libGLESv2.so /usr/lib/arm-linux-gnueabihf/libGLESv2.so
	ln -fs /opt/vc/lib/libGLESv2.so /usr/lib/arm-linux-gnueabihf/libGLESv2.so.2
	ln -fs /opt/vc/lib/libGLESv2_static.a /usr/lib/libGLESv2_static.a
	ln -fs /opt/vc/lib/libGLESv2_static.a /usr/lib/arm-linux-gnueabihf/libGLESv2_static.a
	ln -fs /opt/vc/lib/libbcm_host.so /usr/lib/libbcm_host.so
	ln -fs /opt/vc/lib/libbcm_host.so /usr/lib/arm-linux-gnueabihf/libbcm_host.so
	ln -fs /opt/vc/lib/libvchiq_arm.a /usr/lib/libvchiq_arm.a
	ln -fs /opt/vc/lib/libvchiq_arm.a /usr/lib/arm-linux-gnueabihf/libvchiq_arm.a
	ln -fs /opt/vc/lib/libvchiq_arm.so /usr/lib/libvchiq_arm.so
	ln -fs /opt/vc/lib/libvchiq_arm.so /usr/lib/arm-linux-gnueabihf/libvchiq_arm.so
	ln -fs /opt/vc/lib/libvcos.a /usr/lib/libvcos.a
	ln -fs /opt/vc/lib/libvcos.a /usr/lib/arm-linux-gnueabihf/libvcos.a
	ln -fs /opt/vc/lib/libvcos.so /usr/lib/libvcos.so
	ln -fs /opt/vc/lib/libvcos.so /usr/lib/arm-linux-gnueabihf/libvcos.so

   	# Cloning xbmc
	mkdir /opt
   	cd /opt/
   	git clone --depth 5 -b Frodo git://github.com/xbmc/xbmc.git

	# Make sure kernel environment are unset
	unset TARGET_SUBARCH TARGET_CPU TARGET_FLOAT TARGET_FPU TARGET_FPU_FLAGS TARGET_EXTRA_FLAGS TARGET_COPT TARGET_LOPT TARGET_INCLUDES CFLAGS CXXFLAGS LDFLAGS

# 2. Compiling taglib (XBMC dependency)
	cd /opt/xbmc
	make -C lib/taglib
   	make -C lib/taglib install
	
	
# 3. Compiling libcec
	cd /opt
	git clone --depth 5 https://github.com/Pulse-Eight/libcec.git
	cd libcec
	./bootstrap 
	./configure --prefix=/usr/local --enable-rpi --with-rpi-include-path="/opt/vc/include" --with-rpi-lib-path="/opt/vc/lib/libbcm_host.so"
	make
	make install

# 4. Compiling libshairport
	cd /opt/xbmc
	make -C lib/libshairport
   	make -C lib/libshairport install

# 5. Compiling XBMC
	# Setup *FLAGS
	export TARGET_SUBARCH="armv6zk"
	export TARGET_CPU="arm1176jzf-s"
	export TARGET_FLOAT="hard"
	export TARGET_FPU="vfp"
	export TARGET_FPU_FLAGS="-mfloat-abi=$TARGET_FLOAT -mfpu=$TARGET_FPU"
	export TARGET_EXTRA_FLAGS="-Wno-psabi -Wa,-mno-warn-deprecated"
	export TARGET_COPT="-Wall -pipe -fomit-frame-pointer -O3 -fexcess-precision=fast -ffast-math  -fgnu89-inline"
	export TARGET_LOPT="-s -Wl,--as-needed"
        export TARGET_INCLUDES="-I/usr/include/interface/vcos/pthreads/ -I/usr/include/interface/vmcs_host/linux"
	export CFLAGS="-march=$TARGET_SUBARCH -mcpu=$TARGET_CPU $TARGET_FPU_FLAGS -mabi=aapcs-linux $TARGET_COPT $TARGET_EXTRA_FLAGS $TARGET_INCLUDES"
	export CXXFLAGS="$CFLAGS"
	export LDFLAGS="-march=$TARGET_SUBARCH -mtune=$TARGET_CPU $TARGET_LOPT"

	# Preparing the XBMC code for compilation
	cd /opt/xbmc/

    	# Applying patches
	wget https://raw.github.com/xbianonpi/xbian/xbian-alpha5/Patches/xbmc/TPNno.patch
    	wget https://raw.github.com/xbianonpi/xbian/xbian-alpha5/Patches/xbmc/EGLRes.patch
	wget https://raw.github.com/xbianonpi/xbian/xbian-alpha5/Patches/xbmc/XBianSysSum.patch
        wget https://raw.github.com/xbianonpi/xbian/xbian-alpha5/Patches/xbmc/NetworkCachingRedux.patch
    	wget https://raw.github.com/xbianonpi/xbian/xbian-alpha5/Patches/xbmc/RemoveGUISoundSettings.patch
	wget https://raw.github.com/xbianonpi/xbian/xbian-alpha5/Patches/xbmc/WOL.patch
	wget https://raw.github.com/xbianonpi/xbian/xbian-alpha5/Patches/xbmc/Splash.patch
	patch -p1 < Splash.patch
	patch -p1 < WOL.patch
   	patch -p1 < TPNno.patch
    	patch -p1 < EGLRes.patch
	patch -p1 < XBianSysSum.patch
        patch -p1 < NetworkCachingRedux.patch
	patch -p1 < RemoveGUISoundSettings.patch

	# Replacing the default splash screen
	wget https://raw.github.com/xbianonpi/xbian/xbian-alpha5/usr/local/share/xbmc/media/Splash.png
	mv Splash.png media/

	sed -i 's/USE_BUILDROOT=1/USE_BUILDROOT=0/' tools/rbp/setup-sdk.sh
    	sed -i 's/TOOLCHAIN=\/usr\/local\/bcm-gcc/TOOLCHAIN=\/usr/' tools/rbp/setup-sdk.sh
    	sh tools/rbp/setup-sdk.sh
    	sed -i 's/cd $(SOURCE); $(CONFIGURE)/#cd $(SOURCE); $(CONFIGURE)/' tools/rbp/depends/xbmc/Makefile
	make -C tools/rbp/depends/xbmc/
	
	# Configure  
	./configure --prefix=/usr/local --build=arm-linux-gnueabihf --host=arm-linux-gnueabihf --localstatedir=/var/lib --with-platform=raspberry-pi --disable-gl --enable-gles --disable-x11 --disable-sdl \
              --enable-ccache --enable-optimizations --disable-external-libraries --disable-goom --disable-hal --disable-pulse --disable-vaapi \
              --disable-vdpau --disable-xrandr --enable-airplay --disable-alsa --enable-avahi --enable-libbluray --enable-dvdcss --disable-debug \
              --disable-joystick --disable-mid --enable-nfs --disable-profiling --disable-projectm --enable-rsxs --enable-rtmp --disable-vaapi \
              --disable-vdadecoder --disable-external-ffmpeg --enable-optical-drive --enable-player=omxplayer

  	make # (THIS WILL TAKE LOOOONG! +- 14 hours)
  	make install


# 6. Compiling PVR Addons
	cd /opt/
	git clone --depth 5 git://github.com/opdenkamp/xbmc-pvr-addons.git
	cd xbmc-pvr-addons/
	./bootstrap 
	./configure --prefix=/usr/local --enable-addons-with-dependencies
	make install

	# Compiling the XVDR addon
	cd /opt/
	git clone git://github.com/pipelka/xbmc-addon-xvdr.git
	cd xbmc-addon-xvdr
	sh autogen.sh
	./configure --prefix=/usr/local
	make install

# Many thanks to http://www.raspbian.org/RaspbianXBMC !

