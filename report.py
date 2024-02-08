import pandas as pd 
# server side
data = pd.read_excel("Sample_Data_S00062.xlsx", sheet_name="Sample_Data")
data.sort_values(by='Document Date',inplace=True)

distinct_supplier_codes = data['Supplier Code'].unique()
distinct_branches = data['Branch'].unique()
distinct_item_codes = data['Item Code'].unique()

def calculate_out_of_stock_days(data):
    oosd=data[data['RUNNING STOCK']<=0].count()['RUNNING STOCK']
    return oosd

def generate_report(data, item_code=None, branch=None,startdate=None,enddate=None):

#     report=[{
#         "branch": "ALL", 
#         "itemCode": "null"
#         }]
    report=[]
    start_date= "2020-12-28"
    end_date= "2024-12-31"
    
#     if (item_code not in distinct_item_codes or branch not in distinct_branches):
#         return None
#     else:
    if startdate:
        start_date = startdate

    if enddate:
        end_date = enddate

    if item_code and branch:
        filtered_data = data[(data['Item Code'] == item_code) & (data['Branch'] == branch)]
        filtered_data['RUNNING STOCK'] = filtered_data['Total Qty IN'].cumsum() - filtered_data['Total Qty OUT'].cumsum()
        filtered_data=filtered_data[filtered_data['Document Date'].between(start_date, end_date)]
        if not filtered_data.empty: 
            reporti={"itemCode" : item_code,
                         "branch": branch,
                         "itemData": {"range":"From "+start_date+" to "+end_date,
                                      "total_purchases": filtered_data['Total Qty IN'].sum(),
                                      "total_sales": filtered_data['Total Qty OUT'].sum(),
                                      "actual_oosd": calculate_out_of_stock_days(filtered_data)
                                     }
                        }
            report.append(reporti)

    elif item_code:
        for branch in distinct_branches:
            filtered_data = data[(data['Item Code'] == item_code) & (data['Branch'] == branch)]
            filtered_data['RUNNING STOCK'] = filtered_data['Total Qty IN'].cumsum() - filtered_data['Total Qty OUT'].cumsum()
            filtered_data=filtered_data[filtered_data['Document Date'].between(start_date, end_date)]
            if not filtered_data.empty:
                reporti={"itemCode" : item_code,
                         "branch": branch,
                         "itemData": {"range":"From "+start_date+" to "+end_date,
                                      "total_purchases": filtered_data['Total Qty IN'].sum(),
                                      "total_sales": filtered_data['Total Qty OUT'].sum(),
                                      "actual_oosd": calculate_out_of_stock_days(filtered_data)
                                     }
                        }
                report.append(reporti)

    elif branch:
        for item_code in distinct_item_codes:
            filtered_data = data[(data['Item Code'] == item_code) & (data['Branch'] == branch)]
            filtered_data['RUNNING STOCK'] = filtered_data['Total Qty IN'].cumsum() - filtered_data['Total Qty OUT'].cumsum()
            filtered_data=filtered_data[filtered_data['Document Date'].between(start_date, end_date)]
            if not filtered_data.empty:
                reporti={"itemCode" : item_code,
                         "branch": branch,
                         "itemData": {"range":"From "+start_date+" to "+end_date,
                                      "total_purchases": filtered_data['Total Qty IN'].sum(),
                                      "total_sales": filtered_data['Total Qty OUT'].sum(),
                                      "actual_oosd": calculate_out_of_stock_days(filtered_data)
                                     }
                        }
                report.append(reporti)
    else:
        for item_code in distinct_item_codes:
            for branch in distinct_branches:
                filtered_data = data[(data['Item Code'] == item_code) & (data['Branch'] == branch)]
                filtered_data['RUNNING STOCK'] = filtered_data['Total Qty IN'].cumsum() - filtered_data['Total Qty OUT'].cumsum()
                filtered_data=filtered_data[filtered_data['Document Date'].between(start_date, end_date)]
                if not filtered_data.empty:
                    reporti={"itemCode" : item_code,
                             "branch": branch,
                             "itemData": {"range":"From "+start_date+" to "+end_date,
                                          "total_purchases": filtered_data['Total Qty IN'].sum(),
                                          "total_sales": filtered_data['Total Qty OUT'].sum(),
                                          "actual_oosd": calculate_out_of_stock_days(filtered_data)
                                         }
                            }
                    report.append(reporti)
    return report