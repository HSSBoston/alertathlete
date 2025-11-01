from machine import Pin, PWM
import time

# Define the buzzer pin (check your M5StickC documentation for the correct pin)
buzzer_pin = 2

# Initialize the buzzer pin as a PWM output. Default to off
buzzer = PWM(Pin(buzzer_pin), freq=440, duty=0)

def beep(freq, durationMsec):
    buzzer.freq(freq)
    buzzer.duty(50)  # Duty cycle (loudness)
    time.sleep_ms(durationMsec)
    buzzer.duty(0)

def demo():
    try:
      while True:
          beep(1000, 200)
          time.sleep(0.3)
          beep(500, 100)
          time.sleep(1)
    except KeyboardInterrupt:
        buzzer.duty(0)
        print("Exiting...")

if __name__ == "__main__":
    demo()