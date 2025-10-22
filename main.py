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

def IndustryAutomationRisk(df):
    sns.boxplot(x='Industry', y='Automation Risk (%)', data=df)
    plt.title('Automation Risk by Industry')
    plt.xlabel('Industry')
    plt.ylabel('Automation Risk (%)')
    plt.show()

def JobImpact(df):
    df.sort_values(by=('Automation Risk (%)'), ascending=False, inplace=True)
    print("Top 20 jobs at the highest risk of being replaced by automation:\n")
    print(df[['Job Title', 'Automation Risk (%)', 'AI Impact Level']].head(20))

    print("\nTop 20 jobs with the lowest risk of being automated:\n")
    print(df[['Job Title', 'Automation Risk (%)', 'AI Impact Level']].tail(20))



#AIandAutomationRisk(df_US)
#IndustryAutomationRisk(df_US)
#JobImpact(df_US)
