#!/bin/bash
python3 load_screen.py -a TCPIP::${2:-169.254.137.4}::INSTR -o ${1:-testscreen}.png
##### python3 load_screen.py -a TCPIP::169.254.137.4::INSTR -o test1.png