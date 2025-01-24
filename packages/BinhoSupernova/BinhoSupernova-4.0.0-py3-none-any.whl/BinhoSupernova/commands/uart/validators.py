from .serializers import *
from ..helpers.validator import check_type, check_valid_id, check_byte_array
from ...utils.system_message import SystemMessage, SystemModules, RequestValidatorOpcode

def uartInitValidator(metadata: dict):
    """
    This function validates the metadata for the UART INIT command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result =  SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "UART INIT request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["baudRate"], UartBaudRate)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for baudrate value"
        success = False
    if (not check_type(metadata["hardwareHandshake"], bool)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for hardware handshake value"
        success = False
    if (not check_type(metadata["parityMode"], UartParity)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for parity mode value"
        success = False
    if (not check_type(metadata["dataSize"], UartDataSize)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for data size value"
        success = False
    if (not check_type(metadata["stopBitType"], UartStopBit)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for stop byte configuration value"
        success = False

    if (success):
        request, response = uartInitSerializer(metadata["id"], metadata["baudRate"], metadata["hardwareHandshake"], metadata["parityMode"], metadata["dataSize"], metadata["stopBitType"])

    return request, response, result

def uartSetParametersValidator(metadata: dict):
    """
    This function validates the metadata for the UART SET PARAMETERS command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "UART SET PARAMETERS request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["baudRate"], UartBaudRate)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for baudrate value"
        success = False
    if (not check_type(metadata["hardwareHandshake"], bool)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for hardware handshake value"
        success = False
    if (not check_type(metadata["parityMode"], UartParity)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for parity mode value"
        success = False
    if (not check_type(metadata["dataSize"], UartDataSize)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for data size value"
        success = False
    if (not check_type(metadata["stopBitType"], UartStopBit)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for stop byte configuration value"
        success = False

    if (success):
        request, response = uartSetParametersSerializer(metadata["id"], metadata["baudRate"], metadata["hardwareHandshake"], metadata["parityMode"], metadata["dataSize"], metadata["stopBitType"])

    return request, response, result

def uartSendValidator(metadata: dict):
    """
    This function validates the metadata for the UART SEND MESSAGE command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "UART SEND MESSAGE request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_byte_array(metadata["data"], MAX_UART_TRANSFER_LENGTH)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: invalid data array"
        success = False

    if (success):
        request, response = uartSendSerializer(metadata["id"], metadata["data"])

    return request, response, result