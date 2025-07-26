from machine import Pin, I2C
import ssd1306
import time
i2c = I2C(0, sda=Pin(0), scl=Pin(1))

# Set up the OLED display (128x64 pixels) on the I2C bus
# SSD1306_I2C is a subclass of FrameBuffer. FrameBuffer provides support for graphics primitives.
# http://docs.micropython.org/en/latest/pyboard/library/framebuf.html
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear the display by filling it with white and then showing the update
oled.fill(1)
oled.show()
time.sleep(1)  # Wait for 1 second

# Clear the display again by filling it with black
oled.fill(0)
oled.show()
time.sleep(1)  # Wait for another second

# Display text on the OLED screen
oled.text('Hello,', 0, 0)  # Display "Hello," at position (0, 0)
oled.text('different hello', 0, 16)  # Display "sunfounder.com" at position (0, 16)

# The following line sends what to show to the display
oled.show()