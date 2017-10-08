import ugfx, wifi, time, gc, ubinascii
import usocket as socket

def log(msg):
  print(msg);

wifi.init()

while not wifi.sta_if.isconnected():
  log('Waiting for wifi connection.')
  time.sleep(1)

addr = ('192.168.0.18', 80)

data = b''
tmpfile = 'screen.png'

ugfx.init()

def draw_image(file):
  ugfx.display_image(0, 0, file)
  ugfx.flush()

def update():
  global data
  try:
    s = socket.socket()
    s.connect(addr)
    s.send(b'GET / HTTP/1.1\r\nHost: bogus\r\n\r\n')
    response = parse_response(s.recv(4096))
    response_body = response[1]
    with open(tmpfile, 'w+b') as f:
      f.write(response_body)
      f.flush()
      draw_image(tmpfile)
  except OSError:
    log('Something wrong with the socket')
  except ValueError:
    log('Request failed (ValueError). Make sure server is reachable.')
  gc.collect()

# Parse a raw HTTP response and return a string tuple with (headers, body)
def parse_response(raw):
  parts = raw.split(b'\r\n\r\n')
  if (len(parts) >= 2):
    return (parts[0], parts[1])
  elif (len(parts) == 1):
    return (parts[0], b'')
  else:
    return (b'', b'')

while True:
  log('Getting updated data')

  # Handle network connection
  if not wifi.sta_if.isconnected():
    log('Lost network connection. Waiting for reconnection.')
    while not wifi.sta_if.isconnected():
      log('Waiting...')
      time.sleep(1)
    log('Connected!')

  # Get fresh data
  update()
  log(data)

  # Wait a bit
  time.sleep(5)

