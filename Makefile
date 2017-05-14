DEST = /opt/pixpack

help:
	@printf "make help:					Print help."
	@printf "make install: 			Install PixPack on you Linux system."
	@printf "make uninstall:		Uninstall PixPack from your Linux system."

install:
	sudo mkdir $(DEST) $(DEST)/img $(DEST)/json $(DEST)/pixpack
	sudo install --mode=555 img/icon.ico $(DEST)/img/icon.ico
	sudo install --mode=555 json/translate.json $(DEST)/json/translate.json
	sudo install --mode=555 pixpack/* $(DEST)/pixpack
	sudo install --mode=555 pixpack.py $(DEST)
	sudo install --mode=555 README.md $(DEST)
	sudo install --mode=555 PixPack.desktop /usr/share/applications/PixPack.desktop
	# scripts/instal_dependencies.sh

uninstall:
	rm -rf $(DEST)
	rm -f /usr/share/applications/PixPack.desktop
