# Thing on sha2017 badge

[ ] write raw png/gif to screen
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

- If the shell hangs, make sure the device isn't sleeping.
- Some times after failing to connect, kill running mpfshell processes, wait for device
  restart, enter clean_repl and try again
- Only a single mpfshell running at the time
- At the very least, test the syntax before spending time pushing every single save to the device.
- Run local `python` befre pushing to make sure the script is parseable.

- Pretty fast now when I want to quit the REPL, wait for device restart, skip to menu then re-upload a new version of the script
```
# pkill mpfshell
# ./update.sh
  >>> import appglue; appglue.start_app("foobar");
```
- If you can't seem to connect. Make sure you have the device plugged in. (Check it anyway)


