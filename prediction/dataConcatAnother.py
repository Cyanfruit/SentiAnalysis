import pandas as pd


def dataConcat():
    dir_path = "E:/Design/论文/data/"
    project_list = ['angular.js/','bitcoin/','bootstrap/','core/','docker/','gaia/','go-ethereum/','kubernetes/','rust/']
    comments_path = "issue_comments.csv"
    events_path = "issue_events.csv"
    text_affect_path = "issue_comments_text_affect.csv"
    issues_path = "issues.csv"
    user_experience_in_affect_path = "user_experience_in_affect.csv"
    results_path = "result1.csv"
    result = pd.DataFrame()

    for project in project_list:
        comments = pd.read_csv(dir_path + project + comments_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)
        events = pd.read_csv(dir_path + project + events_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)
        text_affect = pd.read_csv(dir_path + project + text_affect_path, sep=',', header=0, skip_blank_lines=False,
                                  keep_default_na=False)
        issues = pd.read_csv(dir_path + project + issues_path, sep=',', header=0, skip_blank_lines=False,
                             keep_default_na=False)
        issues = issues[['reporter_id','id']]
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
        comments_with_reporter = pd.merge(comments_with_text_affect, issues, how='inner', left_on='issue_id', right_on='id')
        comments_with_reporter.drop(columns = ['id'], inplace = True)
        #获取user_in的值
        comments_with_all_data = pd.merge(comments_with_reporter, user_experience_in_affect, how='inner', left_on='user_id', right_on='user_id')
        # comments_with_all_data.drop(columns = ['user_id_y'], inplace = True)
        # comments_with_all_data.rename(columns={'user_id_x': 'user_id'}, inplace=True)
        result = pd.concat([result, comments_with_all_data], ignore_index=True)
        print(project)
    result.to_csv(dir_path + results_path, index=False, sep=',', encoding="utf_8_sig")

if __name__ == '__main__':
    dataConcat()
