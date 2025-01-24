# PulsarSDK: Python SDK for Binho Pulsar USB Host Adapter

PulsarSDK is a Python package for interacting with the Binho Pulsar USB host adapter. The Pulsar adapter provides simplified control of embedded systems, supporting I2C, SPI, UART, and GPIO communication protocols.

## Prerequisites

Ensure your system meets the following requirements before installing the PulsarSDK:

- Python 3.8 or higher
- Windows, macOS, or Linux
- Binho Pulsar USB host adapter with up-to-date firmware

## Installation

Install the latest version of the PulsarSDK from PyPi using pip:

```sh
pip install BinhoPulsar
```

After installation, the SDK is ready for use in your Python projects.

## API Overview

The Pulsar host adapter shares its API with the Binho Supernova adapter. If you're familiar with the SupernovaSDK, transitioning to the PulsarSDK will be straightforward, as the same commands and interfaces are used for the supported protocols.

# Examples Repository

To see some examples of how to use this Python package, please refer to the [examples repository](https://github.com/binhollc/SupernovaSDK-examples). This repository hosts different Jupyter notebooks for all the protocol and interface APIs provided by the PulsarSDK.

# Support

For help, please visit our [Customer Support Portal](https://support.binho.io/) or reach us at techsupport@binho.io.

# Changelog

## v1.0.0

### Improvements

- **Enhanced Validation:**
  - Comprehensive ID validation added across all SDK methods.
- **Preliminary 10-bit I2C Addressing Support:**
  - API update to include a flag in transfer methods to indicate a 10-bit target static address.
- **GPIO Initial Value Setting:**
  - API expanded to configure the initial value when setting a GPIO as a digital output. Feature not supported yet by firmware.
- **Communication Enhancements:**
  - A new USB Transfer protocol was implemented to make communication between devices and host more efficient.
  - The `open` method has been updated:
    - Removed the optional parameters vid and pid.
    - The new USB Transfer Protocol now manages the connection internally, automatically identifying and opening the first Pulsar device based on these values.
    
    This change simplifies device connection setup by offloading the responsibility of specifying vid and pid to the underlying protocol.

### Refactors

Several refactors were carried out as part of the implementation of `v1.0.0` to unify and standardize both the API and the dictionary responses across protocols.

- **Responses dictionary standardization:**
  - All the keys are written in ``snake_case`` style.
  - All the Python dictionaries returned by the API are based on a common structures containing the following  `key-value` pairs:
    - ``'id'``: integer number representing the response id.
    - ``command``: string name of the command.
    - ``result``: string indicating the result of the command request.
    - ``payload_length``: all those responses that return a variable length value, include this key to indicate the length of the returned variable length data.
    - ``payload``: this key identifies the variable length data.

```python
{'id':<response_id>, 'command':<command_name_string>, 'result': <result_string>, 'payload_length': <int>, 'payload': <list>}
```

See some examples below:

```python
{'id': 1, 'command': 'SYS GET USB STRING', 'result': 'SUCCESS', 'payload_length': 12, 'payload': 'MN-Binho LLC'}

{'id': 6, 'command': 'SYS SET I2C SPI UART GPIO VOLTAGE', 'result': 'SUCCESS'}

{'id': 12, 'command': 'I2C CONTROLLER WRITE', 'result': 'SUCCESS', 'i2c_bus': 'I2C_BUS_A', 'payload_length': 128}
```

The key ``'command'`` now identifies the command name instead of the integer number, and the key `'name'` was removed.

- **Integration of protocol roles in the API methods naming:** As part of the standardization process, the API methods expose the role to which the method relates to.
  - **UART:** Simplified nomenclature by removing "Controller" from command and parameter names, since there is no controller or target roles.
  - **I2C:** Standardized methods naming with "Controller", except for ``i2cSetPullUpResistors``, as it is independent of the device role.

- **Functional Consolidation:**
  - **I2C:** Unified I2C methods:
    - ``i2cWriteNonStop`` merged with ``i2cControllerWrite`` (triggered by the ``isNonStop`` flag)
    - ``i2cReadFrom`` integrated into ``i2cControllerRead`` (invoked based on register address length)
  - **Voltage setting**: Rename methods for clarification.
    - ``setI2cSpiUartBusVoltage`` as ``setI2cSpiUartGpioVoltage``
    - ``useExternalSourceForI2cSpiUartBusVoltage`` as ``useExternalI2cSpiUartGpioVoltage``

- **API Standardization:**
  - For the most part, all protocols are based on a set of methods to initialize and configure the device, as well as to issue transfers. For instance:
    - ``i2cControllerInit``, ``i2cControllerSetParameters``, ``i2cControllerWrite``, ``i2cControllerRead``
    - ``spiControllerInit``, ``spiControllerSetParameters``, ``spiControllerTransfer``
    - ``uartInit``, ``uartSetParameters``, ``uartSend``
  - In a near future, new methods such as ``deinit`` and ``getParameters`` might be implemented too.
  - **I2C frequencies configuration:**
    - In I2C, now the frequency is set through the methods ``i2cControllerInit`` and ``i2cControllerSetParameters``.
    - These changes are in line with the already implementation of the methods ``uartSetParameters`` and ``spiControllerSetParameters`` to set the UART baudrate and SPI clock frequency respectively.

### New Features

- **I2C Bus Selector:** Added `busId: I2cBus` parameter to all I2C-related commands. This parameter specifies the bus used for communication. The possible options are:
  - I2cBus.I2C_BUS_A: Corresponds to the Qwiic port.
  - I2cBus.I2C_BUS_B: Corresponds to the breakout board pins.

  This update provides flexibility for interacting with devices on different I2C interfaces.

- **I2C Controller Initialization Command:** Added a new method, ``i2cControllerInit(id: int, busId: I2cBus, frequency: int, pullUpResistorsValue: I2cPullUpResistorsValue)``, for initializing the I2C controller with enhanced configuration capabilities. Possible result codes include:
  - ``SUCCESS``
  - ``INVALID_PARAMETER``
  - ``FEATURE_NOT_SUPPORTED_BY_HARDWARE``
  - ``BUS_ALREADY_INITIALIZED``
  - ``BUS_NOT_SUPPORTED``

- **Voltage setting:**
  - Now the method  ``setI2cSpiUartGpioVoltage`` accept the value ``0`` mV as a valid voltage value. This allows the user to turn off the power supply and as a result the downstream devices.

- **UsbDisconnectionError exception:** A new exception was implemented which is raised when the USB Host device is unexpectedly disconnected. Deeper logic added was also added to return an error if a method is invoked after the disconnection and before a reconnection.