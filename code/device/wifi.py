import network, time, ntptime

def connectWiFi():
    with open("wifi_config.txt", "r") as f:
        lines = f.readlines()
    ssid   = lines[0]
    passwd = lines[1]
    setUpWiFi(passwd, passwd)

def setUpWiFi(ssid, passwd):
    wifi = network.WLAN(network.WLAN.IF_STA)
    wifi.active(True)
    wifi.scan()
    wifi.connect(ssid, passwd)
    while not wifi.isconnected():
        time.sleep(1)
        print("Connecting to WiFi...")
        wifi.connect(ssid, passwd)
    print("Connected to WiFi.")
    print(wifi.ifconfig())

if __name__ == "__main__":    
    connectWiFi()
    ntptime.settime()
    print("Current time in UTC:", time.localtime())

