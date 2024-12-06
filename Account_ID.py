

import pandas as pd

def Account_ID(pathway):
    df = pd.read_csv(pathway)
    total_donations = df.groupby('Account ID')['Donation Amount'].sum()
    account_counts = df['Account ID'].value_counts()
    result = {
        int(account_id): {
            'Count': int(account_counts[account_id]),
            'Total_donation': int(total_donations[account_id]),
        }
        for account_id in account_counts.index
    

    }
    total_donations_all_accounts = total_donations.sum()

    print(total_donations_all_accounts,"\n")
    print(result,"\n")



Account_ID("/Users/ejmainu/downloads/2018 Annual Campaign - Archived.csv")
Account_ID("/Users/ejmainu/downloads/2019 Annual Campaign - Archived.csv")
Account_ID("/Users/ejmainu/downloads/2020 Annual Campaign - Archived.csv")
Account_ID("/Users/ejmainu/downloads/2021 Annual Campaign - Archived.csv")
Account_ID("/Users/ejmainu/downloads/2021 NBC 15 Community Diaper Driver.csv")
Account_ID("/Users/ejmainu/downloads/2022 Annual Campaign - Active.csv")
Account_ID("/Users/ejmainu/downloads/2022 Bottoms Up Ball - Active.csv")
Account_ID("/Users/ejmainu/downloads/2022 NBC 15 Community Diaper Driver.csv")
Account_ID("/Users/ejmainu/downloads/2023 Annual Campaign - Active.csv")
Account_ID("/Users/ejmainu/downloads/2023 Bottoms Up Ball - Active.csv")
Account_ID("/Users/ejmainu/downloads/2023 NBC 15 Community Diaper Driver.csv")
Account_ID("/Users/ejmainu/downloads/2024 Annual Campaign - Active.csv")
Account_ID("/Users/ejmainu/downloads/2024 WMTV Diaper Drive.csv")




