import math
import matplotlib.pyplot as plt
from data_freq import Frequency

class FrequencyExp:
    def __init__(self, transistor=0, name='2SC1815Yellow', flag=True):
        self.data = Frequency(transistor)
        self.name = name
        self.flag = flag
        self.markers = [".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8",
                        "s", "p", "*", "h", "H", "+", "x", "D", "d", "|", "_",
                        "None", None, "", "$x$", "$\\alpha$", "$\\beta$", "$\\gamma$"]

    def ioexperiment(self, datan=-1):
        self.iochar()
        return plt

    def freqexperiment(self, datan=-1):
        self.freqchar(datan)
        return plt

    def iochar(self):
        # Input/Output Characteristics
        Vi, Vo = self.data.getIOC()
        plt.figure(figsize=(14, 8), dpi=100)
        plt.scatter(Vi, Vo, label="observed")
        plt.plot(Vi, Vo, color="r")
        plt.title(self.name + ' : 入出力特性（周波数 f=1kHz 一定）')
        plt.xlabel('入力電圧 Vi[mV]', fontsize=14)
        plt.ylabel('出力電圧 Vo[mV]', fontsize=14)
        plt.grid(which="both")  # "both"はxy軸両方にグリッド
        plt.get_current_fig_manager().canvas.set_window_title(self.name + ' : 低周波増幅特性')

    def gvab(self, Vi, Vo):
        self.Av = []
        self.Gv = []
        for i, x in enumerate(Vo):
            y = x / Vi[i]
            self.Av.append( y )
            self.Gv.append( 20.0 * math.log10(y) )
        GvA = max(self.Gv)
        GvB = GvA - 3
        return GvA, GvB

    def crossp(self, GvB, Hz):
        # 交点の座標(hz1, GvB),(hz2, GvB)を取得
        hz1 = hz2 = 0
        for i in range(len(self.Gv) - 1):
            left = i
            right = i + 1
            if self.Gv[left] <= GvB <= self.Gv[right]:
                rate = (GvB - self.Gv[left]) / (self.Gv[right] - self.Gv[left])
                hz1 = rate * (Hz[right] - Hz[left]) + Hz[left]
            if self.Gv[left] >= GvB >= self.Gv[right]:
                rate = (GvB - self.Gv[right]) / (self.Gv[left] - self.Gv[right])
                hz2 = Hz[right] - rate * (Hz[right] - Hz[left])
        return hz1, hz2, hz2 - hz1

    def plot_lines(self, Hz, GvB, hz1, hz2, lbl='', markn=2):
        if self.flag:
            plt.plot(Hz, self.Gv, color='r', marker=self.markers[markn])
        else:
            plt.plot(Hz, self.Gv, label=lbl, marker=self.markers[markn])
            plt.legend(loc='upper left')
        # 交点をグラフにプロット
        plt.plot(hz1, GvB, 'ms', ms=5, label='_nolegend', color='green')
        if self.flag:
            plt.text(hz1 * 1.1, GvB - 2, '({x:.2f}, {y:.2f})'.format(x=hz1, y=GvB), fontsize=10)
        plt.hlines(GvB, min(Hz), max(Hz), color="b", label='_nolegend')
        plt.vlines(hz1, min(self.Gv), max(self.Gv), color="b", label='_nolegend')
        if hz2>0:
            plt.plot(hz2, GvB, 'ms', ms=5, label='_nolegend', color='green')
            if self.flag:
                plt.text(hz2 * 1.1, GvB + 1, '({x:.2f}, {y:.2f})'.format(x=hz2, y=GvB), fontsize=10)
            plt.vlines(hz2, min(self.Gv), max(self.Gv), color="b",label='_nolegend')

    def freqchar(self, datan):
        # Frequency Characteristics
        plt.figure(figsize=(14, 8), dpi=100)
        if self.flag:
            Hz, Vi, Vo = self.data.getFRQ(datan)
            GvA, GvB = self.gvab(Vi, Vo)
            #print(f"Max of Gv(=GvA) : {GvA}[dB],\t GvA-3(=GvB) : {GvB}[dB]")
            hz1, hz2, B = self.crossp(GvB, Hz)
            #print(f"低域遮断周波数（fL）＝{hz1:.3f}[Hz]\t高域遮断周波数（fH）＝{hz2:.3f}[Hz]\t周波数帯域幅（B）＝{B:.3f}[Hz]")
            self.plot_lines(Hz, GvB, hz1, hz2)
        else:
            Hz, Vi, Vo = self.data.getFRQ(datan=17)
            GvA, GvB = self.gvab(Vi, Vo)
            hz1, hz2, B = self.crossp(GvB, Hz)
            self.plot_lines(Hz, GvB, hz1, hz2, lbl='Orange', markn=0)

            Hz, Vi, Vo = self.data.getFRQ(datan=18)
            GvA, GvB = self.gvab(Vi, Vo)
            hz1, hz2, B = self.crossp(GvB, Hz)
            self.plot_lines(Hz, GvB, hz1, hz2, lbl='Yellow', markn=3)

            Hz, Vi, Vo = self.data.getFRQ(datan=15)
            GvA, GvB = self.gvab(Vi, Vo)
            hz1, hz2, B = self.crossp(GvB, Hz)
            self.plot_lines(Hz, GvB, hz1, hz2, lbl='GReen', markn=5)

            Hz, Vi, Vo = self.data.getFRQ(datan=16)
            GvA, GvB = self.gvab(Vi, Vo)
            hz1, hz2, B = self.crossp(GvB, Hz)
            self.plot_lines(Hz, GvB, hz1, hz2, lbl='BLue', markn=2)

        if self.flag:
            y = ( max(self.Gv)-min(self.Gv) ) / 2 + min(self.Gv)
            plt.text(hz1 * 2.0, y - 2, '低域遮断周波数：{x:13,.2f} [Hz]'.format(x=hz1), fontsize=10)
            if hz2>0:
                plt.text(hz1 * 2.0, y,     '高域遮断周波数：{y:10,.2f} [Hz]'.format(y=hz2), fontsize=10)
                plt.text(hz1 * 2.0, y - 4, '周波数帯域　　：{z:10,.2f} [Hz]'.format(z=B), fontsize=10)
        #
        ax = plt.gca()
        ax.spines['top'].set_color('none')
        ax.set_xscale('log')  # x軸をlogスケールで
        if not self.flag:
            self.name = '2SC1815Y(B回路、Re=23, 24, 25, 27, 30, 40, 56Ω)'
        plt.title(self.name + ' : 周波数特性')
        plt.xlabel('周波数 f[Hz]', fontsize=14)
        plt.ylabel('電圧利得 Gv[dB]', fontsize=14)
        plt.grid(which="both")
        plt.get_current_fig_manager().canvas.set_window_title(self.name + ' : 低周波増幅特性')
