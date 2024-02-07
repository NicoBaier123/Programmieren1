import time

def traffic_lights():
    while True:
        print("Red light")
        time.sleep(5)  # Wait for 5 seconds
        
        print("Green light")
        time.sleep(5)  # Wait for 5 seconds
        
        print("Yellow light")
        time.sleep(2)  # Wait for 2 seconds

traffic_lights()