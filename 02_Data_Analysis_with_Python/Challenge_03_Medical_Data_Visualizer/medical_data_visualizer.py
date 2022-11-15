
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
"""
 To determine if a person is overweight, 
 first calculate their BMI by dividing their weight in kilograms by the square of their height in meters.
 If that value is > 25 then the person is overweight.
 Use the value 0 for NOT overweight and the value 1 for overweight.
"""
BMI = ( df['weight']/ ((df['height']/100)**2)   )
df['overweight'] = BMI.apply(lambda x: 1 if x> 25 else 0) 

# Normalize data by making 0 always good and 1 always bad. 
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0. 
# If the value is more than 1, make the value 1.

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x==1 else 1)
df['gluc'] =df['gluc'].apply(lambda x: 0 if x==1 else 1)

# other solution:
# df['cholesterol'] = df['cholesterol'].replace([1, 2, 3], [0, 1, 1])
# df['gluc'] = df['gluc'].replace([1, 2, 3], [0, 1, 1])

# other solution:
#df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
#df['gluc'] = np.where(df['gluc'] > 1, 1, 0)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` 
    # using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    """
    Convert the data into long format 
    and create a chart that shows the value counts of the categorical features using seaborn's catplot(). 
    The dataset should be split by 'Cardio' so there is one chart for each cardio value. 
    The chart should look like examples/Figure_1.png.
    """
    df_cat = pd.melt(df, 
                     id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])


    # Group and reformat the data to split it by 'cardio'. 
    #Show the counts of each feature. 
    #You will have to rename one of the columns for the catplot to work correctly.
    df_cat=df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')


    # Draw the catplot with 'sns.catplot()'
    
    figure= sns.catplot(x ='variable',
                y= 'total',
                data=df_cat,
                col='cardio',
                hue='value',
                kind='bar')

    # Get the figure for the output
    fig = figure.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig



# Draw Heat Map
def draw_heat_map():
    # Clean the data
    """
    Clean the data. Filter out the following patient segments that represent incorrect data:
diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
height is more than the 97.5th percentile
weight is less than the 2.5th percentile
weight is more than the 97.5th percentil
    """
    
    df_heat = df [ (df['ap_lo'] <= df['ap_hi'])
                & (df['height'] >= df['height'].quantile(0.025))
                & (df['height'] <= df['height'].quantile(0.975)) 
                & (df['weight'] >= df['weight'].quantile(0.025))
                & (df['weight'] <= df['weight'].quantile(0.975))
                 ]

    # Calculate the correlation matrix
    """
    Create a correlation matrix using the dataset.
    Plot the correlation matrix using seaborn's heatmap(). 
    Mask the upper triangle. The chart should look like examples/Figure_2.png.
    """
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    #Solution that did not work:
    #mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(15, 15))

    # Draw the heatmap with 'sns.heatmap()'
    ax =  sns.heatmap(corr, #
               mask=mask,
               annot=True, 
               linewidths=.5,
               square=True,
               fmt='.1f', #1 decimal in the numbers within heatmap sqwuares
                
               center=0,  #it also affects cmap
               vmin=-0.12, vmax=0.3,
               cbar_kws={'shrink':0.5,'format': '%.2f'})    
    cbar = ax.collections[0].colorbar
    cbar.set_ticks(np.linspace(-0.08, 0.24, 5))

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    
    return fig
