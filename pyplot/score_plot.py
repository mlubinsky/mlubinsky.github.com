```
#- date ( string in format YYYY-MM-DD)
#- device (string)
#- build (string)
#- metric (string)
#- number (float)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

data_by_col = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
df_by_col = pd.DataFrame.from_dict(data_by_col)

#print(df_by_col)


#data_by_row = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}

data_by_row = {
    1: ['2024-01-01', 'dev1', 'build_1', 'horiz_score', 5],
    2: ['2024-01-01', 'dev2', 'build_2', 'horiz_score', 10],
    3: ['2024-01-02', 'dev1', 'build_1', 'horiz_score', 12],
    4: ['2024-01-02', 'dev2', 'build_2', 'horiz_score', 18],
    5: ['2024-01-03', 'dev1', 'build_1', 'horiz_score', 20],
    6: ['2024-01-03', 'dev2', 'build_2', 'horiz_score', 30],

    11: ['2024-01-01', 'dev1', 'build_1', 'speed_score', 1],
    12: ['2024-01-01', 'dev2', 'build_2', 'speed_score', 2],
    13: ['2024-01-02', 'dev1', 'build_1', 'speed_score', 8],
    14: ['2024-01-02', 'dev2', 'build_2', 'speed_score', 15],
    15: ['2024-01-03', 'dev1', 'build_1', 'speed_score', 20],
    16: ['2024-01-03', 'dev2', 'build_2', 'speed_score', 25],
}

df_by_row = pd.DataFrame.from_dict(data_by_row, orient='index',
                       columns=['date', 'dut', 'build', 'metric', 'number'])
print(df_by_row)

#---------------------------------------------------------------------------
def plot_metrics_per_build(df, image_size=(10, 10), output_file="metrics_plots.png", plot_type='bar'):
#-----------------------------------------------------------------------
# Function to generate bar charts with x-axis - builds
# separate plot per metric
    # Set the style of seaborn for better visualizations
    #sns.set(style="whitegrid")
    sns.set_style("whitegrid")

    # Get unique metrics
    metrics = df['metric'].unique()
    
    # Calculate the number of rows and columns for subplots
    num_metrics = len(metrics)
    #ncols = 2  # We fix the number of columns to 2
    #nrows = math.ceil(num_metrics / ncols)
    ncols = 1
    nrows = num_metrics
    # Create subplots
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=image_size)
    axes = axes.flatten()  # Flatten the axes for easier indexing
    
    # Loop over each metric
    for i, metric in enumerate(metrics):
 
        #continue
        ax = axes[i]
        
        # Filter dataframe for the current metric
        metric_df = df[df['metric'] == metric]
        
        # Group by build and calculate the average of the number column
        avg_df_build = metric_df.groupby('build')['number'].mean().reset_index()
        #my_labels = avg_df_build["build"].tolist()
        #avg_df_date = df.groupby(['date', 'build'])['number'].mean().reset_index()
        print ('type(avg_df_build) = ',type(avg_df_build))
        # Plot the bar chart
        if plot_type == 'bar':
            sns.barplot(x='build', y='number', data=avg_df_build, ax=ax, palette="husl", hue = 'build')
        else:
            #line_style: - solid, -- dashed, : dotted
            #marker  o x + . ^ s d * p h
            sns.lineplot(x='build', y='number', data=avg_df_build, ax=ax, palette="husl", hue = 'build', marker = 'o', markersize=5, linestyle='-', linewidth=2)

        # Set title and labels
        ax.set_title(f"Metric: {metric}")
        ax.set_xlabel('Build')
        ax.set_ylabel('Average Number')
        #ax.legend(title="Build", loc='best', fontsize=12  ) #fontsize="x-large") #, labels=my_labels)
        #ax.legend( loc='upper right', fontsize=12  )
        ax.legend( loc='best', fontsize=12  )
        
        # Rotate x labels for better readability
        #https://stackoverflow.com/questions/63723514/userwarning-fixedformatter-should-only-be-used-together-with-fixedlocator
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    
#--------------------------------------------------------------------------------

    # Adjust layout
    plt.tight_layout()
    
    # Save the plot as a file
    fig.savefig(output_file, format=output_file.split('.')[-1])
    plt.close()
    print(output_file)



#----------------------------------
def plot_avg_per_build_per_date_per_metric(df, image_size=(12, 8), output_file="avg_build_per_date.png", plot_type = 'bar'):
#------------------------------------
    # Set the style of seaborn for better visualizations
    #sns.set(style="whitegrid")
    sns.set_style("whitegrid")

    # Get unique metrics
    metrics = df['metric'].unique()
    
    # Calculate the number of rows and columns for subplots
    num_metrics = len(metrics)
    #ncols = 2  # We fix the number of columns to 2
    #nrows = math.ceil(num_metrics / ncols)
    ncols = 1
    nrows = num_metrics
    # Create subplots
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=image_size)
    axes = axes.flatten()  # Flatten the axes for easier indexing
    
    # Loop over each metric
    for i, metric in enumerate(metrics):
 
        #continue
        ax = axes[i]
        
        # Filter dataframe for the current metric
        metric_df = df[df['metric'] == metric]
        
        # Group by build and calculate the average of the number column
        #avg_df_build = metric_df.groupby('build')['number'].mean().reset_index()
        avg_df_date_build = metric_df.groupby(['date', 'build'])['number'].mean().reset_index()

        # Plot the bar chart
        if plot_type == 'bar':
            sns.barplot(x='date', y='number', data=avg_df_date_build, ax=ax, palette="husl", ci=None, hue = 'build')
        else:
            #line_style: - solid, -- dashed, : dotted
            #marker  o x + . ^ s d * p h
            sns.lineplot(x='date', y='number', data=avg_df_date_build, ax=ax, palette="husl", style = 'build', hue = 'build', marker = 'o', markersize=15, linestyle='-', linewidth=2)


        # Set title and labels
        ax.set_title(f"Metric: {metric}")
        ax.set_xlabel('Date')
        ax.set_ylabel('Average Number')
        #ax.legend(title="Build", loc='best', fontsize="x-large")
        ax.legend( loc='best', fontsize="15")
        
        # Rotate x labels for better readability
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

    # Adjust layout
    plt.tight_layout()
    
    # Save the plot as a file
    fig.savefig(output_file, format=output_file.split('.')[-1])
    plt.close()
    print(output_file)

#----------------------------------
def plot_avg_per_build_per_date(df, image_size=(12, 8), output_file="avg_build_per_date.png"):
#------------------------------------
    # Function to generate bar charts with x-axis as dates and multiple bars for builds
    # Set the style of seaborn for better visualizations
    #sns.set(style="whitegrid")
    sns.set_style("whitegrid")
    
    # Group by date and build, calculate the average of 'number'
    avg_df = df.groupby(['date', 'build'])['number'].mean().reset_index()

    # Create the barplot
    plt.figure(figsize=image_size)
    sns.barplot(x='date', y='number', hue='build', data=avg_df, palette="husl")
    
    # Set title and labels
    plt.title('Average Number per Build per Date')
    plt.xlabel('Date')
    plt.ylabel('Average Number')

    # Rotate x labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Adjust the layout
    plt.tight_layout()

    # Save the plot to file
    plt.savefig(output_file, format=output_file.split('.')[-1])
    print( output_file)
    plt.close()



#plot_metrics_per_build(df_by_row , image_size=(20, 10), output_file="metrics_plots.png")
#plot_metrics_per_build(df_by_row , image_size=(20, 10), output_file="metrics_plots.png", plot_type='bar')

# plot_avg_per_build_per_date(df_by_row, image_size=(15, 10), output_file="avg_build_per_date.png")
plot_avg_per_build_per_date_per_metric(df_by_row, image_size=(15, 10), output_file="avg_build_per_date_per_metric_line.png", plot_type='line')
#plot_avg_per_build_per_date_per_metric(df_by_row, image_size=(15, 10), output_file="avg_build_per_date_per_metric.png", plot_type='bar')
```
