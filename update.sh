#!/bin/sh
sudo mpfshell -s script.mpf
echo -e '\nPaste:\nimport appglue; appglue.start_app("foobar");\n'
sudo mpfshell -c "open ttyUSB0; repl"
