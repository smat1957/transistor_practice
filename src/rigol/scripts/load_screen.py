import pyvisa
import argparse
from PIL import Image
import io
  
argparser = argparse.ArgumentParser()
argparser.add_argument('-a', '--address', required=True, help='VISA address like "TCPIP::{ipaddress}::INSTR"')
argparser.add_argument('-o', '--output', help='Output file name (default: "screen.png")', default='screen.png')
args = argparser.parse_args()
  
inst = pyvisa.ResourceManager().open_resource(args.address)
print(inst.query('*IDN?').strip())
  
bmp_bin = inst.query_binary_values(':DISP:DATA?', datatype='B', container=bytes)
img = Image.open(io.BytesIO(bmp_bin))
img.save(args.output, args.output.split('.')[-1])