class Static:
    def __init__(self, transistor=0):
        self.transistor = transistor
        self.Vce_vccic = [[0.2, 0.4, 0.6, 0.8, 1.0, 2.0, 5.0, 8.0, 10.0],\
                          [0.2, 0.4, 0.6, 0.8, 1.0, 2.0, 5.0, 8.0, 10.0],\
                          [0.2, 0.4, 0.6, 0.8, 1.0, 2.0, 5.0, 8.0, 10.0],\
                          [0.2, 0.4, 0.6, 0.8, 1.0, 2.0, 5.0, 8.0, 10.0]]
        self.Ic20_vccic = [[2.251, 2.398, 2.402, 2.404, 2.408, 2.419, 2.448, 2.477, 2.495],\
                           [3.275, 3.526, 3.537, 3.545, 3.553, 3.600, 3.698, 3.811, 3.879],\
                           [5.218, 5.86, 5.898, 5.922, 5.948, 6.033, 6.302, 6.495, 6.691],\
                           [8.919, 10.684, 10.998, 11.124, 11.19, 11.51, 12.46, 13.41, 14.14]]
        self.Ic40_vccic = [[4.282, 4.755, 4.771, 4.781, 4.791, 4.830, 4.924, 5.011, 5.057],\
                           [6.255, 6.961, 7.016, 7.047, 7.068, 7.189, 7.550, 7.900, 8.148],\
                           [9.108, 11.068, 11.62, 11.7, 11.76, 11.99, 12.75, 13.52, 14.12],\
                           [14.56, 17.98, 19.90, 21.02, 21.66, 22.71, 25.51, 28.32, 29.68]]
        self.Ic60_vccic = [[6.240, 7.033, 7.108, 7.127, 7.143, 7.207, 7.397, 7.585, 7.700],\
                           [8.841, 10.20, 10.45, 10.52, 10.63, 10.98, 11.65, 12.42, 13.06],\
                           [12.26, 15.03, 16.6, 17.24, 17.42, 17.89, 19.36, 20.96, 22.34],\
                           [18.70, 23.04, 25.69, 27.90, 29.44, 32.23, 37.41, 41.66, 43.92]]
        self.Ic80_vccic = [[7.971, 9.165, 9.424, 9.464, 9.495, 9.624, 9.943, 10.240, 10.430],\
                           [11.16, 12.98, 13.60, 13.79, 13.90, 14.32, 15.54, 16.88, 17.79],\
                           [14.98, 18.18, 20.4, 22.02, 22.9, 24.18, 27.11, 30.47, 32.6],\
                           [22.45, 27.13, 30.22, 32.77, 35.13, 41.80, 49.16, 53.90, 56.02]]
        self.Ib_ibic = [[0, 10, 20, 30, 40, 50, 60, 70, 80],\
                        [0, 10, 20, 30, 40, 50, 60, 70, 80],\
                        [0, 10, 20, 30, 40, 50, 60, 70, 80],\
                        [0, 10, 20, 30, 40, 50, 60, 70, 80]]
        self.Ic_ibic = [[0, 1.229, 2.457, 3.691, 4.924, 6.179, 7.427, 8.689, 9.958],\
                        [0, 1.814, 3.679, 5.565, 7.505, 9.453, 11.44, 13.49, 15.50],\
                        [0, 3.098, 6.306, 9.53, 12.84, 16.2, 19.63, 23.1, 26.62],\
                        [0, 6.189, 12.43, 18.64, 24.92, 31.09, 37.26, 42.95, 48.31]]
        self.Vbe_vbeib = [[0.2, 0.3, 0.4, 0.5, 0.6, 0.664, 0.6814, 0.7036, 0.7136],\
                          [0.2, 0.3, 0.4, 0.5, 0.6, 0.6523, 0.6670, 0.6787, 0.6838],\
                          [0.2, 0.3, 0.4, 0.5, 0.6, 0.661, 0.677, 0.697, 0.705],\
                          [0.2, 0.3, 0.4, 0.5, 0.6, 0.6476, 0.6519, 0.6367, 0.6164]]    ##
        self.Ib_vbeib = [[0.01, 0.02, 0.03, 0.10, 1.21, 10.0, 20.0, 50.0, 80.0],\
                         [0.01, 0.02, 0.03, 0.12, 1.48, 10.0, 20.0, 50.0, 80.0],\
                         [0.0, 0.001, 0.01, 0.07, 1.24, 10.0, 20.0, 50.0, 80.0],\
                         [0.01, 0.02, 0.03, 0.11, 1.36, 10.0, 20.0, 50.0, 80.0]]    ##
        self.Vce_loadl = [[9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0],\
                          [9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0],\
                          [9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0],\
                          [9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]]
        self.Ic_loadl = [[0, 2.521, 5.052, 7.616, 10.134, 12.66, 15.22, 17.79, 20.35],\
                         [0, 2.555, 5.057, 7.567, 10.118, 12.65, 15.21, 17.75, 20.30],\
                         [0.0, 2.473, 5.085, 7.511, 10.083, 12.62, 15.18, 17.69, 20.24],\
                         [0.0, 2.489, 5.089, 7.595, 10.144, 12.70, 15.26, 17.83, 20.38]] ##

    def getVceIc(self):
        return self.Vce_vccic[self.transistor], self.Ic20_vccic[self.transistor], self.Ic40_vccic[self.transistor], self.Ic60_vccic[self.transistor], self.Ic80_vccic[self.transistor]

    def getIbIc(self):
        return self.Ib_ibic[self.transistor], self.Ic_ibic[self.transistor]

    def getVbeIb(self):
        return self.Vbe_vbeib[self.transistor], self.Ib_vbeib[self.transistor]

    def getLoadl(self):
        return self.Vce_loadl[self.transistor], self.Ic_loadl[self.transistor]

    def getTrEx01(self, icurr='Ib20'):
        if icurr=='Ib20':
            return  self.Vce_vccic, self.Ic20_vccic
        elif icurr=='Ib40':
            return self.Vce_vccic, self.Ic40_vccic
        elif icurr=='Ib60':
            return self.Vce_vccic, self.Ic60_vccic
        elif icurr=='Ib80':
            return self.Vce_vccic, self.Ic80_vccic

    def getTrEx02(self):
        return  self.Ib_ibic, self.Ic_ibic

    def getTrEx03(self):
        return self.Vbe_vbeib, self.Ib_vbeib

    def getTrEx04(self):
        return self.Vce_loadl, self.Ic_loadl
