import matplotlib
import matplotlib.pyplot as plt

class FontCheck:
    def __init__(self):
        # フォントを全て読み込み
        fonts = set([f.name for f in matplotlib.font_manager.fontManager.ttflist])
        print(fonts)
        # 描画領域のサイズ調整
        plt.figure(figsize=(10, len(fonts) / 4))
        # フォントの表示
        for i, font in enumerate(fonts):
            plt.text(0, i, f"日本語：{font}", fontname=font)
