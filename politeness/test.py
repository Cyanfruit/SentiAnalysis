import pandas as pd

from convokit import Corpus, Speaker, Utterance
from convokit import PolitenessStrategies, TextParser, Classifier

csv_path = "E:/Design/经过处理提取的数据集/gm_eclipse_corpus格式.csv"
data = pd.read_csv(csv_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)
print("Loading awry corpus...")
corpus = Corpus.from_pandas(data)
parser = TextParser(verbosity=10000)
corpus = parser.transform(corpus)
# extract the politeness strategies.
# Note: politeness strategies are a hand-engineered feature set, so no fitting is needed.
ps = PolitenessStrategies(verbose=10000)
corpus = ps.transform(corpus, markers=True)
print("Extracting politeness strategies...")

values = []
idx = []
for utterance in corpus.iter_utterances():
    values.append(utterance.meta["politeness_strategies"])
    idx.append(utterance.id)
pd.DataFrame(values, index=idx).to_csv("ce.csv")
print("Done, results written to ce.csv")

