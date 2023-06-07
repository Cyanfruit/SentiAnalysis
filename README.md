# SentiAnalysis

## politeness
main.py 使用Convokit politenessStrategies获取politeness值
test.py 使用Convokit politenessStrategies获取politenessStrategies

## psm:

数据集：http://kin-y.github.io/miningReviewRepo/

dataGet.py 获取各种指标的sql及执行

dataHandle.py 根据设定的条件过滤文本信息

dataConcat4***.py 将各情绪分析工具获取的信息和数据合并

dataAggregate.py 以PR的平均值，第一条评论的情绪值或最后一条评论的情绪值来代表PR的情绪值

psm3.py 进行psm

dataMatch.py 根据psm后得到的id对，保存每组对应id的数据信息

### data:
EASTER：使用EASTER提取PR文本中的情绪信息

Senti4SD：使用Senti4SD提取PR文本中的情绪信息

SESSION：使用SESSION提取PR文本中的情绪信息

psm result：对合并后的数据进行PSM分析情绪和PR的关联关系，其中包含对PR的数据采用了不同的聚合方式以及后续添加的非情绪因素指标

observation：对不同情绪的PR中的具体数据进行观察


## huawei:

华为代码及数据


## prediction：

数据集：https://zenodo.org/record/3825044#.ZDFvv3tBwdU

dataConcat.py：根据表关系提取数据

aggre.py：以PR为单位聚合数据

rfLogit.py smLogit.py smfLogit.py sklearnLogit.py 都是逻辑回归，实现方式不同

randomforest.py 构建随机森林分类器

### data:
特征：包含SentiCR、SESSION、Senti4SD、EASTER的输出、SESSION的四种表达模型信息，Convokit提取的和文本特征有关的情绪指标

加入特征：将特征和数据集提取的数据进行合并以及构建的随机森林分类器的结果

其他结果：逻辑回归模型的结果
