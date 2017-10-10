#!/bin/sh
#mpfshell -s script.mpf
echo -e '\nPaste this in REPL to start app:\nimport appglue; appglue.start_app("pngscreen");\n'
mpfshell -c "open ttyUSB0; md /lib/pngscreen; cd /lib/pngscreen; put __init__.py; put pngscreen.py; repl"
