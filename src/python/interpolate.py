import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

class Interpolate:
    ip1 = ["最近傍点補間", lambda x, y: interpolate.interp1d(x, y, kind="nearest")]
    ip2 = ["線形補間", interpolate.interp1d]
    ip3 = ["ラグランジュ補間", interpolate.lagrange]
    ip4 = ["重心補間", interpolate.BarycentricInterpolator]
    ip5 = ["Krogh補間", interpolate.KroghInterpolator]
    ip6 = ["2次スプライン補間", lambda x, y: interpolate.interp1d(x, y, kind="quadratic")]
    ip7 = ["3次スプライン補間", lambda x, y: interpolate.interp1d(x, y, kind="cubic")]
    ip8 = ["秋間補間", interpolate.Akima1DInterpolator]
    ip9 = ["区分的 3 次エルミート補間", interpolate.PchipInterpolator]

    def __init__(self):
        self.ips = [self.ip1, self.ip2, self.ip3, self.ip4, self.ip5, self.ip6, self.ip7, self.ip8, self.ip9]
        self.ip = self.ip9

    def demo(self):
        x_observed = [9, 28, 38, 58, 88, 98, 108, 118, 128, 138, 148, 158, 168, 178, 188, 198, 208, 218, 228, 238, 278, 288, 298]
        y_observed = [51, 80, 112, 294, 286, 110, 59, 70, 56, 70, 104, 59, 59, 72, 87, 99, 64, 60, 74, 151, 157, 57, 83]
        x_latent = np.linspace(min(x_observed), max(x_observed), 100)
        for method_name, method in [self.ip1, self.ip2, self.ip3, self.ip4, self.ip5, self.ip6, self.ip7, self.ip8, self.ip9]:
            print(method_name)
            fitted_curve = method(x_observed, y_observed)
            plt.scatter(x_observed, y_observed, label="observed")
            plt.plot(x_latent, fitted_curve(x_latent), c="red", label="fitted")
            plt.grid()
            plt.legend()
            plt.show()

    def getMethod(self, id):
        return self.ips[id-1]
