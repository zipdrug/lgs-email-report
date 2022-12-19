import pandas as pd
import jinja2
from queries.sql_statement import CHECK_AUDIT_LEADS_SUCCESS_QUERY, CHECK_AUDIT_LEADS_FAILURE_QUERY

def get_lead_details(engine, current_dt):
    print("engine ", engine)
    leads_suc_query = CHECK_AUDIT_LEADS_SUCCESS_QUERY.format(curr_date=current_dt)
    #leads_query = CHECK_AUDIT_LEADS_QUERY
    print("leads_query ", leads_suc_query)
    leads_suc_df = pd.read_sql(sql=leads_suc_query, con=engine)
    leads_fail_query = CHECK_AUDIT_LEADS_FAILURE_QUERY.format(curr_date=current_dt)
    leads_fail_df = pd.read_sql(sql=leads_fail_query, con=engine)
    return leads_suc_df, leads_fail_df

def email_compose(lead_suc_df, lead_fail_df):
    '''
    print("hai")
    s_message = "Network\t\t\t\tPharmacy\t\t\t\tNPI\t\t\t\tMember\t\t\t\t"
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
    '''
    title = 'My Report'
    body_title = 'Total members matched to pharmacy'
    sc_network_lst = list(set(lead_suc_df['Network']))
    sc_lst_len = len(sc_network_lst)
    fl_network_lst = list(set(lead_fail_df['Network']))
    fl_lst_len = len(fl_network_lst)
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))
    template = jinja_env.get_template('email_report.html')
    #html = template.render(sc_df=lead_suc_df, sc_net=sc_network_lst, sc_len=sc_lst_len, fl_df=lead_fail_df, fl_net=fl_network_lst, fl_len=fl_lst_len)
    html = template.render(sc_df=lead_suc_df, sc_net=sc_network_lst, sc_len=sc_lst_len)
    print("html", html)
    with open('Email_Report_Out.html', 'w') as f:
        f.write(html)






