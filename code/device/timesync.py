import wifi, time, ntptime, machine

# EDT (Eastern Daylight Time; summer): -4
# EST (winter after Nov 2): -5

UTC_OFFSET_HR = -4

def sync(utcOffset = UTC_OFFSET_HR):
    wifi.connectWiFi()
    syncToUtc()

    utcNow = time.localtime()
#     print(utcNow)  
    localNowSeconds = time.time() + (utcOffset * 3600)
    yr, mo, day, hr, minute, sec, wkday, yrday = time.localtime(localNowSeconds)
    machine.RTC().datetime((yr, mo, day, wkday, hr, minute, sec, 0))
    print(f"Time synched to local time:", time.localtime())

def syncToUtc():
    while(True):
        try:
            ntptime.settime()
            print("Time synched to UTC")
            break
        except OSError as e:
            if e.args[0] == 116: # ETIMEDOUT
                print("NTP request timed out. Retrying...")
                continue

if __name__ == "__main__":
    sync()
    
    
   
    
