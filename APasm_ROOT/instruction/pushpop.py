import importlib.util as im

# Import RM dynamically
rmpath = "APasm_ROOT/definitions/RM.py"
rmspec = im.spec_from_file_location("rmmodule", rmpath)
rmmodule = im.module_from_spec(rmspec)
rmspec.loader.exec_module(rmmodule)

modpath = "APasm_ROOT/definitions/mod.py"
modspec = im.spec_from_file_location("modmodule", modpath)
modmodule = im.module_from_spec(modspec)
modspec.loader.exec_module(modmodule)

movpath = "APasm_ROOT/instruction/mov.py"
movspec = im.spec_from_file_location("movmodule", movpath)
movmodule = im.module_from_spec(movspec)
movspec.loader.exec_module(movmodule)

segpath = "APasm_ROOT/instruction/preflix.py"
segspec = im.spec_from_file_location("segmodule", segpath)
segmodule = im.module_from_spec(segspec)
segspec.loader.exec_module(segmodule)

def push_es() -> bytes:
    """Encode PUSH ES (segment register)."""
    opcode = 0x06
    return bytes([opcode])

def pop_es() -> bytes:
    """Encode POP ES (segment register)"""
    opcode = 0x07
    return bytes([opcode])

def push_cs() -> bytes:
    """Encode PUSH CS (segment register)"""
    opcode = 0x0E
    return bytes([opcode])

def push_ss() -> bytes:
    """Encode PUSH SS (segment register)"""
    opcode = 0x16
    return bytes([opcode])

def pop_ss() -> bytes:
    """Encode POP SS (segment register)"""
    opcode = 0x17
    return bytes([opcode])

def push_ds() -> bytes:
    """Encode PUSH DS (segment register)"""
    opcode = 0x1E
    return bytes([opcode])

def pop_ds() -> bytes:
    """Encode POP DS (segment register)"""
    opcode = 0x1F
    return bytes([opcode])
