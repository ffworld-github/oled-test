import machine
import ssd1306

# Set up OLED
i2c = machine.I2C(-1, machine.Pin(4), machine.Pin(5))  # Adjust GPIOs as needed
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)  # Clear the display
oled.text("Hello World!", 0, 0)  # Display text
oled.show()  # Refresh the display
