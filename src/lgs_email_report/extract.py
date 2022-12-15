import pandas as pd
from queries.sql_statement import CHECK_AUDIT_LEADS_QUERY

def get_lead_details(engine, current_dt):
    print("engine ", engine)
    #leads_query = CHECK_AUDIT_LEADS_QUERY.format(curr_date=current_dt)
    leads_query = CHECK_AUDIT_LEADS_QUERY
    print("leads_query ", leads_query)
    leads_df = pd.read_sql(sql=leads_query, con=engine)

    return leads_df

def email_compose(lead_df):
    print("hai")

