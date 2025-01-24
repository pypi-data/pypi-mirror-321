from .serializers import *
from ..helpers.validator import check_type, check_valid_id, check_range
from ...utils.system_message import SystemMessage, SystemModules, RequestValidatorOpcode

def i2cControllerInitValidator(metadata: dict):
    """
    This function validates the metadata for the I2C CONTROLLER INIT command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I2C CONTROLLER INIT request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["busId"], I2cBus)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for I2C Bus value"
        success = False
    if (not check_range(metadata["frequency_Hz"], int, I2C_CONTROLLER_MIN_FREQUENCY, I2C_CONTROLLER_MAX_FREQUENCY)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: frequency value out of range (100 kHz - 1 MHz)"
        success = False
    if (not check_type(metadata["pullUpValue"], I2cPullUpResistorsValue)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for pull up resistors value"
        success = False

    if (success):
        request, response = i2cControllerInitSerializer(metadata["id"], metadata["busId"], metadata["frequency_Hz"], metadata["pullUpValue"])

    return request, response, result

def i2cControllerSetParametersValidator(metadata: dict):
    """
    This function validates the metadata for the I2C SET PARAMETERS command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I2C SET PARAMETERS request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["busId"], I2cBus)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for I2C Bus value"
        success = False
    if (not check_range(metadata["frequency_Hz"], int, I2C_CONTROLLER_MIN_FREQUENCY, I2C_CONTROLLER_MAX_FREQUENCY)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: frequency value out of range (100 kHz - 1 MHz)"
        success = False
    if (not check_type(metadata["pullUpValue"], I2cPullUpResistorsValue)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for pull up resistors value"
        success = False
    
    if (success):
        request, response = i2cControllerSetParametersSerializer(metadata["id"], metadata["busId"], metadata["frequency_Hz"], metadata["pullUpValue"])

    return request, response, result

def i2cSetPullUpResistorsValidator(metadata: dict):
    """
    This function validates the metadata for the I2C SET PULL UP RESISTORS command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I2C SET PULL UP RESISTORS request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["busId"], I2cBus)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for I2C Bus value"
        success = False
    if (not check_type(metadata["pullUpResistorsValue"], I2cPullUpResistorsValue)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for pull up resistors value"
        success = False

    if (success):
        request, response = i2cSetPullUpResistorsSerializer(metadata["id"], metadata["busId"], metadata["pullUpResistorsValue"])

    return request, response, result

def i2cControllerWriteValidator(metadata: dict):
    """
    This function validates the metadata for the I2C CONTROLLER WRITE command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I2C CONTROLLER WRITE request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["busId"], I2cBus)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for I2C Bus value"
        success = False
    
    if (success):
        request, response = i2cControllerWriteSerializer(metadata["id"], metadata["busId"], metadata["targetAddress"],
                                                         metadata["registerAddress"], metadata["data"], metadata["isNonStop"], metadata["is10BitTargetAddress"])

    return request, response, result

def i2cControllerReadValidator(metadata: dict):
    """
    This function validates the metadata for the I2C CONTROLLER READ command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I2C CONTROLLER READ request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["busId"], I2cBus)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for I2C Bus value"
        success = False
    
    if (success):
        request, response = i2cControllerReadSerializer(metadata["id"], metadata["busId"], metadata["targetAddress"],
                                                        metadata["dataLength"], metadata["registerAddress"], metadata["is10BitTargetAddress"])

    return request, response, result
