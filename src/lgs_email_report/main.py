import boto3
import os
import sys
import pandas as pd
from extract import get_lead_details, email_compose
from utility.db import make_engine
from utility.utils import parse_envs, create_logger

env_name, environment_secrets = parse_envs()
print('Environment is:', env_name)
print('environment_secrets:', environment_secrets)
DB_ENV: str = environment_secrets["DB_ENV"]

def execute():
    print("hai", sys.argv[1])
    dt = str(sys.argv[1])
    engine = make_engine(db_env=DB_ENV)
    leads_data_df = get_lead_details(engine=engine, current_dt=dt)
    print("leads_data_df ", leads_data_df)

    email_compose(leads_data_df)


if __name__ == "__main__":
    execute()
