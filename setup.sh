#!/bin/bash
python -m pip install -U --force-reinstall "https://github.com/Nuitka/Nuitka/archive/factory.zip"
nuitka --module backups/parsers.py --output-dir=src/lawyer --jobs=10 --lto=yes --python-flag=no_site --python-flag=no_warnings --remove-output --full-compat --prefer-source-code --warn-implicit-exceptions --warn-unusual-code --no-pyi-file --assume-yes-for-downloads
nuitka --module backups/exceptions.py --output-dir=src/lawyer --jobs=10 --lto=yes --python-flag=no_site --python-flag=no_warnings --remove-output --full-compat --prefer-source-code --warn-implicit-exceptions --warn-unusual-code --no-pyi-file --assume-yes-for-downloads
pip install .
rm -rf build src/lawyer.egg-info