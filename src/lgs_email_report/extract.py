import pandas as pd
from queries.sql_statement import CHECK_AUDIT_LEADS_QUERY

def get_lead_details(engine, current_dt):
    leads_query = CHECK_AUDIT_LEADS_QUERY.format(curr_date=current_dt)
    print("leads_query ",leads_query)
    leads_df = pd.read_sql(sql=leads_query, con=engine)
    # print("patient_id_df", patient_id_df)
    return leads_df
