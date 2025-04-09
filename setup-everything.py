
import os
import pathlib

os.system(f"python -m pip install -U --force-reinstall \"https://github.com/Nuitka/Nuitka/archive/factory.zip\"")
os.system(f"nuitka --module --output-dir={pathlib.Path('./src/lawyer').resolve()} --jobs=10 --lto=yes --python-flag=no_site --python-flag=no_warnings --remove-output --full-compat --prefer-source-code --warn-implicit-exceptions --warn-unusual-code --no-pyi-file --assume-yes-for-downloads {pathlib.Path('./src/lawyer/parsers.py').expanduser().resolve()}")
os.system(f"nuitka --module --output-dir={pathlib.Path('./src/lawyer').resolve()} --jobs=10 --lto=yes --python-flag=no_site --python-flag=no_warnings --remove-output --full-compat --prefer-source-code --warn-implicit-exceptions --warn-unusual-code --no-pyi-file --assume-yes-for-downloads {pathlib.Path('./src/lawyer/exceptions.py').expanduser().resolve()}")
