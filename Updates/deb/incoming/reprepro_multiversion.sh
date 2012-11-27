dpkg-scanpackages -m . /dev/null > Packages
rm Packages.new
rm Packages.gz
START=0;
PACKAGE="";
while read LINE; do
	if [[ $LINE =~ 'Package:' ]]; then
		START=1;
	fi
	if [[ ${#LINE} -eq 0 ]]; then
		NAME=$(echo -e $PACKAGE | sed -n 's/\(Package: \)\(.*$\)/\2/p')	
		VERSION=$(echo -e $PACKAGE | sed -n 's/\(Version: \)\(.*$\)/\2/p')	
		FIRSTL=$(echo $NAME | head -c 1);
		COMMAND="echo -e \"$PACKAGE\" | sed -e 's/Filename: .\//Filename: pool\/main\/$FIRSTL\/$NAME\//g' | sed -e 's/$NAME$VERSION\.deb/$NAME\_$VERSION\_armhf\.deb/g' | sed -e 's/$NAME-$VERSION\.deb/$NAME\_$VERSION\_armhf\.deb/g' >> Packages.new"
		eval $COMMAND
		PACKAGE="";
		START=0;
	fi
	if [ $START -eq 1 ]; then
		PACKAGE+=$LINE"\n";
	fi
done < Packages;
mv Packages.new Packages
cp Packages Packages.bak
gzip -9 Packages
cp Packages.bak Packages
rm Packages.bak

rm Release
cat <<\EOF > Release
Origin: XBian
Label: XBian repository
Codename: wheezy
Date: Wed, 21 Nov 2012 11:11:49 UTC
Architectures: armhf
Components: main
Description: Packages especially made for XBian
MD5Sum:
 [md5Packages]
 [md5Packages.gz]
 [md5Release]
SHA1:
 [sha1Packages]
 [sha1Packages.gz]
 [sha1Release]
SHA256:
 [sha256Packages]
 [sha256Packages.gz]
 [sha256Release]
EOF

SUM=$(md5sum Packages | awk '{print $1}');
SIZE=$(ls -Al Packages | awk '{print $5}';);
eval "sed -i 's/\[md5Packages\]/$SUM $SIZE main\/binary-armhf\/Packages/g' Release";

SUM=$(md5sum Packages.gz | awk '{print $1}');
SIZE=$(ls -Al Packages.gz  | awk '{print $5}';);
eval "sed -i 's/\[md5Packages.gz\]/$SUM $SIZE main\/binary-armhf\/Packages.gz/g' Release";

SUM=$(md5sum ../dists/wheezy/main/binary-armhf/Release | awk '{print $1}');
SIZE=$(ls -Al ../dists/wheezy/main/binary-armhf/Release  | awk '{print $5}';);
eval "sed -i 's/\[md5Release\]/$SUM $SIZE main\/binary-armhf\/Release/g' Release";

SUM=$(sha1sum Packages | awk '{print $1}');
SIZE=$(ls -Al Packages | awk '{print $5}';);
eval "sed -i 's/\[sha1Packages\]/$SUM $SIZE main\/binary-armhf\/Packages/g' Release";

SUM=$(sha1sum Packages.gz | awk '{print $1}');
SIZE=$(ls -Al Packages.gz  | awk '{print $5}';);
eval "sed -i 's/\[sha1Packages.gz\]/$SUM $SIZE main\/binary-armhf\/Packages.gz/g' Release";

SUM=$(sha1sum ../dists/wheezy/main/binary-armhf/Release | awk '{print $1}');
SIZE=$(ls -Al ../dists/wheezy/main/binary-armhf/Release  | awk '{print $5}';);
eval "sed -i 's/\[sha1Release\]/$SUM $SIZE main\/binary-armhf\/Release/g' Release";

SUM=$(sha256sum Packages | awk '{print $1}');
SIZE=$(ls -Al Packages | awk '{print $5}';);
eval "sed -i 's/\[sha256Packages\]/$SUM $SIZE main\/binary-armhf\/Packages/g' Release";

SUM=$(sha256sum Packages.gz | awk '{print $1}');
SIZE=$(ls -Al Packages.gz  | awk '{print $5}';);
eval "sed -i 's/\[sha256Packages.gz\]/$SUM $SIZE main\/binary-armhf\/Packages.gz/g' Release";

SUM=$(sha256sum ../dists/wheezy/main/binary-armhf/Release | awk '{print $1}');
SIZE=$(ls -Al ../dists/wheezy/main/binary-armhf/Release  | awk '{print $5}';);
eval "sed -i 's/\[sha256Release\]/$SUM $SIZE main\/binary-armhf\/Release/g' Release";
chmod 777 Release

gpg --clearsign < Release > InRelease
gpg --output Release.gpg -ba Release

mv InRelease ../dists/wheezy/
mv Release ../dists/wheezy/
mv Release.gpg ../dists/wheezy/
mv Packages ../dists/wheezy/main/binary-armhf/
mv Packages.gz ../dists/wheezy/main/binary-armhf/

rm Packages.bak