import pandas as pd


def aggre():
    dir_path = "E:/Design/"
    data_path = "no_grouped_result.csv"
    result_path = "grouped_result.csv"
    comments_with_text = pd.read_csv(dir_path + data_path, sep=',', header=0, skip_blank_lines=False,
                                     keep_default_na=False, error_bad_lines=False)

    groupd = comments_with_text.groupby('issue_id').agg(
        {'arousal': 'mean', 'valence': 'mean', "dominance": 'mean', "anger": 'mean', "sadness": 'mean',
         "joy": 'mean', "love": 'mean', "politeness": 'mean', "in_arousal": 'mean',
         "in_valence": 'mean', "in_dominance": 'mean', "in_anger": 'mean', "in_sadness": 'mean', "in_joy": 'mean',
         "in_love": 'mean', "in_politeness": 'mean', "is_developer": 'mean',
         "num_commits": 'mean', "num_issues_created": 'mean', "num_comments": 'mean', "merged": 'mean',
         "isDirectSentiment": 'mean', "isDecoratedSentiment": 'mean', "isAboutMe": 'mean', "isJudgement": 'mean',
         "feature_politeness_==Please==": 'mean',
         "feature_politeness_==Please_start==": 'mean',
         "feature_politeness_==HASHEDGE==": 'mean',
         "feature_politeness_==Indirect_(btw)==": 'mean',
         "feature_politeness_==Hedges==": 'mean',
         "feature_politeness_==Factuality==": 'mean',
         "feature_politeness_==Deference==": 'mean',
         "feature_politeness_==Gratitude==": 'mean',
         "feature_politeness_==Apologizing==": 'mean',
         "feature_politeness_==1st_person_pl.==": 'mean',
         "feature_politeness_==1st_person==": 'mean',
         "feature_politeness_==1st_person_start==": 'mean',
         "feature_politeness_==2nd_person==": 'mean',
         "feature_politeness_==2nd_person_start==": 'mean',
         "feature_politeness_==Indirect_(greeting)==": 'mean',
         "feature_politeness_==Direct_question==": 'mean',
         "feature_politeness_==Direct_start==": 'mean',
         "feature_politeness_==HASPOSITIVE==": 'mean',
         "feature_politeness_==HASNEGATIVE==": 'mean',
         "feature_politeness_==SUBJUNCTIVE==": 'mean',
         "feature_politeness_==INDICATIVE==": 'mean',
         'Negative':'mean',
        'EASTER':'mean',
        'scale':'mean',
        'sentiCR':'mean',
        'binary':'mean',
        'Positive':'mean',
        'trinary':'mean',
        'senti4SD':'mean'
    }
    )

    groupd.to_csv(dir_path + result_path, index=True, index_label='ID', sep=',', encoding="utf_8_sig")


if __name__ == '__main__':
    aggre()
