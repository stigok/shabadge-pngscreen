import wifi, time, gc
import usocket as socket

def log(msg):
  print(msg);

wifi.init()

while not wifi.sta_if.isconnected():
  log('Waiting for wifi connection.')
  time.sleep(1)

addr = ('192.168.0.18', 80)

data = b''

def update():
  global data
  s = socket.socket()
  s.connect(addr)
  s.send(b'GET / HTTP/1.1\r\nHost: bogus\r\n\r\n')
  res = parse_response(s.recv(1000))
  data = res[1]
  s.close()
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

