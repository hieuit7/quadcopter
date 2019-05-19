import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

while True:
        # L3G4200D address, 0x68(104)
        # Select Control register1, 0x20(32)
        #               0x0F(15)        Normal mode, X, Y, Z-Axis enabled
        try:
                bus.write_byte_data(0x69, 0x20, 0x0F)
        except:
                print("ss")
                pass
        # L3G4200D address, 0x68(104)
        # Select Control register4, 0x23(35)
        #               0x30(48)        Continous update, Data LSB at lower address
        #                                       FSR 2000dps, Self test disabled, 4-wire interface
        try:
                bus.write_byte_data(0x69, 0x23, 0x30)
        except:
                pass
        time.sleep(0.5)

        # L3G4200D address, 0x68(104)
        # Read data back from 0x28(40), 2 bytes, X-Axis LSB first
        try:
                data0 = bus.read_byte_data(0x69, 0x28)
        except:
                pass
        try:
                data1 = bus.read_byte_data(0x69, 0x29)
        except:
                pass
        # Convert the data
        try:
                xGyro
        except:
                pass
        else:
                xGyro = data1 * 256 + data0
                if xGyro > 32767 :
                        xGyro -= 65536

        # L3G4200D address, 0x68(104)
        # Read data back from 0x2A(42), 2 bytes, Y-Axis LSB first
        try:
                data0 = bus.read_byte_data(0x69, 0x2A)
        except:
                pass

        try:
                data1
        except NameError:
                pass
        else:
                data1 = bus.read_byte_data(0x69, 0x2B)

        # Convert the data
        try:
                yGyro = data1 * 256 + data0
        except:
                pass

        try:
                yGyro
        except:
                pass
        else:
                if yGyro > 32767 :
                        yGyro -= 65536

        # L3G4200D address, 0x68(104)
        # Read data back from 0x2C(44), 2 bytes, Z-Axis LSB first
        try:
                data0
        except:
                pass
        else:
                try:
                        data0 = bus.read_byte_data(0x69, 0x2C)
                except:
                        pass

        try:
                data1
        except:
                pass
        else:
                data1 = bus.read_byte_data(0x69, 0x2D)

        # Convert the data
        try:
                zGyro
        except:
                pass
        else:
                zGyro = data1 * 256 + data0
                if zGyro > 32767 :
                        zGyro -= 65536

        # Output data to screen
        try:
                xGyro
        except:
                pass
        else:
                print ("Rotation in X-Axis : %d" %xGyro)

        try:
                yGyro
        except:
                pass
        else:
                print ("Rotation in Y-Axis : %d" %yGyro)

        try:
                zGyro
        except:
                pass
        else:
                print ("Rotation in Z-Axis : %d" %zGyro)
