class UsbDisconnectionError(Exception):
    """
    Custom exception raised when an unexpected USB disconnection occurs.
    """
    def __init__(self, message="USB device unexpectedly disconnected"):
        super().__init__(message)