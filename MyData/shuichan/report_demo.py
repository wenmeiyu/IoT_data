# encoding: utf-8
from __future__ import unicode_literals
from pyecharts import Bar
from pyecharts_snapshot.main import make_a_snapshot
import tinify

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
bar.render()
bar.render('aimg.jpeg')

tinify.key = "h0ErL5tzh-FPrA1Oq6J4Vaoh6jhYPI4_"
s=tinify.from_file('./aimg.png')
s.to_file('./a.png')

# from pyecharts import Bar
# from pyecharts_snapshot.main import make_a_snapshot
#
# bar = Bar("我的第一个图表", "这里是副标题")
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90],is_more_utils=True)
# # bar.show_config()
# bar.render()
# make_a_snapshot('aimg.html', 'aimg.png')

# # 准备数据
# label = ["粮面类", "饮料类", "衣服类", "文具类", "酒类", "水果类"]
# datas = [40, 90, 30, 10, 60, 77]
# # 第一步，主标题，副标题
# bar = Bar("超市销量", "模拟")
# # 设置主题颜色，pyechars自带主题为dark
# # bar.use_theme('dark')
# # 安装主题插件
# # pip install echarts-themes-pypkg
# # vintage, macarons, infographic, shine 和 roma 主题
# bar.use_theme('macarons')
# # 第二步
# bar.add("日用品", label, datas, is_more_utils=True)
# # 第三步，生成html文件，打开后显示柱状图
# bar.render()