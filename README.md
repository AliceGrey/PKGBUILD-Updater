# PKGBUILD-Updater
Simple python script to download and hash new package versions and update the PKGBUILD file with the new pkgver and sha256sum. 
I currently use this to maintain the [mullvad](https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=mullvad) package on the AUR. This script requires Python 3 and a valid PKGBUILD file.

# Usage
update.py [old package version] [new package version]
