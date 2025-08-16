"""
# int.py - Integer Value Function Storage
"""
def UINT8(value):
    if not (0 <= value <= 0xFF):
        raise ValueError(f"UINT8 out of range: {value}")
    return value.to_bytes(1, "little")

def UINT16(value):
    if not (0 <= value <= 0xFFFF):
        raise ValueError(f"UINT16 out of range: {value}")
    return value.to_bytes(2, "little")

def UINT32(value):
    if not (0 <= value <= 0xFFFFFFFF):
        raise ValueError(f"UINT32 out of range: {value}")
    return value.to_bytes(4, "little")
