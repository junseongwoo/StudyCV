import pandas as pd
from pandas_profiling import ProfileReport

df_dataset = pd.read_csv("train.csv")

profile = ProfileReport(df_dataset, title="타이타닉 데이터셋 분석 결과", explorative=True)