import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.stats import spearmanr


'''The data set used is taken from kaggle 'ai_job_trends_dataset
which can be found here, https://www.kaggle.com/datasets/sahilislam007/ai-impact-on-job-market-20242030'''

# Load the dataset
df = pd.read_csv('ai_job_trends_dataset.csv')

# dataset for US only
df_US = df[df['Location'] == 'USA']

def AIandAutomationRisk(df):
    #this function will examine the correlation between AI impact and automation risk
    '''
    AI impact level: Categorical (Low, Moderate, High)
    Automation risk: Continuous, percentage
    '''

    sns.boxplot(x='AI Impact Level', y='Automation Risk (%)', data=df)
    plt.title('Automation Risk by AI Impact Level')
    plt.xlabel('AI Impact Level')
    plt.ylabel('Automation Risk (%)')
    plt.show()

    # Spearman correlation: Indicates how strongly two sets are correlated
    # Convert categories to ordered numbers
    df['AI Impact Numeric'] = df['AI Impact Level'].map({'Low': 1, 'Moderate': 2, 'High': 3})

    corr, pval = spearmanr(df['AI Impact Numeric'], df['Automation Risk (%)'])
    print(f"Spearman correlation = {corr:.3f}, p-value = {pval:.3e}")


AIandAutomationRisk(df_US)
