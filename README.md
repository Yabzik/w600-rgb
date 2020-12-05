# About

This is a set of scripts and instructions for MicroPython firmware on a W600 chip. Originally designed for cheap Chinese **AM-WIFI-002** RGB strip controller, but can be used for any W600-based device.

# Hardware

There is a module inside the controller on the board that can be easily confused with the ESP-12, moreover there is no markings on the metal shield.
<img align="right" src="https://user-images.githubusercontent.com/22223120/101246339-54b93280-371b-11eb-973b-725bcce2d94a.jpg" width="30%">

In fact, it is a TW-03 module based on the W600 chip. In order to flash it, **you need to connect GND, TXD and RXD pins with any USB-UART converter** (provided that the power comes from the main board, or in addition 3.3V to the VCC pin). **Pinout of GND, VCC, TXD, RXD fully complies with ESP-12.**
In addition, if you are using another W600-based device, you need to find out the peripheral connection pins (the easiest way is using a multimeter or along the tracks on the PCB). In this case, we use pin **PB16 for red, PB18 for green and PB15 for blue**.

![tw03s](https://user-images.githubusercontent.com/22223120/101246451-13755280-371c-11eb-8b52-cd3cfec66663.jpg)


# Installation

1. Download MicroPython firmware from the official site of WinnerMicro ([link](http://www.winnermicro.com/upload/1/editor/1568709203932.zip "firmware"))
2. Install [w600tool](https://github.com/vshymanskyy/w600tool "w600tool")
3. Connect everything as described in the hardware section and flash the chip
	`w600tool -u wm_w600.fls`
4.  Setup scripts inside flash memory:

	After flashing MicroPython and resetting module you should get Python prompt on serial port. Next you need to connect to your Wi-Fi network:
	
```python
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan() # Scan for available access points
sta_if.connect("<ssid>", "<password>")
sta_if.isconnected() # Check if there is a connection
```
If you do not receive a list of networks after scanning, the wrong wireless channel is most likely selected (for configuration, use the AT commands AT+CHL and AT+CHLL) (for more details, see the [official manual](http://www.winnermicro.com/en/upload/1/editor/1559640551866.pdf "official manual"))

After connecting to wireless network, you need to start built-in FTP server to upload python scripts.
```python
import w600
w600.run_ftpserver(port=21, username="root", password="root")
```
Use **FileZilla FTP Client** to connect, because the built-in server uses a limited set of instructions and other clients will most likely not work.

Now you can clone this repository, edit the main.py and run.py files as you need (at least Wi-Fi settings in main.py file) (more details in the software section), and upload them to the chip via FTP.

# Software

This script provides very simple functionality to manage RGB strip color through the browser. If desired, it is easy to modify it to use, for example, MQTT.
[MicroPyServer by troublegum](https://github.com/troublegum/micropyserver "MicroPyServer by troublegum") is used for web-server functionality. On the GET / path, it sends the index.html page, GET /rgb is used for color management (eg /rgb?r=255&g=255&b=255), GET /reboot can be used for remote reboot. The last set color is saved to rgb file for recovery after reboot.
PWM is used to control RGB colors. If you are using other pins for PWM peripheral control, set channel numbers according to the table.

The other functionality of the W600 chip with MicroPython firmware is well described in the [official manual](http://www.winnermicro.com/en/upload/1/editor/1573450100546.pdf "official manual").

# AM-WIFI-002 board

<img align="left" src="https://user-images.githubusercontent.com/22223120/101246535-a8784b80-371c-11eb-8d20-c838469b1f55.jpg" width="45%">
<img align="right" src="https://user-images.githubusercontent.com/22223120/101246536-a910e200-371c-11eb-9e50-7f6678396237.jpg" width="45%">

