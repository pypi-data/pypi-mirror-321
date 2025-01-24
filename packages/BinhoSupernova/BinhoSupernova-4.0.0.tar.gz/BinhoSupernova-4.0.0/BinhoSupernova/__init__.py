__all__ = ["Supernova"]

from .usb.usb_hid_manager import SUPERNOVA_PID, UsbHidManager

def getConnectedSupernovaDevicesList() -> list:
    '''
    This function can be used to scan all the Supernova devices connected
    to the host computer.

    Arguments
    ---------
    None

    Returns
    -------
    devices: list
        Python list that holds devices dictionary.
    '''

    return UsbHidManager.enumerate(SUPERNOVA_PID)