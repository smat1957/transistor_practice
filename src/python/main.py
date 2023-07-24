from quadrant import QuadrantExp
from frequency import FrequencyExp

if __name__ == '__main__':
    transistors1 = ['2SC1815Orange', '2SC1815Yellow', '2SC1815GReen', '2SC1815BLue']
    transistors2 = ['2SC1815O（$h_{FE}=117,\;R_B=83.23k\Omega$）',\
                    '2SC1815Y（$h_{FE}=176,\;R_B=85.83k\Omega$）',\
                    '2SC1815GR（$h_{FE}=260,\;R_B=87.42k\Omega$）',\
                    '2SC1815BL（$h_{FE}=593,\;R_B=90.78k\Omega$）']
    # Static Character
    transistor = 0
    q = QuadrantExp(transistor, transistors1[transistor])
    p = q.experiment()
    p.savefig('static'+str(transistor)+'.png')
    p.show()
    #
    Ib='Ib40'
    p = q.experiment01( Ib )
    p.savefig('staticE01'+Ib+'.png')
    p.show()
    p = q.experiment02()
    p.savefig('staticE02.png')
    p.show()
    p = q.experiment03()
    p.savefig('staticE03.png')
    p.show()
    p = q.experiment04()
    p.savefig('staticE04.png')
    p.show()
    #
    # Input-Output Character
    transistor = 0
    f = FrequencyExp(transistor, transistors2[transistor], True)
    p = f.ioexperiment(transistor)
    p.savefig('iochar'+str(transistor)+'.png')
    p.show()
    # Frequency Character
    p = f.freqexperiment(transistor)
    p.savefig('freqchar'+str(transistor)+'.png')
    p.show()
