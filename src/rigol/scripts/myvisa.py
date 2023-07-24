import inspect
import pyvisa
print(inspect.getfile(pyvisa))

import pyvisa
inst = pyvisa.ResourceManager().open_resource('TCPIP::192.168.1.197::INSTR')
print(inst.query('*IDN?').strip())