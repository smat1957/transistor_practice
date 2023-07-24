class Frequency:
    def __init__(self, transistor=1):
        self.transistor = transistor
        Vi_ioc = [0, 2, 4, 6, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        self.Vi_ioc = [Vi_ioc, Vi_ioc, Vi_ioc, Vi_ioc]  # x座標
        Vo_iocM1O = [38.6, 471.8, 851.7, 1249, 1635, 2007, 2861, 3557, 3988, 4275, 4477, 4621, 4729, 4808]
        Vo_iocM1Y = [29, 469.4, 836.1, 1238, 1622, 1990, 2857, 3547, 3982, 4272, 4475, 4624, 4732, 4813]
        Vo_iocM1G = [29.2, 482.1, 852.1, 1251, 1643, 2007, 2888, 3573, 3999, 4285, 4490, 4636, 4746, 4827]
        Vo_iocM1B = [36, 459.1, 837.2, 1215, 1594, 1950, 2797, 3501, 3941, 4238, 4452, 4614, 4727, 4816]
        self.Vo_ioc = [Vo_iocM1O, Vo_iocM1Y, Vo_iocM1G, Vo_iocM1B]
        Hz_frq = [15, 20, 30, 50, 70, 100, 200, 300, 500, 1000, 2000, 5000, 10000, 20000, 50000, 70000, 100000, 150000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
        self.Hz_frq = [Hz_frq, Hz_frq, Hz_frq, Hz_frq]
        Vi_frq = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
        self.Vi_frq = [Vi_frq, Vi_frq, Vi_frq, Vi_frq]
        Vo_frqM1O = [500, 610, 740, 862, 906, 940, 965, 970, 980, 980, 989, 979, 980, 971, 945, 920, 870, 780, 688, 539, 439, 363, 308, 241, 213, 190, 172]
        Vo_frqM1Y = [522, 622, 760, 874, 910, 940, 961, 962, 970, 971, 978, 972, 970, 968, 942, 920, 872, 782, 690, 537, 432, 360, 300, 238, 209, 186, 168]
        Vo_frqM1G = [540, 640, 778, 881, 925, 960, 980, 985, 989, 989, 990, 990, 982, 972, 959, 940, 885, 800, 700, 541, 440, 362, 308, 270, 238, 189, 172]
        Vo_frqM1B = [554, 655, 781, 879, 905, 922, 943, 950, 951, 952, 954, 953, 945, 950, 929, 898, 849, 762, 675, 528, 428, 357, 276, 234, 209, 185, 167]
        self.Vo_frq = [Vo_frqM1O, Vo_frqM1Y, Vo_frqM1G, Vo_frqM1B]

    def getIOC(self, datan=-1):
        if datan<=-1:
            return self.Vi_ioc[self.transistor], self.Vo_ioc[self.transistor]
        else:
            return self.Vi_ioc[datan], self.Vo_ioc[datan]

    def getFRQ(self, datan=-1):
        if datan<=-1:
            return self.Hz_frq[self.transistor], self.Vi_frq[self.transistor], self.Vo_frq[self.transistor]
        else:
            return self.Hz_frq[datan], self.Vi_frq[datan], self.Vo_frq[datan]