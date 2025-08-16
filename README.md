# APasm
Require:
- [![Python3](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
- [![QEMU](https://img.shields.io/badge/QEMU-Emulator-blue)](https://www.qemu.org/) or another emulator
- [![Hex Editor](https://img.shields.io/badge/Hex-Editor-blue)](https://mh-nexus.de/en/hxd/) Optional

License:
- [![License](https://img.shields.io/badge/MIT-License-green)](https://github.com/RandomX42069/APasm/blob/main/License.md)

Example Usage:
---
```python
from AvalonPasm import *

setah       =     MOV_imm("ah", 0x0E)                           # call BIOS print
setal       =     MOV_imm("al", 0x64)                           # print "d"
call        =     BIOSCALL_10h

total       =     setah + setal + call                          # mix the code
bootloader  =     total + cli() + hlt() + jmp(-2) + BootPad()   # boot loop

with open("Bootloader.bin", "w") as f:
  f.write(bootloader)
```
