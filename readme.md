# 1. 使い方（BQOutPutCSV.py実行手順）

* Bigquery接続情報を確認する。
        KUGCP2CSV\KEY配下の「applied-groove-380605-5e8c978ed8f6.json」の接続情報を確認する。
        （project_id等が施設毎の設定値に修正しないと接続出来ない。）

* コマンドで実行対象「BQOutPutCSV.py」のフォルダを指定する。
        例　cd C:\Users\owner\Desktop\tools\03.Interiquet\KUGCP2CSV\KUGCP2CSV

* コマンドを実行する。
        第一パラメータ：実行用SQLパス
        第二パラメータ：csv出力先指定
        第三パラメータ以降：実施するSQLのwhere句パラメータ

        例 python BQOutCSV.py C:\Users\owner\KUGCP2CSV\SQL\SQL.txt C:\Users\owner\Desktop\test.csv 2019-1-8 a2019-1-12

# 2. 資源のご説明

* KUGCP2CSV\KEY\applied-groove-380605-5e8c978ed8f6.json

        BigQueryの接続情報

* KUGCP2CSV\BQOutPutCSV.py

        SQLを実行して、BigQueryからcsvを出力する

* SQL

* Batch
    

# 3. オフライン環境で起動させるには？

オンラインのpcで以下を実行

c:\KUGCP2CSV>pip download -d ./packages2 google-cloud-bigquery

出来た「packages2」をオフラインのpcに持っていって以下を実行

c:\KUGCP2CSV>pip install --no-index --find-links=./packages2 google-cloud-bigquery
