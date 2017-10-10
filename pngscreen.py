import badge, ugfx, wifi, time, easydraw
import urequests as requests

#
# Requests a PNG from HTTP server and display on screen
#

# Settings
imageurl = 'http://192.168.0.18/screen.png'
splashurl = 'http://192.168.0.18/stigok.png'
tmpfile = '/media/screen.png'
interval_sec = 5

# Functions
def log(msg):
  print(msg);

def clear_ghosting():
  ugfx.clear(ugfx.BLACK)
  ugfx.flush()
  badge.eink_busy_wait()
  ugfx.clear(ugfx.WHITE)
  ugfx.flush()
  badge.eink_busy_wait()

def wait_for_network():
  # Handle network connection
  if not wifi.sta_if.isconnected():
    while not wifi.sta_if.isconnected():
      easydraw.msg('Waiting for network')
      log('Waiting for network')
      time.sleep(1)
    log('Connected!')

def download_screen_data(url):
  log('Requesting image data: '+ url)
  req = requests.get(url)
  with open(tmpfile, 'w+b') as fd:
    fd.write(req.content)
  
def update_screen():
  # Imagebox centers the image on the screen
  box = ugfx.Imagebox(0, 0, ugfx.width(), ugfx.height(), tmpfile)
  ugfx.flush()
  box.destroy()

def try_draw_url(url):
  try:
    download_screen_data(imageurl)
    update_screen()
  except BaseException as e:
    log('Failed to download and draw image: '+ str(e))

# Prepare device
ugfx.set_lut(ugfx.GREYSCALE)
ugfx.init()
wifi.init()
badge.init()
ugfx.input_init()

ugfx.input_attach(ugfx.BTN_B, lambda pressed: btn_b(pressed))
def btn_b(pressed):
  if pressed:
    import appglue
    appglue.start_app('clean_repl')

# Show splash
clear_ghosting()
try_draw_url(splashurl)
easydraw.msg('Made with <3 in my room in Oslo', title = 'pngscreen')
time.sleep(1)

# Main loop
while True:
  wait_for_network()
  try_draw_url(imageurl)
  time.sleep(interval_sec)

