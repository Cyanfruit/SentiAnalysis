#调取各类依赖包
import pandas as pd
from bokeh.plotting import figure, show, output_file

positive_path = "E:/Design/经过处理提取的数据集/gm_eclipse_对照组_积极.csv"
negative_path = "E:/Design/经过处理提取的数据集/gm_eclipse_干预组_消极.csv"
df_positive = pd.read_csv(positive_path)
df_negative = pd.read_csv(negative_path)

#建立测试数据
d1 = {'样本': df_positive.timeDiff }
d2 = {'样本': df_negative.timeDiff}
df1 = pd.DataFrame(data=d1)
df1['维度']='积极'
df2 = pd.DataFrame(data=d2)
df2['维度']='消极'
df=pd.concat([df1,df2])

#数据格式化
cats=list(df[u'维度'].drop_duplicates().sort_values())
catss=list(map(lambda x:str(x),cats))

#数据四分位获取
groups = df.groupby(u'维度')
q1 = groups.quantile(q=0.25)
q2 = groups.quantile(q=0.5)
q3 = groups.quantile(q=0.75)
iqr = q3 - q1
upper = q3 + 1.5*iqr
lower = q1 - 1.5*iqr

#数据可视化
TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
p = figure(tools=TOOLS,plot_width=1200,
           title="样本分布图", x_range=catss)

qmin = groups.quantile(q=0.00)
qmax = groups.quantile(q=1.00)
upper[u'样本'] = [min([x,y]) for (x,y) in zip(list(qmax.loc[:,u'样本']),upper[u'样本'])]
lower[u'样本'] = [max([x,y]) for (x,y) in zip(list(qmin.loc[:,u'样本']),lower[u'样本'])]

# 线绘制
p.segment(catss, upper[u'样本'], catss, q3[u'样本'], line_color="black")
p.segment(catss, lower[u'样本'], catss, q1[u'样本'], line_color="black")

# 方块绘制
p.vbar(catss, 0.7, q2[u'样本'], q3[u'样本'], fill_color="#E08E79", line_color="black")
p.vbar(catss, 0.7, q1[u'样本'], q2[u'样本'], fill_color="#3B8686", line_color="black")

#其他bokeh组件设置
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = "white"
p.grid.grid_line_width = 2
p.xaxis.major_label_text_font_size="12pt"

output_file("boxplot.html", title="boxplot.py example")
show(p)