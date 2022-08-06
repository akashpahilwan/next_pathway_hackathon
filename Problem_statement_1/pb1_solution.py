query="""
SELECT
T.SWB_CNTRY_ID,
T.CNTRY_TYPE_CD,
T.DW_EFF_DT,
S.DW_AS_OF_DT
FROM
(SELECT
SWB_CNTRY_ID,
CNTRY_TYPE_CD,
RCV_IN,
DW_EFF_DT,
MAX(DW_EFF_DT) MAX_EFF_DT
FROM IDW_DATA.CNTRY_MULTI_DEF_CD_T
WHERE
CURR_IN=1 GROUP BY 1,2,3,4) T
INNER JOIN
(SELECT
SWB_CNTRY_ID,
CNTRY_SCHEME_CD,
DW_AS_OF_DT,
DW_ACTN_IND
FROM IDW_STAGE.CNTRY_MULTI_DEF_CD_S) S
On
S.SWB_CNTRY_ID = T.SWB_CNTRY_ID AND S.CNTRY_SCHEME_CD = T.CNTRY_TYPE_CD
WHERE (S.DW_SCTN_IND=‘U’ OR (S.DW_ACTN_IND=‘I’ AND T.RCV_IN=0))
AND S.DW_AS_OF_DT > T.MAX_EFF_DT
"""

import sqlparse
from sql_metadata import Parser


def generate_selected_columns(query): #generate selected column with table alias name
    selected_list=[]
    query_selected=query[:query.index("FROM")]
    query_not_from=query_selected.replace("SELECT","")
    query_list=query_not_from.split(",")
    for col in query_list:
        col1=col.replace("\n","")
        tbl_alias=col1.split(".")[0]
        colmn_name=col1.split(".")[1]
        selected_list.append([colmn_name,tbl_alias])
    return selected_list


def generate_final_list(selected_list): #generate column to table mapping list
    final_mapping=[]
    for ele in selected_list:
        index_from=table_alias[ele[1]].index("FROM")
        try:
            index_to=table_alias[ele[1]].index("WHERE")
        except:
            index_to=10000
        table_name=table_alias[ele[1]][index_from:index_to]
        final_mapping.append([ele[0],table_name])
    return final_mapping


def print_final_list(final_list):  #Printing final coln -> table_name
    for i in range(len(final_list)):
        print(final_list[i][0]," => ",final_list[i][1])

parser = Parser(query)
table_alias=parser.subqueries
tables=parser.tables

selected_list=generate_selected_columns(query)
final_list=generate_final_list(selected_list)

print_final_list(final_list)




