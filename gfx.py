import ugfx

def init():
  ugfx.init()

# badge.eink_display_raw might be a better idea
# image can be filename or ugfx.Image() object
def draw_image(image):
  ugfx.display_image(0, 0, image)
  ugfx.flush()

