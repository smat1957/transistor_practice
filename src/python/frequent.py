import math
import matplotlib.pyplot as plt
from data_freq import Frequency

class Frequent:
    def __init__(self, transistor=0):
        self.data = Frequency(transistor)
        Hz, Vi, Vo = self.data.getFRQ()
        self.Av = [x / Vi for x in Vo]
        self.Gv = [20.0 * math.log10(x) for x in self.Av]

    def ioexperiment(self):
        self.iochar()
        return plt

    def freqexperiment(self):
        self.freqchar();
        return plt

    def iochar(self):
        # Input/Output Characteristics
        Vi, Vo = self.data.getIOC()
        plt.figure(figsize=(14, 8), dpi=100)
        plt.scatter(Vi, Vo, label="observed")
        plt.plot(Vi, Vo, color="r")
        plt.title('2SC1815Y : 入出力特性（周波数 f=1kHz 一定）')
        plt.xlabel('入力電圧 Vi[mV]', fontsize=18)
        plt.ylabel('出力電圧 Vo[mV]', fontsize=18)
        plt.grid(which="both")  # "both"はxy軸両方にグリッド
        plt.get_current_fig_manager().canvas.set_window_title('2SC1815Y : 低周波増幅特性')

    def gvab(self):
        GvA = max(self.Gv)
        GvB = GvA - 3
        return GvA, GvB

    def crossp(self, GvB):
        Hz, Vi, Vo = self.data.getFRQ()
        # 交点の座標(hz1, GvB),(hz2, GvB)を取得
        for i in range(len(self.Gv) - 1):
            left = i
            right = i + 1
            if self.Gv[left] <= GvB <= self.Gv[right]:
                rate = (GvB - self.Gv[left]) / (self.Gv[right] - self.Gv[left])
                hz1 = rate * (Hz[right] - Hz[left]) + Hz[left]
            if self.Gv[left] >= GvB >= self.Gv[right]:
                rate = (GvB - self.Gv[right]) / (self.Gv[left] - self.Gv[right])
                hz2 = Hz[right] - rate * (Hz[right] - Hz[left])
        return hz1, hz2

    def freqchar(self):
        # Frequancy Characteristics
        Hz, Vi, Vo = self.data.getFRQ()
        GvA, GvB = self.gvab()
        print(f"Max of Gv(=GvA) : {GvA}[dB],\t GvA-3(=GvB) : {GvB}[dB]")
        plt.figure(figsize=(14, 8), dpi=100)
        plt.scatter(Hz, self.Gv, label="observed")
        plt.plot(Hz, self.Gv, color="r")
        hz1, hz2 = self.crossp(GvB)
        B = hz2 - hz1
        print(f"低域遮断周波数（fL）＝{hz1:.3f}[Hz]\t高域遮断周波数（fH）＝{hz2:.3f}[Hz]\t周波数帯域幅（B）＝{B:.3f}[Hz]")
        # 交点をグラフにプロット
        plt.plot(hz1, GvB, 'ms', ms=5, label='Intersection', color='green')
        plt.text(hz1 + 50, GvB - 1, '({x:.2f}, {y:.2f})'.format(x=hz1, y=GvB), fontsize=10)
        plt.plot(hz2, GvB, 'ms', ms=5, label='Intersection', color='green')
        plt.text(hz2 + 1500, GvB + 1, '({x:.2f}, {y:.2f})'.format(x=hz2, y=GvB), fontsize=10)
        plt.text(hz1 + 150, GvB - 15, '低域遮断周波数：{x:7.2f}[Hz]'.format(x=hz1), fontsize=10)
        plt.text(hz1 + 150, GvB - 17, '高域遮断周波数：{y:7.2f}[Hz]'.format(y=hz2), fontsize=10)
        plt.text(hz1 + 150, GvB - 19, '周波数帯域　　：{z:7.2f}[Hz]'.format(z=B), fontsize=10)
        plt.hlines(GvB, min(Hz), max(Hz), color="b", label="GvB=GvA-3")
        plt.vlines(hz1, min(self.Gv), max(self.Gv), color="b")
        plt.vlines(hz2, min(self.Gv), max(self.Gv), color="b")
        #
        ax = plt.gca()
        ax.spines['top'].set_color('none')
        ax.set_xscale('log')  # x軸をlogスケールで
        plt.title('2SC1815Y : 周波数特性')
        plt.xlabel('周波数 f[Hz]', fontsize=18)
        plt.ylabel('電圧利得 Gv[dB]', fontsize=18)
        plt.grid(which="both")
        plt.get_current_fig_manager().canvas.set_window_title('2SC1815Y : 低周波増幅特性')
