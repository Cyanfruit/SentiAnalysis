from psmpy import PsmPy
from psmpy.functions import cohenD
from psmpy.plotting import *
import matplotlib.pyplot as plt

# 图形设置
sns.set(rc={'figure.figsize':(10,8)}, font_scale = 1.3)
path = "E:/Design/经过处理提取的数据集/gm_eclipse.csv"

fields = [
    "ID",
    "Overall",
    "fileNum",
    "churn",
    "authorNum",
    "comments",
    "patchsetCounts",
    "mergeRate",
    "PRNum",
    "isDeveloper",
    "firstResponded"
]

data = pd.read_csv(path)[fields]

psm = PsmPy(data, indx='ID', treatment='Overall',target='timeDiff')
psm.logistic_ps(balance = True)
print(psm.predicted_data)
psm.knn_matched(matcher='propensity_score',replacement=False,caliper=0.05)

pic1 = psm.plot_match(matched_entity ='propensity_score',Title='propensity score distribution', Ylabel='numbers', Xlabel= 'propensity_score', names = ['Negative', 'Positive'], save=True)
plt.show()
print(psm.matched_ids)
pic2 = effect_size_plot(psm,title='Standardized Mean differences accross covariates before and after matching',save=True)
