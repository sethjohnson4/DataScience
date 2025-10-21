import pandas as pd


'''The data set used is taken from kaggle 'ai_job_trends_dataset
which can be found here, https://www.kaggle.com/datasets/sahilislam007/ai-impact-on-job-market-20242030'''

# Load the dataset
df = pd.read_csv('ai_job_trends_dataset.csv')

# dataset for US only
df_US = df[df['Location'] == 'USA']

