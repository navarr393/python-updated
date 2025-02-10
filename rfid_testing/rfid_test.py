from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
from Phidget22.Devices.DigitalOutput import *
import time

# Protocol constants (from Phidget22 API)
ISO14443 = 1
ISO15693 = 2
FELICA = 3
ICODE = 4

def onTagGainedHandler(self, tag, protocol):
    # Map the protocol number to a human-readable name
    if protocol == ISO14443:
        protocol_name = "ISO14443"
    elif protocol == ISO15693:
        protocol_name = "ISO15693"
    elif protocol == FELICA:
        protocol_name = "FELICA"
    elif protocol == ICODE:
        protocol_name = "ICODE"
    else:
        protocol_name = "Unknown Protocol"

    # Print the tag and protocol name
    print(f"Tag detected: {tag}, Protocol: {protocol_name}")
        # define the digital output
    digitalOutput2 = DigitalOutput()
    # set the channel where the output is connected (in this case, channel 2)
    digitalOutput2.setChannel(2)
    # open the deivice and wait for attachment
    digitalOutput2.openWaitForAttachment(5000)
    # set the duty cycle to 1 (fully on)
    digitalOutput2.setDutyCycle(1)
    time.sleep(1)
    digitalOutput2.setDutyCycle(0)

# TODO: Set up a server to handle incoming requests, maybe flask or tornado

def main():
    try:
        # Create an RFID object
        rfid = RFID()

        # Open the RFID device
        rfid.openWaitForAttachment(5000)  # Wait for the device to be attached (5 seconds)

        # Set up the handler for when a tag is read
        rfid.setOnTagHandler(onTagGainedHandler)

        # Wait indefinitely (keeping the program running to listen for tags)
        print("Waiting for RFID tag...")
        input("Press Enter to exit...\n")

        # Close the device when done
        rfid.close()

    except PhidgetException as e:
        print("Phidget exception:", e)

if __name__ == "__main__":
    main()



