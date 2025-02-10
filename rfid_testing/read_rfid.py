from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *
import time

def main():
    # Initialize a DigitalOutput device to control an output pin
    digitalOutput2 = DigitalOutput()

    # Set the channel where the output is connected (in this case, channel 2)
    digitalOutput2.setChannel(2)

    # Open the device and wait for attachment
    digitalOutput2.openWaitForAttachment(5000)

    # Set the duty cycle to 1 (fully on)
    digitalOutput2.setDutyCycle(1)
    time.sleep(1)
    digitalOutput2.setDutyCycle(0)
    time.sleep(1)
    digitalOutput2.setDutyCycle(1)

    # Wait for the user to press Enter before stopping
    try:
        input("Press Enter to Stop\n")
    except (Exception, KeyboardInterrupt):
        pass

    # Close the DigitalOutput device
    digitalOutput2.close()

# Run the main function
if __name__ == "__main__":
    main()


