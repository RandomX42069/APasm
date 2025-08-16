# APasm

## Requirements
- [![Python3](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
- [![QEMU](https://img.shields.io/badge/QEMU-Emulator-blue)](https://www.qemu.org/) (or another emulator)
- [![Hex Editor](https://img.shields.io/badge/Hex-Editor-blue)](https://mh-nexus.de/en/hxd/) (optional)

## Example Usage
```python
from AvalonPasm import *

setah      = MOV_imm("ah", 0x0E)  # call BIOS print
setal      = MOV_imm("al", 0x64)  # print "d"
call       = BIOSCALL_10h()

total      = setah + setal + call
bootloader = total + cli() + hlt() + jmp(-2) + BootPad()

with open("Bootloader.bin", "wb") as f:
    f.write(bootloader)
```
## APasm APIs
- APasmEnv   - Create an APasm Development Environment(class)
- QEMU       - Use Subproccess to test your bootloader in QEMU(class)

## APasmEnv Usage
```python
from AvalonPasm import *
env = APasmEnv(  # your code will be packaged automatically
  MOV_imm("ah", 0x0E),
  MOV_imm("al", 0x64),  # print d
  BIOSCALL_10h()  
)
env.Push() # -> D:/APasmEnv Output/Untitled APasm Output File No{rand.randint(0,1000000)}
```

## License
- [![License](https://img.shields.io/badge/MIT-License-green)](https://github.com/RandomX42069/APasm/blob/main/LICENSE)
  
