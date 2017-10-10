# pngscreen

Made for the SHA2017 badge

## Usage

1. Prepare an HTTP server which serves single PNG image files from its web root
2. Enter the address of the HTTP server in `pngscreen.py`
3. Upload sources to the badge using `update.sh`
4. Set up WiFi network on the badge and start the app`

## Installation

1. Clone repo
2. Upload sources to the badge using any method you know. I use `mpfshell` and
   `screen`. See below for more information.

## TODO

[x] write raw png/gif to screen
[x] get raw image data from a server

## mpfshell

1. connect with screen `sudo screen /dev/ttyUSB0 115200`
2. reboot device
3. disconnect screen with `Control+A  \` then confirm
4. start clean_repl on device
5. `mpfshell`
6. Then run `open ttyUSB0`

Write `repl` to drop into a python REPL, but having problems exiting.
Using `pkill mpfshell` then starting from step #5 again for now.

### Gotchas

- When connecting with screen, it may seem that the connection is hanging, but press CTRL+D and the device will restart and give you some output
- Pressing CTRL+D while in the Python shell will make the device restart, so use `pkill mpfshell` to exit REPL
- If the shell hangs, make sure the device isn't sleeping.
- Some times after failing to connect, kill running mpfshell processes, wait for device
  restart, enter clean_repl and try again
- Only a single mpfshell running at the time
- At the very least, test the syntax before spending time pushing every single save to the device.
- Run local `python` befre pushing to make sure the script is parseable.
- Running `clean_repl` is kind of the same as writing `import shell` to console while device is about to sleep (e.g. after restarting)
- Exit mpfshell python REPL with CTRL+]
- When the REPL from mpfshell doesn't respond to the exit code, run `sudo pkill mpfshell` to avoid device reboot

- Pretty fast now when I want to quit the REPL, wait for device restart, skip to menu then re-upload a new version of the script
```
# pkill mpfshell
# ./update.sh
  >>> import appglue; appglue.start_app("pngscreen");
```
- If you can't seem to connect. Make sure you have the device plugged in. (Check it anyway)


