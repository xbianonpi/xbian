# Start with a fresh Raspbian image, make sure you alloc mininum amount of memmory to the GPU

# Chapters
# 1. Cloning XBMC repo & installing needed packages and creating a bigger swap file
# 2. Compiling libtag (XBMC dependency)
# 3. Compiling libcec 
# 4. Compiling libshairport
# 5. Compiling XBMC


# 1. Cloning XBMC repo & installing needed packages
   	# Updating all packages & installing the ones who are needed and creating a bigger swap file           
  	sudo apt-get update
   	sudo apt-get upgrade

	sudo apt-get install build-essential autoconf ccache gawk gperf mesa-utils zip unzip

   	sudo apt-get install autotools-dev comerr-dev dpkg-dev libalsaplayer-dev libapt-pkg-dev:armhf libasound2-dev:armhf libass-dev:armhf libatk1.0-dev \
   	libavahi-client-dev libavahi-common-dev libavcodec-dev libavformat-dev libavutil-dev libbison-dev:armhf libbluray-dev:armhf libboost1.49-dev \
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
   	libnfs-dev libplist-dev avahi-daemon zlib1g-dev:armhf swig java-package libafpclient-dev liblockdev1-dev autoconf automake libtool gcc udev openjdk-6-jre

   	sudo apt-get clean
	
   	# Copying libraries
   	sudo cp -R /opt/vc/include/* /usr/include
   	sudo cp /opt/vc/include/interface/vcos/pthreads/* /usr/include/interface/vcos

   	# Creating symbolic links
   	sudo ln -fs /opt/vc/lib/libEGL.so /usr/lib/libEGL.so
   	sudo ln -fs /opt/vc/lib/libEGL.so /usr/lib/arm-linux-gnueabihf/libEGL.so
   	sudo ln -fs /opt/vc/lib/libEGL.so /usr/lib/arm-linux-gnueabihf/libEGL.so.1
   	sudo ln -fs /opt/vc/lib/libEGL_static.a /usr/lib/libEGL_static.a
   	sudo ln -fs /opt/vc/lib/libEGL_static.a /usr/lib/arm-linux-gnueabihf/libEGL_static.a
   	sudo ln -fs /opt/vc/lib/libGLESv2.so /usr/lib/libGLESv2.so
   	sudo ln -fs /opt/vc/lib/libGLESv2.so /usr/lib/arm-linux-gnueabihf/libGLESv2.so
   	sudo ln -fs /opt/vc/lib/libGLESv2.so /usr/lib/arm-linux-gnueabihf/libGLESv2.so.2
   	sudo ln -fs /opt/vc/lib/libGLESv2_static.a /usr/lib/libGLESv2_static.a
   	sudo ln -fs /opt/vc/lib/libGLESv2_static.a /usr/lib/arm-linux-gnueabihf/libGLESv2_static.a
   	sudo ln -fs /opt/vc/lib/libbcm_host.so /usr/lib/libbcm_host.so
   	sudo ln -fs /opt/vc/lib/libbcm_host.so /usr/lib/arm-linux-gnueabihf/libbcm_host.so
   	sudo ln -fs /opt/vc/lib/libvchiq_arm.a /usr/lib/libvchiq_arm.a
   	sudo ln -fs /opt/vc/lib/libvchiq_arm.a /usr/lib/arm-linux-gnueabihf/libvchiq_arm.a
   	sudo ln -fs /opt/vc/lib/libvchiq_arm.so /usr/lib/libvchiq_arm.so
   	sudo ln -fs /opt/vc/lib/libvchiq_arm.so /usr/lib/arm-linux-gnueabihf/libvchiq_arm.so
   	sudo ln -fs /opt/vc/lib/libvcos.a /usr/lib/libvcos.a
   	sudo ln -fs /opt/vc/lib/libvcos.a /usr/lib/arm-linux-gnueabihf/libvcos.a
   	sudo ln -fs /opt/vc/lib/libvcos.so /usr/lib/libvcos.so
   	sudo ln -fs /opt/vc/lib/libvcos.so /usr/lib/arm-linux-gnueabihf/libvcos.so

   	# Cloning xbmc
   	sudo mkdir /opt/
   	cd /opt/
   	git clone git://github.com/xbmc/xbmc.git
	
   	# Creating a bigger swap file
   	sudo dd if=/dev/zero of=/moreswap bs=1024 count=512000
	

# 2. Compiling libtag (XBMC dependency)
	cd /opt/
	git clone git://github.com/taglib/taglib.git
	cd /opt/taglib/
	cmake -DCMAKE_INSTALsL_PREFIX=/usr -DCMAKE_RELEASE_TYPE=Release
	make
	sudo make install
	
	
# 3. Compiling libcec
	cd /opt/
	git clone git://github.com/Pulse-Eight/libcec.git
	cd /opt/libcec/
	autoreconf -vif
	./configure
	make
	sudo make install
	

# 4. Compiling libshairport
	cd /opt/
	wget http://mirrors.xbmc.org/build-deps/darwin-libs/libshairport-1.2.0.20310_lib.tar.gz
	tar xzf libshairport-1.2.0.20310_lib.tar.gz
	cd /opt/libshairport-1.2.0.20310_lib/
	
	# Applying some patches
	patch -Np0 -i /opt/xbmc/tools/rbp/depends/libshairport/001_add_ao.patch
	patch -Np0 -i /opt/xbmc/tools/rbp/depends/libshairport/002_fix_install_header.patch
	patch -Np0 -i /opt/xbmc/tools/rbp/depends/libshairport/003_fix_deadlock.patch
	patch -Np0 -i /opt/xbmc/tools/rbp/depends/libshairport/004_fix_bad_access.patch
	patch -Np0 -i /opt/xbmc/tools/rbp/depends/libshairport/005_fix_shutdown.patch
	patch -Np0 -i /opt/xbmc/tools/rbp/depends/libshairport/006_no_printf.patch
	patch -Np0 -i /opt/xbmc/tools/rbp/depends/libshairport/007_fix_syslog_defines.patch  
	patch -Np0 -i /opt/xbmc/tools/rbp/depends/libshairport/008-add-missing-libs.patch  
	patch -Np0 -i /opt/xbmc/tools/rbp/depends/libshairport/009_fix_ipv6.patch
	patch -Np0 -i /opt/xbmc/tools/rbp/depends/libshairport/010_handle_metadata.patch
	wget https://raw.github.com/Memphiz/xbmc/203145a9b6049035dd3e9adbe1e10d8eeae629c9/lib/libshairport/011_fix_ipv4_fallback.patch
	patch -Np0 -i 011_fix_ipv4_fallback.patch
 
	# Compiling
	autreconf -vif  
	./configure --prefix=/usr --sysconfdir=/etc --disable-static --enable-shared
	make
	sudo make install


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
	export CFLAGS="-march=$TARGET_SUBARCH -mcpu=$TARGET_CPU $TARGET_FPU_FLAGS -mabi=aapcs-linux $TARGET_COPT $TARGET_EXTRA_FLAGS"
	export CXXFLAGS="$CFLAGS"
	export LDFLAGS="-march=$TARGET_SUBARCH -mtune=$TARGET_CPU $TARGET_LOPT"

	# Swapon swap and cd to the directory
	cd /opt/xbmc/
	swapon /moreswap
	
	nano configure.in # set use_texturepacker_native=yes to use_texturepacker_native=no @ line 668
	
	# Preparing the XBMC code for compilation
	sed -i 's/USE_BUILDROOT=1/USE_BUILDROOT=0/' tools/rbp/setup-sdk.sh
    	sed -i 's/TOOLCHAIN=\/usr\/local\/bcm-gcc/TOOLCHAIN=\/usr/' tools/rbp/setup-sdk.sh
    	sudo sh tools/rbp/setup-sdk.sh
    	sed -i 's/cd $(SOURCE); $(CONFIGURE)/#cd $(SOURCE); $(CONFIGURE)/' tools/rbp/depends/xbmc/Makefile
	make -C tools/rbp/depends/xbmc/
	
	# Configure  
	./configure --prefix=/usr --localstatedir=/var/lib --with-platform=raspberry-pi --disable-gl --enable-gles --disable-x11 --disable-sdl \
              --enable-ccache --disable-optimizations --disable-external-libraries --disable-goom --disable-hal --disable-pulse --disable-vaapi \
              --disable-vdpau --disable-xrandr --enable-airplay --disable-alsa --enable-avahi --disable-libbluray --enable-dvdcss --disable-debug \
              --disable-joystick --disable-mid --enable-nfs --disable-profiling --disable-projectm --enable-rsxs --enable-rtmp --disable-vaapi \
              --disable-vdadecoder --disable-external-ffmpeg --enable-optical-drive --enable-player=omxplayer

  	make # (THIS WILL TAKE LOOOONG! +- 14 hours)
  	sudo make install

# Many thanks to http://www.raspbian.org/RaspbianXBMC !
