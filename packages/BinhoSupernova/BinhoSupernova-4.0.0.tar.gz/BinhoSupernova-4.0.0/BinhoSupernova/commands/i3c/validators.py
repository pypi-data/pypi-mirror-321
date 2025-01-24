from .serializers import *
from ..helpers.validator import check_type, check_range, check_valid_id, check_byte_array, getRepeatedItems
from ...utils.system_message import SystemMessage, SystemModules, RequestValidatorOpcode

#================================================================================#
# region I3C CONTROLLER INIT validator
#================================================================================#

def i3cControllerInitValidator(metadata: dict):
    """
    This function validates the metadata for the I3C CONTROLLER INIT command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C CONTROLLER INIT request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["pushPullRate"], I3cPushPullTransferRate)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for pushPullRate value"
        success = False
    if (not check_type(metadata["i3cOpenDrainRate"], I3cOpenDrainTransferRate)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for i3cOpenDrainRate value"
        success = False
    if (not check_type(metadata["i2cOpenDrainRate"], I2cTransferRate)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for i2cOpenDrainRate value"
        success = False

    if (success):
        request, response = i3cControllerInitSerializer(metadata["id"], metadata["pushPullRate"], metadata["i3cOpenDrainRate"], metadata["i2cOpenDrainRate"])

    return request, response, result

#endregion

#================================================================================#
# region I3C CONTROLLER SET PARAMETERS validator
#================================================================================#

def i3cControllerSetParametersValidator(metadata: dict):
    """
    This function validates the metadata for the I3C CONTROLLER SET PARAMETERS command to perform an I3C Private Read Transfer.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C CONTROLLER SET PARAMETERS request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["pushPullRate"], I3cPushPullTransferRate)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for pushPullRate value"
        success = False
    if (not check_type(metadata["i3cOpenDrainRate"], I3cOpenDrainTransferRate)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for i3cOpenDrainRate value"
        success = False
    if (not check_type(metadata["i2cOpenDrainRate"], I2cTransferRate)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for i2cOpenDrainRate value"
        success = False

    if (success):
        request, response = i3cControllerSetParametersSerializer(metadata["id"], metadata["pushPullRate"], metadata["i3cOpenDrainRate"], metadata["i2cOpenDrainRate"])

    return request, response, result

#endregion

#================================================================================#
# region I3C CONTROLLER INIT BUS validator
#================================================================================#

def i3cControllerInitBusValidator(metadata: dict):
    """
    This function validates the metadata for the I3C CONTROLLER INIT BUS command.
    Validates the targetDeviceTable of the user request. Checks that all I3C devices have a DAA method assigned and that there
    are no repeated addresses:
    - static address for I2C targets and I3C targets to be initialized with SETAASA
    - static and dynamic addresses for I3C targets to be initialized with SETDASA
    - dynamic addresses for I3C targets to be initialized with ENTDAA

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """

    request = None
    response = None

    def verifyI3cDynamicAddressAssignmentMethod(targetDeviceTable: dict):
        """
        Verifies that all I3C entries from the targetDeviceTable have a DAA method assigned.

        Arguments
        ---------
        dict: dictionary of metadata that represents the targetDeviceTable for I3cInitBusRequest_t

        Returns
        -------
        indexOfAddrWithoutMethod
            Index of the entries from targetDeviceTable that does not indicate a DAA method.

        """

        indexOfAddrWithoutMethod = []
        for index, target in targetDeviceTable.items():
            if ((target["configuration"]["targetType"] == TargetType.I3C_DEVICE) and
                ( target["configuration"]["daaUseSETDASA"] == False) and ( target["configuration"]["daaUseSETAASA"] == False) and ( target["configuration"]["daaUseENTDAA"] == False)):
                indexOfAddrWithoutMethod.append(index)
        return indexOfAddrWithoutMethod

    def getRepeatedAddresses(targetDeviceTable: dict):
        """
        Gets all the repeated addresses from the targetDeviceTable argument.

        Arguments
        ---------
        dict: dictionary of metadata that represents the targetDeviceTable for I3cInitBusRequest_t

        Returns
        -------
        listOfAddresses
           List of Addresses repeated in targetDeviceTable.

        """

        # Address used for SETDASA point to point
        SETDASA_POINT_TO_POINT_ADDR = 0x01

        listOfAddresses = []

        for target in targetDeviceTable.values():
            if (target["configuration"]["targetType"] == TargetType.I3C_DEVICE):

                # If the I3C device supports SETDASA and its static and dynamic addresses are SETDASA_POINT_TO_POINT_ADDR it might refer to a point-to-point SETDASA
                if not((target["configuration"]["daaUseSETDASA"] == True) and (target['staticAddress'] == SETDASA_POINT_TO_POINT_ADDR) and (target['dynamicAddress'] == SETDASA_POINT_TO_POINT_ADDR)):

                    if (target["configuration"]["daaUseSETDASA"] == True) or (target["configuration"]["daaUseENTDAA"] == True):
                        listOfAddresses.append(target['dynamicAddress'])

                    if (target["configuration"]["daaUseSETDASA"] == True) or (target["configuration"]["daaUseSETAASA"] == True):
                        listOfAddresses.append(target['staticAddress'])

            if (target["configuration"]["targetType"] == TargetType.I2C_DEVICE):
                listOfAddresses.append(target['staticAddress'])

        # Return the list of repeated addresses
        return getRepeatedItems(listOfAddresses)

    if metadata.get("targetDeviceTable") is not None:
        targetDeviceTable = metadata["targetDeviceTable"]

        listOfTargetsWithoutDaaMethod = verifyI3cDynamicAddressAssignmentMethod(targetDeviceTable)
        if listOfTargetsWithoutDaaMethod:
            targets_str = ', '.join([f"{target_index}" for target_index in listOfTargetsWithoutDaaMethod])
            message = f"I3C CONTROLLER INIT BUS failed: target/s in position {targets_str} of the input table not supporting any DAA method"
            result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.FAIL, message)
            return request, response, result

        listOfRepeatedAddr = getRepeatedAddresses(targetDeviceTable)
        if listOfRepeatedAddr:
            addresses_str = ', '.join([f"0x{addr:02X}" for addr in listOfRepeatedAddr])
            message = f"I3C CONTROLLER INIT BUS failed: address/es {addresses_str} repeated"
            result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.FAIL, message)
            return request, response, result

    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C CONTROLLER INIT BUS request success")
    success = True

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False

    if (success):
        request, response = i3cControllerInitBusSerializer(metadata["id"], metadata["targetDeviceTable"])

    return request, response, result

#endregion

#================================================================================#
# region I3C CONTROLLER RESET BUS validator
#================================================================================#

def i3cControllerResetBusValidator(metadata: dict):
    """
    This function validates the metadata for the I3C CONTROLLER RESET BUS command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C CONTROLLER RESET BUS request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False

    if (success):
        request, response = i3cControllerResetBusSerializer(metadata["id"])

    return request, response, result

#endregion

#================================================================================#
# region I3C CONTROLLER GET TARGET DEVICES TABLE validator
#================================================================================#

def i3cControllerGetTargetDevicesTableValidator(metadata: dict):
    """
    This function validates the metadata for the I3C CONTROLLER GET TARGET DEVICES TABLE command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C CONTROLLER GET TARGET DEVICES TABLE request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False

    if (success):
        request, response = i3cControllerGetTargetDevicesTableSerializer(metadata["id"])

    return request, response, result

#endregion

#================================================================================#
# region I3C CONTROLLER SET TARGET DEVICE CONFIGURATION validator
#================================================================================#

def i3cControllerSetTargetDeviceConfigurationValidator(metadata: dict):
    """
    This function validates the metadata for the I3C CONTROLLER SET TARGET DEVICE CONFIGURATION command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C SET TARGET DEVICE CONFIG request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False

    if (success):
        request, response = i3cControllerSetTargetDeviceConfigurationSerializer(metadata["id"], metadata["targetAddress"], metadata["configuration"])

    return request, response, result

#endregion

#================================================================================#
# region I3C CONTROLLER PRIVATE WRITE validator
#================================================================================#

def i3cControllerWriteValidator(metadata: dict):
    """
    This function validates the metadata for the I3C CONTROLLER PRIVATE TRANSFER command to perform an I3C Private Write Transfer.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C CONTROLLER PRIVATE WRITE request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["mode"], TransferMode)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for mode value"
        success = False

    if (success):
        request, response = i3cControllerWriteSerializer(metadata["id"], metadata["targetAddress"], metadata["mode"], metadata["registerAddress"], metadata["data"], metadata["startWith7E"])

    return request, response, result

#endregion

#================================================================================#
# region I3C CONTROLLER PRIVATE READ validator
#================================================================================#

def i3cControllerReadValidator(metadata: dict):
    """
    This function validates the metadata for the I3C CONTROLLER PRIVATE TRANSFER command to perform an I3C Private Read Transfer.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C CONTROLLER PRIVATE READ request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["mode"], TransferMode)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for mode value"
        success = False

    if (success):
        request, response = i3cControllerReadSerializer(metadata["id"], metadata["targetAddress"], metadata["mode"], metadata["registerAddress"], metadata["length"], metadata["startWith7E"])

    return request, response, result

#endregion

#================================================================================#
# region I3C CONTROLLER CCC TRANSFER validator
#================================================================================#

def i3cControllerCccTransferValidator(metadata: dict):
    """
    This function validates the metadata for the I3C CONTROLLER CCC TRANSFER command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C SEND CCC request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["mode"], TransferMode)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for mode value"
        success = False

    if (success):
        request, response = i3cControllerCccTransferSerializer(metadata["id"], metadata["targetAddress"], metadata["direction"], metadata["mode"], metadata["commandType"], metadata["defByte"], metadata["ccc"], metadata["length"], metadata["data"])

    return request, response, result

#endregion

#================================================================================#
# region I3C CONTROLLER TRIGGER TARGET RESET PATTERN validator
#================================================================================#

def i3cControllerTriggerTargetResetPatternValidator(metadata: dict):
    """
    This function validates the metadata for the I3C TRIGGER TARGET RESET PATTERN command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C TRIGGER TARGET RESET PATTERN request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["pattern"], I3cPattern)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for pattern value"
        success = False

    if (success):
        request, response = i3cControllerTriggerPatternSerializer(metadata["id"],  metadata["pattern"])

    return request, response, result

#endregion

#================================================================================#
# region I3C CONTROLLER TRIGGER HDR EXIT PATTERN validator
#================================================================================#

def i3cControllerTriggerHdrExitPatternValidator(metadata: dict):
    """
    This function validates the metadata for the I3C TRIGGER TARGET EXIT PATTERN command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C TRIGGER TARGET EXIT PATTERN request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["pattern"], I3cPattern)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for pattern value"
        success = False

    if (success):
        request, response = i3cControllerTriggerPatternSerializer(metadata["id"], metadata["pattern"])

    return request, response, result

#endregion

#================================================================================#
# region I3C TARGET validators
#================================================================================#

def i3cTargetInitValidator(metadata: dict):
    """
    This function validates the metadata for the I3C TARGET INIT command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C TARGET INIT request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["memoryLayout"], I3cTargetMemoryLayout_t)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for memory layout value"
        success = False
    if (len(metadata["pid"])!=sizeof(I3cPidBytes_t)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: PID length should be 6 bytes"
        success = False
    if (not check_range(metadata["bcr"], int, 0, 127)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: BCR out of range [0,127]"
        success = False
    if (not check_type(metadata["dcr"], I3cTargetDcr_t)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for DCR value"
        success = False
    if (not check_range(metadata["staticAddress"], int, 0, 127)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: Static Address out of range [0,127]"
        success = False

    i2c_reserved_addresses = list(range(0x00, 0x08)) + list(range(0x78, 0x80))

    if (metadata["staticAddress"] in i2c_reserved_addresses):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: Invalid Static Address value. Reserved by I2C protocol"
        success = False

    if (not check_range(metadata["mwl"], int, 0, 1024)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: Maximum Write Length out of range [0,1024]"
        success = False
    if (not check_range(metadata["mrl"], int, 0, 1024)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: Maximum Read Length out of range [0,1024]"
        success = False

    if (success):
        request, response = i3cTargetInitSerializer(metadata["id"], metadata["memoryLayout"], metadata["pid"], metadata["bcr"], metadata["dcr"], metadata["staticAddress"], metadata["mwl"], metadata["mrl"])

    return request, response, result

def i3cTargetSetParametersValidator(metadata: dict):
    """
    This function validates the metadata for the I3C TARGET SET PARAMETERS command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C TARGET SET PARAMETERS request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong id value"
        success = False
    if (not check_type(metadata["memoryLayout"], I3cTargetMemoryLayout_t)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for memory layout value"
        success = False
    if (len(metadata["pid"])!=sizeof(I3cPidBytes_t)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: PID length should be 6 bytes"
        success = False
    if (not check_range(metadata["bcr"], int, 0, 127)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: BCR out of range [0,127]"
        success = False
    if (not check_type(metadata["dcr"], I3cTargetDcr_t)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: wrong type for DCR value"
        success = False
    if (not check_range(metadata["staticAddress"], int, 0, 127)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: Static Address out of range [0,127]"
        success = False

    i2c_reserved_addresses = list(range(0x00, 0x08)) + list(range(0x78, 0x80))

    if (metadata["staticAddress"] in i2c_reserved_addresses):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: Invalid Static Address value. Reserved by I2C protocol"
        success = False

    if (not check_range(metadata["mwl"], int, 0, 1024)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: Maximum Write Length out of range [0,1024]"
        success = False
    if (not check_range(metadata["mrl"], int, 0, 1024)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "ARGUMENT ERROR: Maximum Read Length out of range [0,1024]"
        success = False

    if (success):
        request, response = i3cTargetSetParametersSerializer(metadata["id"], metadata["memoryLayout"], metadata["pid"], metadata["bcr"], metadata["dcr"], metadata["staticAddress"], metadata["mwl"], metadata["mrl"])

    return request, response, result

def i3cTargetWriteMemoryValidator(metadata: dict):
    """
    This function validates the metadata for the I3C TARGET WRITE MEMORY command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C TARGET WRITE MEMORY request success")
    success = True
    request = None
    response = None

    # Check memory address value.
    if (metadata["memoryAddress"] is None):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "I3C TARGET WRITE MEMORY request failed, no memory address input"
        success = False
    if (metadata["data"] is None) or (len(metadata["data"]) == 0):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "I3C TARGET WRITE MEMORY request failed, no data input"
        success = False
    if (not check_byte_array(metadata["data"],1024)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "I3C TARGET WRITE MEMORY request failed, invalid data input"
        success = False
    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "I3C TARGET WRITE MEMORY request failed, wrong id value"
        success = False

    if (success):
        request, response = i3cTargetWriteMemorySerializer(metadata["id"], metadata["memoryAddress"], metadata["data"])

    return request, response, result

def i3cTargetReadMemoryValidator(metadata: dict):
    """
    This function validates the metadata for the I3C TARGET READ MEMORY command.

    Arguments
    ---------
    metadata : dict
        Metadata to be validated.

    Returns
    -------
    tuple
        A tuple containing the request, response and result of the validation.

    """
    result = SystemMessage(SystemModules.VALIDATION, RequestValidatorOpcode.SUCCESS, "I3C TARGET READ MEMORY request success")
    success = True
    request = None
    response = None

    if (not check_valid_id(metadata["id"])):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "I3C TARGET READ MEMORY request failed, wrong id value"
        success = False
    if (metadata["memoryAddress"] is None) or (not check_range(metadata["memoryAddress"],int,0,1024)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "I3C TARGET READ MEMORY request failed, invalid memory address value"
        success = False
    if (metadata["length"] is None) or (not check_range(metadata["length"],int,0,1024)):
        result.opcode = RequestValidatorOpcode.FAIL
        result.message = "I3C TARGET READ MEMORY request failed, invalid length value"
        success = False

    if (success):
        request, response = i3cTargetReadMemorySerializer(metadata["id"], metadata["memoryAddress"], metadata["length"])

    return request, response, result

#endregion