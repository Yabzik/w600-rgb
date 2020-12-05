# main.py -- put your code here!

import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan()
sta_if.connect("<ssid>", "<password>")

import w600
w600.run_ftpserver(port=21,username="root",password="root")

print('Starting RGB controller...')
import run