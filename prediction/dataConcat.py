import pandas as pd


def dataConcat():
    dir_path = "E:/Design/论文/data/"
    project_list = ['angular.js/', 'core/', 'gaia/', 'rails/', 'docker/', 'go-ethereum/','bootstrap/', 'kubernetes/', 'rust/']
    comments_path = "issue_comments.csv"
    events_path = "issue_events.csv"
    text_affect_path = "issue_comments_text_affect.csv"
    text_path = 'issue_comments_text.csv'
    issues_path = "issues.csv"
    user_experience_in_affect_path = "user_experience_in_affect.csv"
    results_path = "result2.csv"
    no_grouped_results_path = "no_grouped_result.txt"
    result = pd.DataFrame()
    no_grouped_result = pd.DataFrame()

    for project in project_list:
        comments = pd.read_csv(dir_path + project + comments_path, sep=',', header=0, skip_blank_lines=False,
                               keep_default_na=False)
        events = pd.read_csv(dir_path + project + events_path, sep=',', header=0, skip_blank_lines=False,
                             keep_default_na=False)
        text_affect = pd.read_csv(dir_path + project + text_affect_path, sep=',', header=0, skip_blank_lines=False,
                                  keep_default_na=False)
        issues = pd.read_csv(dir_path + project + issues_path, sep=',', header=0, skip_blank_lines=False,
                             keep_default_na=False)
        comments_text = pd.read_csv(dir_path + project + text_path, sep=',', header=0, skip_blank_lines=False,
                             keep_default_na=False, error_bad_lines=False)
        comments_text = comments_text[pd.to_numeric(comments_text['comment_id'], errors='coerce').notnull()]
        comments_text['comment_id']=comments_text['comment_id'].astype(int)
        issues = issues[['reporter_id', 'id']]
        # issues = issues[issues['reporter_id'].notnull()]
        user_experience_in_affect = pd.read_csv(dir_path + project + user_experience_in_affect_path, sep=',', header=0,
                                                skip_blank_lines=False,
                                                keep_default_na=False)

        merged_issue = events.loc[events['action'] == 'merged']
        merged_issue_id = merged_issue[['issue_id', 'action']]
        # comments和merged合并，得到issue是不是被merge了
        comments_with_issue_is_merged = pd.merge(comments, merged_issue_id, how='left', on='issue_id')
        comments_with_issue_is_merged['action'].fillna(0, inplace=True)
        comments_with_issue_is_merged.loc[comments_with_issue_is_merged['action'] == 'merged', 'action'] = 1
        comments_with_issue_is_merged.rename(columns={'action': 'merged'}, inplace=True)
        # 得到有情感、礼貌信息的评审，这些是评审的out
        comments_with_text_affect = pd.merge(comments_with_issue_is_merged, text_affect, how='inner', on='comment_id')
        # 获取每个issue的创建者
        comments_with_reporter = pd.merge(comments_with_text_affect, issues, how='inner', left_on='issue_id',
                                          right_on='id')
        comments_with_reporter.drop(columns=['id'], inplace=True)
        comments_with_reporter = comments_with_reporter[comments_with_reporter['reporter_id'] != '']
        comments_with_reporter['reporter_id'] = comments_with_reporter['reporter_id'].astype(int)
        # 获取user_in的值
        comments_with_all_data = pd.merge(comments_with_reporter, user_experience_in_affect, how='inner',
                                          left_on='reporter_id', right_on='user_id')
        comments_with_all_data.drop(columns=['user_id_y'], inplace=True)
        comments_with_all_data.rename(columns={'user_id_x': 'user_id'}, inplace=True)
        comments_with_all_data["politeness"] = comments_with_all_data["politeness"].map({"impolite": 0, "polite": 1})
        comments_with_all_data["is_developer"] = comments_with_all_data["is_developer"].replace({True: 1, False: 0})
        comments_with_all_data['merged'] = comments_with_all_data['merged'].astype(int)
        comments_with_text = pd.merge(comments_with_all_data, comments_text, how='inner', on='comment_id')
        # comments_with_text.to_csv(dir_path + project +'project.csv', index=True, index_label='ID', sep=',',
        #                          encoding="utf_8_sig")
        no_grouped_result = pd.concat([no_grouped_result, comments_with_text], ignore_index=True)

        groupd = comments_with_text.groupby('issue_id').agg(
            {'arousal': 'mean', 'valence': 'mean', "dominance": 'mean', "anger": 'mean', "sadness": 'mean',
             "joy": 'mean', "love": 'mean', "politeness": 'mean', "in_arousal": 'mean',
             "in_valence": 'mean', "in_dominance": 'mean', "in_anger": 'mean', "in_sadness": 'mean', "in_joy": 'mean',
             "in_love": 'mean', "in_politeness": 'mean', "is_developer": 'mean',
             "num_commits": 'mean', "num_issues_created": 'mean', "num_comments": 'mean', "merged":'mean'})
        result = pd.concat([result, groupd], ignore_index=False)
        print(project)
    no_grouped_result['body'] = no_grouped_result['body'].astype(str)
    #no_grouped_result['body'] = no_grouped_result['body'].apply(lambda x: f'"{x}"')
    no_grouped_result['body'] = no_grouped_result['body'].apply(lambda x: limit_length(x))
    no_grouped_result['body'] = no_grouped_result['body'].replace('\t', '', regex=True).replace('\n', '', regex=True).replace('-', '', regex=True).replace('\\n', '', regex=True).replace('\\t', ' ', regex=True).replace('\r\n', ' ', regex=True)
    no_grouped_result = no_grouped_result.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    no_grouped_result.reset_index(drop=True)
    no_grouped_result['body'].to_csv(dir_path + no_grouped_results_path, index=False, index_label='ID',sep=',', encoding="utf_8_sig")
    result.to_csv(dir_path + results_path, index=True, index_label='ID',sep=',', encoding="utf_8_sig")


def limit_length(s):
    return s[:30000]

if __name__ == '__main__':
    dataConcat()
