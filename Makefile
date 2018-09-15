DEST = /opt/pixpack

help:
	@printf "make help:          Print help.\n"
	@printf "make install:       Install PixPack on you Linux system.\n"
	@printf "make uninstall:     Uninstall PixPack from your Linux system.\n"
	@printf "make update:        Sync with GitHub and update PixPack\n"

install:
	sudo mkdir $(DEST) $(DEST)/img $(DEST)/json $(DEST)/pixpack $(DEST)/ini
	sudo install --mode=555 img/icon.ico $(DEST)/img/icon.ico
	sudo install --mode=555 ini/* $(DEST)/ini
	sudo install --mode=555 json/translate.json $(DEST)/json/translate.json
	sudo install --mode=555 pixpack/* $(DEST)/pixpack
	sudo install --mode=555 pixpack.py $(DEST)
	sudo install --mode=555 README.md $(DEST)
	sudo install --mode=555 PixPack.desktop /usr/share/applications/PixPack.desktop
	# scripts/install_dependencies.sh not available right now
	echo "Pixpack is successfully installed!"
uninstall:
	rm -rf $(DEST)
	rm -f /usr/share/applications/PixPack.desktop

update:
	sudo make uninstall
	git pull origin
	sudo make install
