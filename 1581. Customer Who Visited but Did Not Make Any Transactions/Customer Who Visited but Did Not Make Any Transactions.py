import pandas as pd

def sql_groupby(df,as_index=False,**kwargs): #Wrapper for sqp-style group by
    groupby_cols = kwargs.pop('groupby')
    return df.groupby(groupby_cols, as_index=as_index).agg(**kwargs)

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    result = visits.merge(transactions,left_on='visit_id',right_on='visit_id',how='left')
    result = result[result['transaction_id'].isna()][['customer_id'
    # ,'visit_id' #to demonstrate additional columns
    ]]

    result = sql_groupby(result, groupby=['customer_id'
                                            # , 'visit_id' #to demonstrate additional columns
                                            ]
                         ,count_no_trans=('customer_id', 'count')
                        # ,max_visit_id=('visit_id', 'max') #to demonstrate additional columns
                        ) 


    # -- without using function --
    # result = result.groupby(['customer_id'],as_index=False).agg(count_no_trans=('customer_id','count')
    # , max_visit_id = ('visit_id','max') #to demonstrate additional columns
    # )


    # result = result.groupby(['customer_id'])['customer_id'].count().reset_index(name='count_no_trans') #alternative 1


    # result = result.groupby(['customer_id'])['customer_id'].size().reset_index(name='count_no_trans') #alternative 2

    return result
