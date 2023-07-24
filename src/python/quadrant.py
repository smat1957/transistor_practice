import numpy as np
from interpolate import Interpolate
import matplotlib.pyplot as plt
from data_static import Static

class QuadrantExp:
    def __init__(self, transistor=0, name='2SC1815GReen'):
        self.data = Static(transistor)
        self.name = name
        self.markers = [".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8",
                        "s", "p", "*", "h", "H", "+", "x", "D", "d", "|", "_",
                        "None", None, "", "$x$", "$\\alpha$", "$\\beta$", "$\\gamma$"]
        plt.rcParams['font.family'] = "Hiragino Maru Gothic Pro"
        plt.figure(figsize=(14, 8), dpi=100)
        plt.subplots_adjust(wspace=0.2, hspace=0.3)
        plt.get_current_fig_manager().canvas.set_window_title(self.name + ' : 静特性')
        self.ip = Interpolate()

    def experiment(self):
        self.experiment1()
        self.experiment2()
        self.experiment3()
        return plt

    def experiment1(self):
        Vce, Ic20, Ic40, Ic60, Ic80 = self.data.getVceIc()
        VceL, IcL = self.data.getLoadl()
        ax1 = plt.subplot(2, 2, 2)
        ax1.grid(True)
        ax1.set_xlim(0, 10)
        #ax1.set_ylim(0, 35)
        ax1.set_title('$V_{CE}$ - $I_C$ 特性＝出力特性（$I_B$ 一定）/ 直流負荷線（$E_C=9$V; $R_C=390\Omega$）')
        ax1.set_xlabel('コレクターエミッタ間電圧 $V_{CE}$[V]')
        ax1.set_ylabel('コレクタ電流 $I_C$[mA]')
        ax1.plot(Vce, Ic20, label='$I_B=20\;\mu$A', marker=self.markers[0])
        ax1.plot(Vce, Ic40, label='$I_B=40\;\mu$A', marker=self.markers[14])
        ax1.plot(Vce, Ic60, label='$I_B=60\;\mu$A', marker=self.markers[17])
        ax1.plot(Vce, Ic80, label='$I_B=80\;\mu$A', marker=self.markers[18])
        ax1.legend(loc='upper right')
        ax1.plot(VceL, IcL, label='Ec=9V,Rc=390$\Omega$', marker=self.markers[4])

    def experiment2(self):
        Ib, Ic = self.data.getIbIc()
        ax2 = plt.subplot(2, 2, 1)
        ax2.set_xlim(0, max(Ib)) #80
        #ax2.set_ylim(0, 35)
        ax2.grid(True)
        ax2.invert_xaxis()
        ax2.set_title('$I_B$ - $I_C$ 特性（$V_{CE}=5$V 一定）')
        ax2.set_xlabel('ベース電流 $I_B$[$\mu$A]')
        ax2.set_ylabel('コレクタ電流 $I_C$[mA]')
        ax2.scatter(Ib, Ic,label="observed")
        ax2.plot(Ib, Ic, label='$V_{CE}=5$V')

    def experiment3(self):
        Vbe, Ib = self.data.getVbeIb()
        ax3 = plt.subplot(2, 2, 3)
        ax3.set_xlim(0, max(Ib))   #80.0
        #ax3.set_ylim(0, 0.8)
        ax3.grid(True)
        ax3.invert_yaxis()
        ax3.invert_xaxis()
        ax3.set_title('$V_{BE}$ - $I_B$ 特性=入力特性（$V_{CE}=5$V 一定）')
        ax3.set_ylabel('ベースーエミッタ間電圧 $V_{BE}$[V]')
        ax3.set_xlabel('ベース電流 $I_B$[$\mu$A]')
        _, method = self.ip.getMethod(9)
        x_latent = np.linspace(min(Ib), max(Ib), 100)
        fitted_curve = method(Ib, Vbe)
        ax3.scatter(Ib, Vbe, label="observed")
        ax3.plot(x_latent, fitted_curve(x_latent), c="red", label="fitted")

    def experiment01(self, Ib = 'Ib40'):
        ttl=''
        if Ib == 'Ib20':
            ttl = '$20\;\mu A\;$'
        elif Ib == 'Ib40':
            ttl = '$40\;\mu A\;$'
        elif Ib == 'Ib60':
            ttl = '$60\;\mu A\;$'
        elif Ib == 'Ib80':
            ttl = '$80\;\mu A\;$'
        Vce, Tr = self.data.getTrEx01(Ib)
        # サブプロットを描画する領域を作成
        fig = plt.figure(figsize=(14, 8), dpi=100)
        # figにAxesを１つ追加
        ax4 = fig.add_subplot(111)
        ax4.grid(True)
        ax4.set_xlim(0, max(Vce[0]))   #10
        #ax4.set_ylim(0, 35)
        ax4.set_title('$V_{CE}$ - $I_C$ 特性＝出力特性（$I_B=$'+ttl+'一定）')
        ax4.set_xlabel('コレクターエミッタ間電圧 $V_{CE}$[V]')
        ax4.set_ylabel('コレクタ電流 $I_C$[mA]')
        for i in range(4):
            mylabel=''
            if i==0:
                mylabel = '2SC1815-O'
            elif i==1:
                mylabel = '2SC1815-Y'
            elif i==2:
                mylabel = '2SC1815-GR'
            elif i==3:
                mylabel = '2SC1815-BL'
            ax4.scatter(Vce[i], Tr[i], marker=self.markers[i+1])
            ax4.plot(Vce[i], Tr[i], label=mylabel, marker=self.markers[i+1])
        ax4.legend(loc='upper right')
        return plt

    def experiment02(self):
        Ib, Tr = self.data.getTrEx02()
        # サブプロットを描画する領域を作成
        fig = plt.figure(figsize=(14, 8), dpi=100)
        # figにAxesを１つ追加
        ax5 = fig.add_subplot(111)
        ax5.set_xlim(0, max(Ib[0])) #80
        #ax5.set_ylim(0, 35)
        ax5.grid(True)
        #ax5.invert_xaxis()
        ax5.set_title('$I_B$ - $I_C$ 特性（$V_{CE}=5$V 一定）')
        ax5.set_xlabel('ベース電流 $I_B$[$\mu$A]')
        ax5.set_ylabel('コレクタ電流 $I_C$[mA]')
        for i in range(4):
            mylabel=''
            if i==0:
                mylabel = '2SC1815-O'
            elif i==1:
                mylabel = '2SC1815-Y'
            elif i==2:
                mylabel = '2SC1815-GR'
            elif i==3:
                mylabel = '2SC1815-BL'
            ax5.scatter(Ib[i], Tr[i], marker=self.markers[i+1])
            ax5.plot(Ib[i], Tr[i], label=mylabel, marker=self.markers[i+1])
        ax5.legend(loc='upper left')
        return plt

    def experiment03(self):
        Vbe, Tr = self.data.getTrEx03()
        # サブプロットを描画する領域を作成
        fig = plt.figure(figsize=(14, 8), dpi=100)
        # figにAxesを１つ追加
        ax6 = fig.add_subplot(111)
        #ax6.set_xlim(0, max(Vbe[0]))   # 80.0
        #ax6.set_ylim(0, 0.8)
        ax6.grid(True)
        #ax6.invert_yaxis()
        #ax6.invert_xaxis()
        ax6.set_title('$V_{BE}$ - $I_B$ 特性=入力特性（$V_{CE}=5$V 一定）')
        ax6.set_ylabel('ベースーエミッタ間電圧 $V_{BE}$[V]')
        ax6.set_xlabel('ベース電流 $I_B$[$\mu$A]')
        _, method = self.ip.getMethod(9)
        for i in range(4):
            mylabel=''
            if i==0:
                mylabel = '2SC1815-O'
            elif i==1:
                mylabel = '2SC1815-Y'
            elif i==2:
                mylabel = '2SC1815-GR'
            elif i==3:
                mylabel = '2SC1815-BL'
            #x_latent = np.linspace(min(Vbe[i]), max(Vbe[i]), 100)
            #fitted_curve = method(Vbe[i], Tr[i])
            ax6.scatter(Vbe[i], Tr[i], marker=self.markers[i+1])
            #ax6.plot(x_latent, fitted_curve(x_latent), label=mylabel)
            ax6.plot(Vbe[i], Tr[i], label=mylabel, marker=self.markers[i+1])
        ax6.legend(loc='upper left')
        return plt

    def experiment04(self):
        VceL, Tr = self.data.getTrEx04()
        # サブプロットを描画する領域を作成
        fig = plt.figure(figsize=(14, 8), dpi=100)
        # figにAxesを１つ追加
        ax7 = fig.add_subplot(111)
        ax7.grid(True)
        ax7.set_xlim(0, max(VceL[0]))   #10
        #ax7.set_ylim(0, 35)
        ax7.set_title('直流負荷線（$E_C=9V; R_C=390\Omega$）')
        ax7.set_xlabel('コレクターエミッタ間電圧 $V_{CE}$[V]')
        ax7.set_ylabel('コレクタ電流 $I_C$[mA]')
        for i in range(4):
            mylabel=''
            if i==0:
                mylabel = '2SC1815-O'
            elif i==1:
                mylabel = '2SC1815-Y'
            elif i==2:
                mylabel = '2SC1815-GR'
            elif i==3:
                mylabel = '2SC1815-BL'
            ax7.scatter(VceL[i], Tr[i], marker=self.markers[i+1])
            ax7.plot(VceL[i], Tr[i], label=mylabel, marker=self.markers[i+1])
        ax7.legend(loc='upper right')
        return plt
