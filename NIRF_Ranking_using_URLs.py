# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 13:02:10 2023

@author: Manoj Kaushik
"""

import time
import pandas as pd
import matplotlib.pyplot as plt

# NIRF Ranking Analysis 2023
url_overall = "https://www.nirfindia.org/2023/OverallRanking.html"
url_universities = "https://www.nirfindia.org/2023/UniversityRanking.html"
url_colleges = "https://www.nirfindia.org/2023/CollegeRanking.html"
url_research = "https://www.nirfindia.org/2023/ResearchRanking.html"
url_engineering = "https://www.nirfindia.org/2023/EngineeringRanking.html"
url_management = "https://www.nirfindia.org/2023/ManagementRanking.html"
url_pharmacy = "https://www.nirfindia.org/2023/PharmacyRanking.html"
url_medical = "https://www.nirfindia.org/2023/MedicalRanking.html"
url_dental = "https://www.nirfindia.org/2023/DentalRanking.html"
url_law = "https://www.nirfindia.org/2023/LawRanking.html"
url_architecture = "https://www.nirfindia.org/2023/ArchitectureRanking.html" 
url_agri = "https://www.nirfindia.org/2023/AgricultureRanking.html"
url_innovation = "https://www.nirfindia.org/2023/InnovationRanking.html"

urls = [url_overall, url_universities, url_colleges, url_research, url_engineering, url_management, url_pharmacy, url_medical, url_dental, url_law, url_architecture, url_agri, url_innovation]

# Accumulating Statewise Number of Institutes in top 100 NIRF Ranking
df_final = pd.DataFrame()
flag = True
for url in urls:
    delay = 5
    max_retries = 3
    for _ in range(max_retries):
        try:
            ranking_type = url.split("/")[-1].split(".")[0]
            print("ranking_type:", ranking_type, "\n")
            df_list = pd.read_html(url)
            rankings_tbl = df_list[0]    
            rank_series = rankings_tbl["State"].value_counts()
            rank_df = pd.DataFrame(data=rank_series.values, index=rank_series.index, columns=['NoI_'+ranking_type[:-7]])
            rank_df.index = rank_df.index.str.title()
            if flag:
                df_final = rank_df.copy()
            else:
                df_final = df_final.join(rank_df)
            flag = False
            break # do not loop after a successfull download...
        except Exception as e:
            print(e)
            time.sleep(delay)
            delay *= 2


# df_final = df_final.drop(['Total'], axis=1)
df_final['Total'] = df_final.sum(axis=1)
df_final = df_final.sort_values(by=['Total'], ascending=False)
df_final.to_csv(r'E:\0.Manoj\Python Scripts\Outputs\NIRF_ranking_Institutions.csv')


# Plotting
# Draw line plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df_final.index, df_final['Total'], 'g', linewidth=2)
ax.set_xlabel("States")
ax.set_ylabel("Total No. of Institutes")
ax.set_title("NIRF Ranking 2023 Total")
plt.xticks(rotation=70)
plt.show()
