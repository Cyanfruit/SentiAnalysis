# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import pandas
import pymysql

dataBaseName = 'gm_eclipse'
csv_path = "E:/Design/经过处理提取的数据集/" + dataBaseName + ".csv"

## 加上字符集参数，防止中文乱码
dbconn = pymysql.connect(
    host='localhost',
    database=dataBaseName,
    user='root',
    password='hschsc123',
    port=3306
)

# sql语句
sql = 'SELECT hist_message text, Q1.hist_patchSetNum patchSetNum,Q1.hist_changeId changeId,Q1.hist_createdTime orderTime,rev_createdTime createTime,rev_committedTime commitTime,timestampdiff(HOUR, rev_committedTime, Q1.hist_createdTime) timeDiff,ch_status reviewStatus,Q2.fileNum,Q2.churn,Q3.authorNum,Q3.comments comments,Q4.patchsetCounts patchsetCounts FROM (SELECT hist_message,hist_patchSetNum,hist_changeId,hist_createdTime,rev_createdTime,rev_committedTime,ch_status FROM t_history,t_revision,t_change WHERE t_history.hist_changeId = t_revision.rev_changeId AND t_history.hist_patchSetNum = t_revision.rev_patchSetNum AND t_history.hist_changeId = t_change.id AND t_change.ch_status != \'NEW\' ) AS Q1 LEFT JOIN (SELECT rev_patchSetNum,rev_changeId,count( t_file.id ) fileNum,sum( t_file.f_linesDeleted ),sum( t_file.f_linesInserted ),sum( t_file.f_linesDeleted + t_file.f_linesInserted ) churn FROM t_revision,t_file WHERE t_file.f_revisionId = t_revision.id GROUP BY rev_changeId,rev_patchSetNum) AS Q2 ON Q1.hist_changeId = Q2.rev_changeId AND Q1.hist_patchSetNum = Q2.rev_patchSetNum LEFT JOIN ( SELECT count( DISTINCT hist_authorAccountId ) authorNum, hist_changeId, hist_patchSetNum, count( hist_message ) comments FROM t_history GROUP BY hist_changeId, hist_patchSetNum ) AS Q3 ON Q1.hist_changeId = Q3.hist_changeId AND Q1.hist_patchSetNum = Q3.hist_patchSetNum LEFT OUTER JOIN ( SELECT max( hist_patchSetNum ) patchsetCounts, hist_changeId, hist_patchSetNum FROM t_history GROUP BY hist_changeId ) AS Q4 ON Q1.hist_changeId = Q4.hist_changeId'

# 创建PR的人是否为开发者
#SELECT DISTINCT ch_authorAccountId FROM t_change WHERE t_change.ch_authorAccountId IN (SELECT DISTINCT t_people.p_accountId FROM t_revision LEFT JOIN t_people ON t_revision.rev_authorUsername = t_people.p_name)


# 参与的PR数量
# SELECT * FROM(SELECT count(A.rev_authorUsername), A.rev_authorUsername FROM (SELECT DISTINCT t_revision.rev_authorUsername, t_revision.rev_changeId FROM t_revision GROUP BY t_revision.id,t_revision.rev_changeId) AS A GROUP BY A.rev_authorUsername) AS B LEFT JOIN t_people ON B.rev_authorUsername = t_people.p_name;


# 参与的PR中被merge的数量
# SELECT * FROM(SELECT count(A.rev_authorUsername), A.rev_authorUsername FROM (SELECT DISTINCT t_revision.rev_authorUsername,t_revision.rev_changeId FROM t_revision LEFT JOIN t_change ON t_revision.rev_changeId = t_change.id WHERE t_change.ch_mergeable =1 GROUP BY t_revision.id,t_revision.rev_changeId) AS A GROUP BY A.rev_authorUsername) AS B LEFT JOIN t_people ON B.rev_authorUsername = t_people.p_name;

# PR中第一次回复的时间
# SELECT timestampdiff(MINUTE, t_revision.rev_createdTime, t_revision.rev_committedTime), t_revision.rev_patchSetNum, t_revision.rev_changeId FROM t_revision WHERE t_revision.rev_patchSetNum = 1


def dataFetch(dbconn, sql) -> pandas.DataFrame:
    # 利用pandas 模块导入mysql数据
    allData = pandas.read_sql(sql, dbconn)
    return allData


if __name__ == '__main__':
    result = dataFetch(dbconn, sql)
    result.to_csv(csv_path, index=False, sep=',', encoding="utf_8_sig")
