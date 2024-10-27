import machine
import utime

# Define pin numbers for flex sensors
FLEX_SENSOR_1_PIN = 26  # Replace 0 with the actual pin number
FLEX_SENSOR_2_PIN = 27 # Replace 1 with the actual pin number
FLEX_SENSOR_3_PIN = 28 # Replace 2 with the actual pin number

# Define pin numbers for LCD
LCD_RS_PIN = 2  # Replace 3 with the actual pin number
LCD_EN_PIN = 3  # Replace 4 with the actual pin number
LCD_D4_PIN = 4  # Replace 5 with the actual pin number
LCD_D5_PIN = 5  # Replace 6 with the actual pin number
LCD_D6_PIN = 6  # Replace 7 with the actual pin number
LCD_D7_PIN = 7  # Replace 8 with the actual pin number

# Define pin numbers for voice module
VOICE_MODULE_PINS = [11,12,14,15,16,17]  # Replace with actual pin numbers

# Initialize flex sensors
flex_sensor_1 = machine.ADC(FLEX_SENSOR_1_PIN)
flex_sensor_2 = machine.ADC(FLEX_SENSOR_2_PIN)
flex_sensor_3 = machine.ADC(FLEX_SENSOR_3_PIN)

# Initialize LCD
lcd_rs = machine.Pin(LCD_RS_PIN, machine.Pin.OUT)
lcd_en = machine.Pin(LCD_EN_PIN, machine.Pin.OUT)
lcd_d4 = machine.Pin(LCD_D4_PIN, machine.Pin.OUT)
lcd_d5 = machine.Pin(LCD_D5_PIN, machine.Pin.OUT)
lcd_d6 = machine.Pin(LCD_D6_PIN, machine.Pin.OUT)
lcd_d7 = machine.Pin(LCD_D7_PIN, machine.Pin.OUT)

# Initialize voice module pins
voice_pins = [machine.Pin(pin, machine.Pin.OUT) for pin in VOICE_MODULE_PINS]

# Define LCD commands
LCD_CLEAR = const(0x01)
LCD_CURSOR_HOME = const(0x02)
LCD_DISPLAY_ON = const(0x0C)
LCD_4BIT_MODE = const(0x28)

def lcd_command(data):
    lcd_rs.off()
    lcd_d7.value(data & 0x08)
    lcd_d6.value(data & 0x04)
    lcd_d5.value(data & 0x02)
    lcd_d4.value(data & 0x01)
    lcd_enable_pulse()

def lcd_enable_pulse():
    lcd_en.off()
    utime.sleep_ms(1)
    lcd_en.on()
    utime.sleep_ms(1)

def lcd_init():
    lcd_command(0x33)
    lcd_command(0x32)
    lcd_command(LCD_4BIT_MODE)
    lcd_command(LCD_DISPLAY_ON)
    lcd_command(LCD_CLEAR)
    lcd_command(LCD_CURSOR_HOME)

def lcd_write(message):
    lcd_command(LCD_CLEAR)
    for char in message:
        lcd_rs.on()
        lcd_d7.value(ord(char) & 0x80)
        lcd_d6.value(ord(char) & 0x40)
        lcd_d5.value(ord(char) & 0x20)
        lcd_d4.value(ord(char) & 0x10)
        lcd_enable_pulse()
        lcd_rs.on()
        lcd_d7.value(ord(char) & 0x08)
        lcd_d6.value(ord(char) & 0x04)
        lcd_d5.value(ord(char) & 0x02)
        lcd_d4.value(ord(char) & 0x01)
        lcd_enable_pulse()

def trigger_voice_module(message):
    # Send message to LCD
    lcd_write(message)
    # Trigger voice module
    for pin in voice_pins:
        pin.on()
    utime.sleep(2)  # Play the sound for 2 seconds
    for pin in voice_pins:
        pin.off()

def send_message_over_serial(message):
    print("I Want To Say That:", message)
    # Implement serial communication here

def main():
    # Initialize LCD
    lcd_init()
    
    while True:
        # Read flex sensor values
        flex1_val = flex_sensor_1.read_u16()
        flex2_val = flex_sensor_2.read_u16()
        flex3_val = flex_sensor_3.read_u16()

        # Check combinations of flex sensor values
        if  flex1_val < 600 and flex2_val > 600 and flex3_val > 600:#1
            message = "I want water"
            trigger_voice_module(message)
            send_message_over_serial(message)
        elif flex1_val > 600 and flex2_val < 600 and flex3_val > 600:#2
            message = "I am hungry"
            trigger_voice_module(message)
            send_message_over_serial(message)
        elif flex1_val > 600 and flex2_val > 600 and flex3_val < 600:#3
            message = "I need help"
            trigger_voice_module(message)
            send_message_over_serial(message)
        elif flex1_val < 600 and flex2_val < 600 and flex3_val > 600:#1,2
            message = "I am in pain"
            trigger_voice_module(message)
            send_message_over_serial(message)
        elif flex1_val < 600 and flex2_val > 600 and flex3_val < 600:#1,3
            message = "Hello, Nice To Meet You"
            trigger_voice_module(message)
            send_message_over_serial(message)
        elif flex1_val > 600 and flex2_val < 600 and flex3_val < 600:#2,3
            message = "Thank you"
            trigger_voice_module(message)
            send_message_over_serial(message)
        elif flex1_val < 600 and flex2_val < 600 and flex3_val < 600:#all
            message = "Please stop"
            trigger_voice_module(message)
            send_message_over_serial(message)
        

if __name__ == "__main__":
    main()

