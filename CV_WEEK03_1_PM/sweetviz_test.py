import sweetviz as sv
import pandas as pd

df_dataset = pd.read_csv("train.csv")
my_report = sv.analyze(df_dataset)
my_report.show_html()