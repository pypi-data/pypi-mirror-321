import matplotlib.pyplot as plt
import matplotlib as mpl

def set_math_font_italic(italic=True):
    """
    设置全局公式是否斜体。

    参数:
    italic (bool): 如果为 True，全局公式为斜体；如果为 False，全局公式不为斜体。
    """
    if italic:
        # 设置为斜体
        mpl.rcParams['mathtext.default'] = 'it'  # 默认斜体
    else:
        # 设置为非斜体
        mpl.rcParams['mathtext.default'] = 'regular'  # 默认非斜体


def set_global_font(font_family='sans-serif', font_name='Microsoft YaHei', font_size=12, font_weight='normal'):
    """
    设置 matplotlib 全局字体样式。

    参数:
        font_family (str): 字体族，例如 'sans-serif', 'serif', 'monospace' 等。
        font_name (str): 具体字体名称，例如 'Microsoft YaHei', 'Times New Roman', 'Arial' 等。
        font_size (int): 字体大小，默认 12。
        font_weight (str): 字体粗细，例如 'normal', 'bold', 'light' 等。
    """
    # 设置全局字体族
    plt.rcParams['font.family'] = font_family
    # 设置全局字体名称
    plt.rcParams['font.sans-serif'] = [font_name]
    # 设置全局字体大小
    plt.rcParams['font.size'] = font_size
    # 设置全局字体粗细
    plt.rcParams['font.weight'] = font_weight
    # 设置数学公式字体
    plt.rcParams['mathtext.fontset'] = 'stix'  # 可选 'stix', 'cm', 'dejavusans' 等

    print(f"全局字体已设置为: {font_name}, 大小: {font_size}, 粗细: {font_weight}")


def initialize_matplotlib(fontname='DejaVu Sans', formula_italic=False, ticks_fontsize=12, title_fontsize=14, text_fontsize=12):
    """
    初始化 matplotlib 的全局设置。

    参数:
    - fontname: str, 字体名称，默认为 'DejaVu Sans'
    - formula_italic: bool, 公式是否斜体，默认为 False
    - ticks_fontsize: int, 刻度字体大小，默认为 12
    - title_fontsize: int, 标题字体大小，默认为 14
    - text_fontsize: int, 普通文本字体大小，默认为 12
    """
    # 设置全局字体
    plt.rcParams['font.family'] = fontname

    # 设置公式是否斜体
    plt.rcParams['mathtext.default'] = 'it' if formula_italic else 'regular'

    # 设置刻度字体大小
    plt.rcParams['xtick.labelsize'] = ticks_fontsize
    plt.rcParams['ytick.labelsize'] = ticks_fontsize

    # 设置标题字体大小
    plt.rcParams['axes.titlesize'] = title_fontsize

    # 设置普通文本字体大小
    plt.rcParams['font.size'] = text_fontsize

    # 设置坐标轴标签字体大小（可选）
    plt.rcParams['axes.labelsize'] = ticks_fontsize + 1  # 标签字体稍大

