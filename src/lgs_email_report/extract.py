import pandas as pd
from queries.sql_statement import CHECK_AUDIT_LEADS_QUERY

def get_lead_details(engine, current_dt):
    print("engine ", engine)
    leads_query = CHECK_AUDIT_LEADS_QUERY.format(curr_date=current_dt)
    #leads_query = CHECK_AUDIT_LEADS_QUERY
    print("leads_query ", leads_query)
    leads_df = pd.read_sql(sql=leads_query, con=engine)

    return leads_df

def email_compose(lead_df):
    print("hai")
    s_message = "Network\t\t\t\tPharmacy\t\t\t\t\tNPI\t\t\t\t\tMember\t\t\t\t"
    for i in lead_df.index:
        if lead_df['status'][i] == 1:
            network = str(lead_df['network'][i]) + "\t\t\t\t"
            pharmacy=str(lead_df['pharmacy'][i]) + "\t\t\t"
            npi=str(lead_df['npi'][i]) + "\t\t\t"
            member=str(lead_df['members'][i]) + "\t\t\t\t"
            s_message = s_message + "\n"
            s_message = s_message + network + pharmacy + npi + member
    print("output")
    print(s_message)


