from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot


def bar_chart() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
        .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )
    return c


bar_chart().render('def.html')

make_snapshot(snapshot, bar_chart().render(), "bar0.png", is_remove_html=True)






from pyecharts.charts import Bar
from pyecharts import options as opts

from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts.globals import ThemeType

# 创建一个柱状图Bar实例
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        # 添加X轴数据
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        # 添加Y轴数据,系列的名称
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("商家B", [8, 15, 60, 20, 25, 30])
        # 添加标题
        .set_global_opts(title_opts=opts.TitleOpts(title="主标题: 双十一销量", subtitle="副标题:服饰类"))
        # 或者直接使用字典参数（key必须是text、subtext）
        # .set_global_opts(title_opts={"text": "主标题: 双十一销量", "subtext": "副标题:服饰类"})
)

bar.render('theme.html')

# # 输出保存为图片
# make_snapshot(snapshot, bar.render(), "sstest20.png", pixel_ratio=20, is_remove_html=True)
