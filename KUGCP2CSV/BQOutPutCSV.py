from google.cloud import bigquery
import csv
import sys
import datetime
import logging
import pandas
import db_dtypes

#ログの構成
logging.basicConfig(filename='app.log',level=logging.INFO)

#CSVのフォーマット
CSV_OUTPUT_FORMAT = {
    'delimiter': ',',
    'quotechar': '"',
    'quoting': csv.QUOTE_ALL,
    'lineterminator' : '\n'
    #'encoding': 'utf-8',
    #'date_format':'%Y-%m-%d %H:%M:%S'
}

#指定されたクエリを使用してBigQueryからデータを取得する
def get_query(query,periods,output_file_path):

    client = bigquery.Client()
    query_params = []

    #型毎にクエリの設定値を作成する
    for period in periods:
        if period.isdigit():
            query_params.append(bigquery.ScalarQueryParameter(None,"INT64",int(period)))
        elif "." in period:
            query_params.append(bigquery.ScalarQueryParameter(None,"FLOAT64",float(period)))
        else:
            query_params.append(bigquery.ScalarQueryParameter(None,"STRING",period))

    job_config = bigquery.QueryJobConfig()
    job_config.query_parameters = query_params

    #クエリにパラメータを設定する
    for i in range(len(periods)):
        sql = query.replace(f"{i+1}?",f"@period{i+1}")

    #query_job = client.query(sql, job_config=job_config) 
    df = client.query(sql, job_config=job_config).to_dataframe()
    df.to_csv(path_or_buf=output_file_path,
                   encoding='utf-8',
                   index=True,
                   quoting=csv.QUOTE_NONNUMERIC)
    print(f"CSV file saved to:{output_file_path}")
#    print(df)

#    try:
#        rows = query_job.result()
#    except Exception as e:
#        logging.exception(e)
#        print("Error: Connection to BigQuery.")
#        print(e)
#        exit()
#
#    results = []
#    for row in rows:
#        results.append(row.values())
#    return results
    return



##データをCSVファイルに出力する
#def output_data(data,file_path,csv_output_format):
#
#    with open(file_path,mode='w',newline='',encoding='utf-8') as csvfile:
#        writer = csv.writer(csvfile,**csv_output_format)
#        for row in data:
#            writer.writerow(row)
#
#    logging.info(f"CSV file saved to:{file_path}")
#    print(f"CSV file saved to:{file_path}")
#



#メイン処理
def main(query_file_path,output_file_path,periods):
    #クエリの読み込み
    with open(query_file_path,'r') as query_file:
    
        query = query_file.read()
    
    #BigQueryからデータを取得する
#    data = get_query(query,periods)
    get_query(query,periods,output_file_path)

    #指定したフォルダにCSVファイルに出力する
#    output_data(data,output_file_path,CSV_OUTPUT_FORMAT)




#初期処理
if __name__ == "__main__":
    #実行SQL読み込み
    query_file_path = sys.argv[1]
    #csv出力先指定
    output_file_path = sys.argv[2]

    #パラメータの読み込み
    if len(sys.argv) >= 4:
       periods = sys.argv[3:] 
    else:
        #periods_str = input("Enter one or more periods, separated by commas: ")
        periods_str = ""
        periods = [p.strip() for p in periods_str.split(",")]

    #エラーを記録する例外処理
    try:
        main(query_file_path,output_file_path,periods)
    except Exception as e:
        logging.exception(e)
        print(e)
        sys.exit