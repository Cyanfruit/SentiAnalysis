# SentiAnalysis

psm:

数据集：http://kin-y.github.io/miningReviewRepo/

dataGet.py 获取各种指标的sql及执行

dataHandle.py 根据设定的条件过滤文本信息

dataConcat4***.py 将各情绪分析工具获取的信息和数据合并

dataAggregate.py 以PR的平均值，第一条评论的情绪值或最后一条评论的情绪值来代表PR的情绪值

psm3.py 进行psm

dataMatch.py 根据psm后得到的id对，保存每组对应id的数据信息



huawei:

华为代码及数据

prediction：

数据集：https://zenodo.org/record/3825044#.ZDFvv3tBwdU

dataConcat.py：根据表关系提取数据

aggre.py：以PR为单位聚合数据
