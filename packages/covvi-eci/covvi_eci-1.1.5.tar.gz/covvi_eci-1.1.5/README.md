# COVVI Ethernet Control Interface (ECI)

This software is used to communicate and control the COVVI Robotic Hand over ethernet. You can:
- turn the power on/off to the hand.
- discover the ECI on the network.
- control the 5 digits plus the rotation of the thumb independently or all together.
- move the hand to pre-defined grip poses.
- read realtime data such as digit positions, digit status, finger-tip pressure, orientation, environmental data.
- define custom callback functions for the realtime data.

## Getting Started

Enable logging debug mode if you wish to see debug messages.


```python
import logging
logging.getLogger().setLevel(logging.DEBUG)
```

Return logging to warning mode if you wish to hide the debug messages.


```python
import logging
logging.getLogger().setLevel(logging.WARNING)
```

### Installing the ECI package

Installing the ECI Python package is a simple process. It is recommended (but not necessary) to create a virtual environment:

```python3 -m pip install virtualenv```

```python3 -m venv .venv```

Then activate this virtual environment:

Ubuntu: ```source ./.venv/bin/activate```

PowerShell: ```.\.venv\Scripts\activate.ps1```

On Ubuntu, you can check that your environment is activated with:

```type python pip```

This should output something similar to:

```python is /path/to/your/project/.venv/bin/python```

```pip is /path/to/your/project/.venv/bin/pip```

In PowerShell, you can check that your environment is activated with:

```where.exe python```

This should output some lines of text, with the first line being something similar to:

```C:\path\to\your\project\.venv\Scripts\python.exe```

Install the ECI package via:

```pip install covvi-eci```

### Discovering the interface

Below is an example code snippet for programmatically discovering the interface. In this example, the IP address of the network interface to discover on is: ```192.168.1.1```. You can listen on multiple interfaces at the same time with ```DiscoveryInterface('addr1', 'addr2', ..., 'addrN')```.


```python
from eci import DiscoveryInterface
with DiscoveryInterface('192.168.1.1') as interface:
    for msg, addr in interface.forever_get_eci_list():
        print(msg)
        break
HOST = msg.ip
print(f'The HOST has been set to: {HOST}')
```

Here is an example of obtaining the IP address of the hand by providing the serial number:


```python
from eci import get_discovery_from_serial
msg = get_discovery_from_serial('192.168.1.1', serial_number=1234)
print(msg)
HOST = msg.ip
print(f'The HOST has been set to: {HOST}')
```

Or set the IP address manually:


```python
HOST = '192.168.1.5'
```

### Setting the discovery information

To change the discovery information of the ECI, send a ```DiscoveryConfigMsg``` via the ```DiscoveryInterface```. Only the ```ip```, ```subnet_mask```, ```gateway```, ```hostname```, and ```dhcp``` can be changed. The rest of the attributes must match those of the ```DiscoveryResponseMsg```.


```python
from eci import DiscoveryInterface, DiscoveryConfigMsg, DeviceClassType, Product, ProductID
with DiscoveryInterface('192.168.1.1') as interface:
    interface.send_config(DiscoveryConfigMsg(
        discovery_version      = 2,                                      # cannot be changed
        device_serial_number   = 1008,                                   # cannot be changed
        mac                    = 'D8:47:8F:3F:63:F0',                    # cannot be changed
        device_class_type      = DeviceClassType.RCI,                    # cannot be changed
        manufacturer_id        = 0,                                      # cannot be changed
        product_id             = Product(ProductID.REMOTE),              # cannot be changed
        ip                     = '192.168.1.6',                          # can be changed
        subnet_mask            = '255.255.255.0',                        # can be changed
        gateway                = '192.168.1.1',                          # can be changed
        dns                    = '192.168.1.1',                          # can be changed
        hostname               = 'covvi-robot3',                         # can be changed
        dhcp                   = False,                                  # can be changed
        hand_comms             = False,                                  # cannot be changed
        hand_power             = False,                                  # cannot be changed
        client_connected       = False,                                  # cannot be changed
        client_address         = '0.0.0.0',                              # cannot be changed
        request_source_address = '192.168.1.1',                          # cannot be changed
    ), '192.168.1.5')
```

### Connecting/Disconnecting the interface

All interactions with the ECI occur through the context manager: ```CovviInterface```. It opens and closes the interface:


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    ...
```

If the 'with' clause is a problem in your application, then you can always use the ```start``` and ```stop``` functions to start and stop the COVVI Interface. Using ```start``` and ```stop``` is preferable when your application uses multiple threads and callback functions.


```python
from eci import CovviInterface
eci = CovviInterface(HOST).start()
...
eci.stop()
```

## Hand Power

### setHandPowerOn() - Turn the power on to the hand


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.setHandPowerOn())
```

### setHandPowerOff() - Turn the power off to the hand


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.setHandPowerOff())
```

Subsequent code snippets assume that ```setHandPowerOn()``` has already been called and that the power to the hand is on. Power to the hand can be determined manually via a blue LED on the 'CAN' label on the hand.

## Discovery and device messages

### Hello

#### getHello() - Get a simple 'hello' response from the ECI


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.getHello())
```

### Firmware

#### getFirmware_PIC() - Get the PIC Firmware version


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.getFirmware_PIC_ECI())
    print(eci.getFirmware_PIC_HAND()) # Requires power to the hand (blue LED on)
```

### DeviceIdentity

#### getDeviceIdentity() - Get device identity parameters


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.getDeviceIdentity())
```

### DeviceProduct

#### getDeviceProduct() - Get product and manufacturer


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.getDeviceProduct())
```

## Real-time messages

### RealtimeCfg

#### setRealtimeCfg() - Set real-time update configuration

##### Turn all realtime packets on


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    eci.enableAllRealtimeCfg()
```


```python
from time import sleep
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    for _ in range(4):
        eci.setRealtimeCfg(
            digit_status    = True,
            digit_posn      = True,
            current_grip    = True,
            electrode_value = True,
            input_status    = True,
            motor_current   = True,
            digit_touch     = True,
            digit_error     = True,
            environmental   = True,
            orientation     = True,
            motor_limits    = True,
        )
        sleep(2)
        eci.setRealtimeCfg(
            digit_status    = False,
            digit_posn      = False,
            current_grip    = False,
            electrode_value = False,
            input_status    = False,
            motor_current   = False,
            digit_touch     = False,
            digit_error     = False,
            environmental   = False,
            orientation     = False,
            motor_limits    = False,
        )
        sleep(2)
```

##### Turn all realtime packets off


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    eci.disableAllRealtimeCfg()
```


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    eci.setRealtimeCfg(
        digit_status    = False,
        digit_posn      = False,
        current_grip    = False,
        electrode_value = False,
        input_status    = False,
        motor_current   = False,
        digit_touch     = False,
        digit_error     = False,
        environmental   = False,
        orientation     = False,
        motor_limits    = False,
    )
```


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    eci.setRealtimeCfg()
```

##### Setting the callbacks for each realtime message type


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    eci.callbackDigitStatusAll  = print
    eci.callbackDigitPosnAll    = print
    eci.callbackCurrentGrip     = print
    eci.callbackElectrodeValue  = print
    eci.callbackInputStatus     = print
    eci.callbackMotorCurrentAll = print
    eci.callbackDigitTouchAll   = print
    eci.callbackDigitError      = print
    eci.callbackEnvironmental   = print
    eci.callbackOrientation     = print
    eci.callbackMotorLimits     = print
```

##### Turn all realtime packets on and print all the parameters of each packet


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    eci.callbackDigitStatusAll  = print
    eci.callbackDigitPosnAll    = print
    eci.callbackCurrentGrip     = print
    eci.callbackElectrodeValue  = print
    eci.callbackInputStatus     = print
    eci.callbackMotorCurrentAll = print
    eci.callbackDigitTouchAll   = print
    eci.callbackDigitError      = print
    eci.callbackEnvironmental   = print
    eci.callbackOrientation     = print
    eci.callbackMotorLimits     = print

    eci.setRealtimeCfg(
        digit_status    = True,
        digit_posn      = True,
        current_grip    = True,
        electrode_value = True,
        input_status    = True,
        motor_current   = True,
        digit_touch     = True,
        digit_error     = True,
        environmental   = True,
        orientation     = True,
        motor_limits    = True,
    )
    from time import sleep
    sleep(60 * 10)
```

#### resetRealtimeCfg() - Reset the realtime callbacks (and stop streaming realtime messages)


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    eci.resetRealtimeCfg()
```

### DigitStatus

#### getDigitStatus_all() - Get all digit status flags


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.getDigitStatus_all())
```

#### getDigitStatus() - Get all digit status flags individually


```python
from eci import CovviInterface, Digit
with CovviInterface(HOST) as eci:
    for digit in Digit:
        print(digit.name, eci.getDigitStatus(digit))
```

### DigitPosn

#### getDigitPosn_all() - Get all digit positions


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.getDigitPosn_all())
```

#### getDigitPosn() - Get all digit positions individually


```python
from eci import CovviInterface, Digit
with CovviInterface(HOST) as eci:
    for digit in Digit:
        print(digit.name, eci.getDigitPosn(digit))
```

#### setDigitPosn() - Set all digit positions individually - Close the hand fully


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    eci.setDigitPosn(speed=50, thumb=0xFF, index=0xFF, middle=0xFF, ring=0xFF, little=0xFF, rotate=0xFF)
```

#### setDigitPosn() - Set all digit positions individually - Open the hand fully


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    eci.setDigitPosn(speed=50, thumb=0, index=0, middle=0, ring=0, little=0, rotate=0)
```

#### setDigitPosn() - Set all digit positions individually - Perform a thumbs up


```python
from time import sleep
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    eci.setDigitPosn(speed=50, thumb=0, index=0, middle=0, ring=0, little=0, rotate=0)
    sleep(1)
    eci.setDigitPosn(speed=50, thumb=0, index=0xFF, middle=0xFF, ring=0xFF, little=0xFF, rotate=0)
```

### CurrentGrip

#### getCurrentGrip() - Get the current grip


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.getCurrentGrip())
```

#### setCurrentGrip(grip_id) - Set the current grip


```python
from eci import CovviInterface, CurrentGripID
with CovviInterface(HOST) as eci:
    print(eci.setCurrentGrip(grip_id=CurrentGripID.GN0))
```

#### setCurrentGrip(grip_id) - Set the current grip to <current_grip_id>


```python
from eci import CovviInterface, CurrentGripID
with CovviInterface(HOST) as eci:
    print(eci.setCurrentGrip(grip_id=CurrentGripID.PREC_CLOSED))
```


```python
from eci import CovviInterface, Percentage
with CovviInterface(HOST) as eci:
    eci.setDirectControlClose(speed=Percentage(value=100))
```


```python
from eci import CovviInterface, Percentage
with CovviInterface(HOST) as eci:
    eci.setDirectControlOpen(speed=Percentage(value=100))
```


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    eci.setDirectControlStop()
```

### DirectControl

#### setDirectControlClose() - Close the whole hand


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    eci.setDirectControlClose(speed=100)
```

#### setDirectControlOpen() - Open the whole hand


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    eci.setDirectControlOpen(speed=100)
```

### DigitMove

#### setDigitMove() - Command to move each digit individually - Open the whole hand


```python
from eci import CovviInterface, Digit
with CovviInterface(HOST) as eci:
    for digit in Digit:
        eci.setDigitMove(digit, position=40, speed=50, power=20, limit=0)
```

#### setDigitMove() - Command to move each digit individually - Close the whole hand


```python
from eci import CovviInterface, Digit
with CovviInterface(HOST) as eci:
    for digit in Digit:
        eci.setDigitMove(digit, position=210, speed=50, power=20, limit=0)
```

#### setDigitMove() - Open the index digit


```python
from eci import CovviInterface, Digit
with CovviInterface(HOST) as eci:
    eci.setDigitMove(Digit.INDEX, position=44, speed=50, power=20, limit=0)
```

#### setDigitMove() - Close the index digit


```python
from eci import CovviInterface, Digit
with CovviInterface(HOST) as eci:
    eci.setDigitMove(Digit.INDEX, position=210, speed=50, power=20, limit=0)
```

#### setDigitMove() - Command to move each digit individually - Set the digits to random positions


```python
from random import randint
from eci import CovviInterface, Digit
with CovviInterface(HOST) as eci:
    for digit in Digit:
        eci.setDigitMove(digit, position=randint(40, 200), speed=50, power=20, limit=0)
```

### MotorCurrent

#### getMotorCurrent_all() - Get the motor current of all Digits


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.getMotorCurrent_all())
```

#### getMotorCurrent() - Get the motor current of all Digits individually


```python
from eci import CovviInterface, Digit5
with CovviInterface(HOST) as eci:
    for digit in Digit5:
        print(digit.name, eci.getMotorCurrent(digit))
```

### DigitError

#### getDigitError() - Get the digit error flags of all digits individually


```python
from eci import CovviInterface, Digit
with CovviInterface(HOST) as eci:
    for digit in Digit:
        print(digit.name, eci.getDigitError(digit))
```

## Digit configuration messages

### DigitConfig

#### getDigitConfig() - Get the limits of each digit individually


```python
from eci import CovviInterface, Digit
with CovviInterface(HOST) as eci:
    for digit in Digit:
        print(digit.name, eci.getDigitConfig(digit))
```

### PinchConfig

#### getPinchConfig() - Get the pinch points of each digit individually


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.getPinchConfig())
```

## Grip configuration messages

### GripName

#### getGripName


```python
from eci import CovviInterface, GripNameIndex
with CovviInterface(HOST) as eci:
    for grip_name_i in list(GripNameIndex):
        print(grip_name_i, eci.getGripName(grip_name_i))
```

## System and status messages

### Environmental

#### getEnvironmental() - Get the temperature, humidity, battery voltage values of the hand


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.getEnvironmental())
```

### SystemStatus

#### getSystemStatus() - Get the system status


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.getSystemStatus())
```

### Orientation

#### getOrientation() - Get the orientation of the hand


```python
from eci import CovviInterface
with CovviInterface(HOST) as eci:
    print(eci.getOrientation())
```

## Firmware update messages

### SendUserGrip

#### sendUserGrip(grip_index, grip_path) - Send a User Grip


```python
from eci import CovviInterface, GripNameIndex, UserGripID
with CovviInterface(HOST) as eci:
    print(eci.sendUserGrip(GripNameIndex.GN0, UserGripID.THUMBS_UP))
    for grip_name_i in list(GripNameIndex):
        print(grip_name_i, eci.getGripName(grip_name_i))
```

#### resetUserGrips() - Reset all the User Grips


```python
from eci import CovviInterface, GripNameIndex
with CovviInterface(HOST) as eci:
    eci.resetUserGrips()
    for grip_name_i in list(GripNameIndex):
        print(grip_name_i, eci.getGripName(grip_name_i))
```

### RemoveUserGrip

#### removeUserGrip(grip_index) - Remove a User Grip


```python
from eci import CovviInterface, GripNameIndex
with CovviInterface(HOST) as eci:
    print(eci.removeUserGrip(GripNameIndex.GN0))
    for grip_name_i in list(GripNameIndex):
        print(grip_name_i, eci.getGripName(grip_name_i))
```
