import convokit
import pandas as pd
from convokit import Corpus, download, TextParser, PolitenessStrategies, Classifier
train_corpus = Corpus(filename=download("stack-exchange-politeness-corpus"))

csv_path = "E:/Design/no_grouped_corpus.csv"
data = pd.read_csv(csv_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)
corpus = Corpus.from_pandas(data)

#test_corpus = Corpus(filename=download('reddit-corpus-small'))
parser = TextParser(verbosity=10000)
parser.transform(train_corpus)
parser.transform(corpus)
ps = PolitenessStrategies(verbose=10000)
ps.transform(train_corpus)
test_vector = ps.transform(corpus)

values = []
idx = []
for utterance in test_vector.iter_utterances():
    values.append(utterance.meta["politeness_strategies"])
    idx.append(utterance.id)
pd.DataFrame(values, index=idx).to_csv("feature.csv")
print("Done, results written to feature.csv")

clf = Classifier(obj_type='utterance', pred_feats=['politeness_strategies'],
                 labeller=lambda utt: utt.meta['Binary']==1)
clf.fit(train_corpus)
clf.transform(corpus)
# aww_vals = clf.summarize(test_corpus, selector=lambda utt: utt.meta['subreddit']=='aww')
# politics_vals = clf.summarize(test_corpus, selector=lambda utt: utt.meta['subreddit']=='politics')
# print(aww_vals['pred_score'].mean())
# print(politics_vals['pred_score'].mean())
result = clf.summarize(corpus)
# values = []
# idx = []
# for utterance in result.iter_utterances():
#     values.append(utterance.meta['pred_score'])
#     idx.append(utterance.id)
# pd.DataFrame(values, index=idx).to_csv("result_df_v2.csv")
print("Done, results written to result_df_v2.csv")
result.to_csv("result_df_v2.csv")
print(result['pred_score'])