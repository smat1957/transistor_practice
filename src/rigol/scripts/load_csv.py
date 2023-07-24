import pyvisa
import argparse
import csv
  
def load_waveform(chidx, points_request):
    inst.write(f':WAV:SOUR CHAN{chidx}')
    inst.write(':WAV:MODE RAW')
    inst.write(f':WAV:POIN {points_request}')
    #inst.write(':WAV:FORM BYTE')
    inst.write(':WAV:FORM WORD')

    preample = inst.query(':WAV:PRE?').split(',')
    points = int(preample[2])
    xinc = float(preample[4])
    xorg = float(preample[5])
    xref = float(preample[6])
    yinc = float(preample[7])
    yorg = float(preample[8])
    yref = float(preample[9])

    print(f'loading CH{chidx} {points}pts')
    data_bin = inst.query_binary_values('WAV:DATA?', datatype='B', container=bytes)
    t = [(float(i) - xref)*xinc + xorg for i in range(points)]
    v = [(float(byte_data) - yref)*yinc + yorg for byte_data in data_bin]
    return t,v

argparser = argparse.ArgumentParser()
argparser.add_argument('-a', '--address', required=True, help='VISA address like "TCPIP::{ipaddress}::INSTR"')
argparser.add_argument('-o', '--output', help='Output file name (default: "waveform.csv")', default='waveform.csv')
argparser.add_argument('-p', '--points', type=int, help='Points of the data to be load', default=1000)
argparser.add_argument('-c', '--chlist', help='Specify channels which waveforms will be load from like "-c 1,2,3,4"', default='1')
args = argparser.parse_args()
  
chlist = [int(x) for x in args.chlist.split(',')]
  
inst = pyvisa.ResourceManager().open_resource(args.address)
print(inst.query('*IDN?').strip())
  
inst.write(':STOP')
inst.query('*OPC?')
  
load_data = {}
for chidx in chlist:
    t, v = load_waveform(chidx, args.points)
    if 'time' not in load_data.keys():
        load_data['time'] = t
    load_data[f'CH{chidx}'] = v

with open(args.output, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(load_data.keys())
    writer.writerows(zip(*load_data.values()))