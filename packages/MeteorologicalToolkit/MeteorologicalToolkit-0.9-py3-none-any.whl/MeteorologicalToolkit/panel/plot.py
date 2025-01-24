import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

from matplotlib.colors import BoundaryNorm
from matplotlib import colorbar as cbar
from scipy.interpolate import griddata


def imshowm(ax, lon, lat, data, levels=None, cmap=None, vmin=None, vmax=None):
    """
    在给定的 ax 上绘制带 levels 的填色图。

    参数:
    ax (matplotlib.axes.Axes): 目标 Axes 对象。
    lon (numpy.ndarray): 经度数组，形状为 (nlon,) 或 (nlat, nlon)。
    lat (numpy.ndarray): 纬度数组，形状为 (nlat,) 或 (nlat, nlon)。
    data (numpy.ndarray): 数据数组，形状为 (nlat, nlon)。
    levels (list or int, optional): 等值线层级。如果是整数，表示等值线数量；如果是列表，表示具体的等值线值。
    cmap (str or matplotlib.colors.Colormap, optional): 颜色映射。

    返回:
    im (matplotlib.collections.QuadMesh): 填色图对象。
    """
    # 确保 lon 和 lat 是二维数组
    if lon.ndim == 1 and lat.ndim == 1:
        lon, lat = np.meshgrid(lon, lat)  # 将一维经纬度转换为二维网格

    # 获取 ax 的投影
    projection = ax.projection

    if vmin == None:
        vmin = np.min(levels)
    if vmax == None:
        vmax = np.max(levels)

    # 绘制填色图
    im = ax.pcolormesh(lon, lat, data, cmap=cmap, transform=ccrs.PlateCarree(), vmin=vmin, vmax=vmax)

    return ax, im


# def imshowm(ax, lon, lat, data, cmap=None, vmin=None, vmax=None, extend='neither'):
#     """
#     在给定的 ax 上绘制填色图（使用 imshow）。
#
#     参数:
#     ax (matplotlib.axes.Axes): 目标 Axes 对象。
#     lon (numpy.ndarray): 经度数组，形状为 (nlon,) 或 (nlat, nlon)。
#     lat (numpy.ndarray): 纬度数组，形状为 (nlat,) 或 (nlat, nlon)。
#     data (numpy.ndarray): 数据数组，形状为 (nlat, nlon)。
#     cmap (str or matplotlib.colors.Colormap, optional): 颜色映射。
#     vmin (float, optional): 数据的最小值，用于颜色映射。
#     vmax (float, optional): 数据的最大值，用于颜色映射。
#     extend (str, optional): 扩展选项，可以是 'neither', 'both', 'min', 或 'max'。
#
#     返回:
#     im (matplotlib.image.AxesImage): 图像对象。
#     """
#     # 确保 lon 和 lat 是二维数组
#     if lon.ndim == 1 and lat.ndim == 1:
#         lon, lat = np.meshgrid(lon, lat)  # 将一维经纬度转换为二维网格
#
#     # 计算图像的边界 (extent)
#     extent = [lon.min(), lon.max(), lat.min(), lat.max()]
#
#     # 绘制图像
#     im = ax.imshow(data, extent=extent, cmap=cmap, vmin=vmin, vmax=vmax,
#                    origin='lower', transform=ccrs.PlateCarree())
#
#     # 添加颜色条并设置 extend
#     cbar = plt.colorbar(im, ax=ax, orientation='horizontal', extend=extend)
#
#     return im



def colorbar(im, ax, position=None, shrink=0.7, ticks=None, orientation='horizontal', fontname=None, label=None, tickwidth=1, edgesize=1, ticklen=11, tickin=False, aspect=50, fontsize=12, yshift=0, labelloc='right', x_label_move=0, y_label_move=0):
    """
    为填色图添加颜色条。

    参数:
    im (matplotlib.collections.QuadMesh): 填色图对象（imshowm 返回的对象）。
    ax (matplotlib.axes.Axes): 目标 Axes 对象。
    position (list): 颜色条的位置和大小 [left, bottom, width, height]，默认为右侧。
    shrink (float): 颜色条的缩放比例（仅在 position 为 None 时生效）。
    ticks (list): 颜色条的刻度值。如果为 None，则自动生成刻度。
    orientation (str): 颜色条的方向，支持 'horizontal' 或 'vertical'。
    fontname (str): 刻度标签和标题的字体名称。
    label (str): 颜色条的标题。
    tickwidth (float): 刻度线的宽度。
    edgesize (float): 颜色条边框的宽度。
    ticklen (float): 刻度线的长度。
    tickin (bool): 刻度线是否朝向颜色条内部。
    aspect (float): 颜色条的纵横比。
    fontsize (int): 刻度标签和标题的字体大小。
    yshift (float): 标题的垂直偏移量（仅适用于水平颜色条）。
    labelloc (str): 标题的位置，支持 'left', 'right', 'top', 'bottom'。
    x_label_move (float): 标题在水平方向上的偏移量（仅适用于垂直颜色条）。
    y_label_move (float): 标题在垂直方向上的偏移量（仅适用于水平颜色条）。

    返回:
    cbar (matplotlib.colorbar.Colorbar): 颜色条对象。
    """
    # 如果未指定 position，则使用默认位置
    if position is None:
        bbox = ax.get_position()  # 获取 ax 的位置
        if orientation == 'horizontal':
            position = [bbox.x0, bbox.y0 - 0.04, bbox.width * shrink, 0.02]  # 底部
        else:
            position = [bbox.x1 + 0.02, bbox.y0, 0.02, bbox.height * shrink]  # 右侧

    # 创建颜色条的 Axes
    cax = ax.figure.add_axes(position)

    # 创建颜色条
    cb = plt.colorbar(im, cax=cax, orientation=orientation, ticks=ticks, aspect=aspect)

    # 设置刻度线
    cb.ax.tick_params(width=tickwidth, length=ticklen, direction='in' if tickin else 'out')

    # 关闭小刻度线
    cb.ax.minorticks_off()

    # 设置边框
    for spine in cb.ax.spines.values():
        spine.set_linewidth(edgesize)

    # 设置刻度标签
    if fontname:
        for l in cb.ax.get_xticklabels() + cb.ax.get_yticklabels():
            l.set_fontname(fontname)
            l.set_fontsize(fontsize)

    # 设置标题
    if label:
        if orientation == 'horizontal':
            # 水平颜色条的标题：y_label_move 对应 labelpad
            cb.set_label(label, fontname=fontname, fontsize=fontsize, labelpad=yshift + y_label_move, loc=labelloc)
            # x_label_move 调整水平位置
            label_obj = cb.ax.get_xaxis().label
            label_obj.set_position((label_obj.get_position()[0] + x_label_move, label_obj.get_position()[1]))
        else:
            # 垂直颜色条的标题：x_label_move 对应 labelpad
            cb.set_label(label, fontname=fontname, fontsize=fontsize, labelpad=yshift + x_label_move, loc=labelloc)
            # y_label_move 调整垂直位置
            label_obj = cb.ax.get_yaxis().label
            label_obj.set_position((label_obj.get_position()[0], label_obj.get_position()[1] + y_label_move))

    return cb



def scatter_density(ax, x, y, start_value, end_value, grid_num=100, cmap='viridis', vmin=None, vmax=None):
    """
    使用 pcolormesh 绘制散点密度图，统计每个网格中的样本数量
    :param ax: matplotlib的Axes对象，用于绘图
    :param x: x轴数据
    :param y: y轴数据
    :param start_value: 绘图范围的起始值
    :param end_value: 绘图范围的结束值
    :param grid_num: 网格数量，默认为100
    :param cmap: 颜色映射，默认为'viridis'
    :param vmin: 颜色映射的最小值
    :param vmax: 颜色映射的最大值
    """
    # 生成网格数据

    x = x.squeeze()
    y = y.squeeze()

    x_edges = np.linspace(start_value, end_value, grid_num + 1)
    y_edges = np.linspace(start_value, end_value, grid_num + 1)

    # 统计每个网格中的样本数量
    hist, x_edges, y_edges = np.histogram2d(x, y, bins=[x_edges, y_edges])

    # 网格中心点
    x_centers = (x_edges[:-1] + x_edges[1:]) / 2
    y_centers = (y_edges[:-1] + y_edges[1:]) / 2
    grid_x, grid_y = np.meshgrid(x_centers, y_centers)

    # 使用 pcolormesh 绘制密度图
    mesh = ax.pcolormesh(grid_x, grid_y, hist.T, cmap=cmap, shading='auto', vmin=vmin, vmax=vmax)

    # 绘制对角线
    diagonal = np.linspace(start_value, end_value, grid_num)
    ax.plot(diagonal, diagonal, 'k--', linewidth=2)

    # 设置图形属性
    ax.set_xlim(start_value, end_value)
    ax.set_ylim(start_value, end_value)
    ax.set_xlabel('X values')
    ax.set_ylabel('Y values')

    return ax, mesh


# 示例使用
if __name__ == "__main__":
    # 创建画布和子图
    fig, ax = plt.subplots(figsize=(10, 8))

    # 示例数据
    x = np.random.normal(100, 20, 1000)
    y = x + np.random.normal(0, 10, 1000)

    # 调用函数
    scatter_density(ax, x, y, start_value=0, end_value=300, grid_num=100, cmap='plasma', vmin=0, vmax=20)

    # 显示图形
    plt.show()



