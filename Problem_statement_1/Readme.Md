Next Pathway Hackathon
====================

Hello All ! </br>
This repository is for my submissions of the Problem statements for [Next-Pathway-Hackathon](https://wuelev8.tech/drills/next-pathway-hack-backpackers). </br>

Problem Statement 1
====================
Identify output columns’ originating tables for SQL query </br>

Provided SQL Query
---------------------
```
LOCKING ROW FOR ACCESS
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
CURR_IN=1 GROUP BY 1,2,3,4) T,
(SELECT
SWB_CNTRY_ID,
CNTRY_SCHEME_CD,
DW_AS_OF_DT,
DW_ACTN_IND
FROM IDW_STAGE.CNTRY_MULTI_DEF_CD_S) S
WHERE
S.SWB_CNTRY_ID = T.SWB_CNTRY_ID AND S.CNTRY_SCHEME_CD = T.CNTRY_TYPE_CD
AND (S.DW_SCTN_IND=‘U’ OR (S.DW_ACTN_IND=‘I’ AND T.RCV_IN=0))
AND S.DW_AS_OF_DT > T.MAX_EFF_DT
```
Expected output
---------------------
Output is expected in key value pair of only selected column as key and table as value.</br>
The output can be obtained using SQL/Python script.</br>

Example:</br>
```
column => table
SWB_CNTRY_ID => IDW_DATA.CNTRY_MULTI_DEF_CD_T
CNTRY_TYPE_CD => IDW_DATA.CNTRY_MULTI_DEF_CD_T
DW_EFF_DT => IDW_DATA.CNTRY_MULTI_DEF_CD_T
DW_AS_OF_DT => IDW_STAGE.CNTRY_MULTI_DEF_CD_S
```

Solution Approach:
----------------------
The solution that I have obtained is partial solution. This will only work for all required columns if the tables are joined using "JOIN" keywork rather than joining in where clause.

Pre-requistes:
----------------------
1. Installing two different python utilities in terminal:
```
pip install sqlparse
pip install sql_metadata
```

Now refer [pb1_solution.py](./pb1_solution.py) for my submission.



