from pyecharts.charts import Pie
from pyecharts import options as opts
import pandas as pd

# 渲染图片需要导入以下两个库
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot


data = pd.read_excel('新冠肺炎省份连续零新增天数.xlsx')
provinces = data['省份'].tolist()
numbers = data['天数'].tolist()
colors = data['颜色'].tolist()    # hex value

# 创建饼图（画布宽度、高度（css长度单位））
pie = Pie(init_opts=opts.InitOpts(width='1000px', height='1500px', page_title='Nightingale', bg_color='white'))

# 添加数据（设置饼图半径（内外半径）、圆心坐标（圆心距左侧、上侧距离））（%不能少）
pie.add('', [list(z) for z in zip(provinces, numbers)], radius=['30%', '135%'], center=['50%', '55%'], rosetype='area')
# rosetype：radius——扇区圆心角展现数据的百分比，半径展现数据的大小；area——所有扇区圆心角相同，仅通过半径展现数据大小。

# 设置全局变量（设置标题、不显示图例）pos_left/right/top/bottom
pie.set_global_opts(title_opts=opts.TitleOpts(title='省份连续零新增天数', subtitle='子标题', pos_left='45%'), legend_opts=opts.LegendOpts(is_show=True, pos_top='2%', pos_left='10%', orient='vertical', align='auto'))
# align可选参数: auto/left/right。left/right指图例在文字的左/右侧；auto貌似与right相同。

# 设置系列配置和颜色（设置标签的显示格式、显示位置、字体和大小、饼图颜色等）
pie.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=12, formatter='{b}:{c}天', font_style='italic', font_weight='bold', font_family='Microsoft YaHei'))
pie.set_colors(colors)

# # 在网页生成图片（后面make_snapshot中pie.render()也可以生成html，且()中可指定文件名）
# pie.render('Nightingale.html')

# 输出保存图片
make_snapshot(snapshot, pie.render(), "Nightingale_COVID-19.png", pixel_ratio=10, is_remove_html=False)
# bar.render()里可以指明文件名（必须加后缀.html)，否则默认为render.html。保存路径可以自定义（必须加后缀，且只能为.png)
# 输入图片文件的速度较慢，可以先输出网页，测试成功后，再转成图片
# 经测试，pixel_ratio最多设为24（如果设为25及以上，输出图片大小为0，打不开）（后来发现不同文件，也不一定是24）


# 官方文档
# def make_snapshot(
#     # 渲染引擎，可选 selenium 或者 phantomjs
#     engine: Any,
#
#     # 传入 HTML 文件路径
#     file_name: str,
#
#     # 输出图片路径
#     output_name: str,
#
#     # 延迟时间，避免图还没渲染完成就生成了图片，造成图片不完整
#     delay: float = 2,
#
#     # 像素比例，用于调节图片质量
#     pixel_ratio: int = 2,
#
#     # 渲染完图片是否删除原 HTML 文件
#     is_remove_html: bool = False,
#
#     # 浏览器类型，目前仅支持 Chrome, Safari，使用 snapshot-selenium 时有效
#     browser: str = "Chrome",
#     **kwargs,
# )
