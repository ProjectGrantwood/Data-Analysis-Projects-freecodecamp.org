# FCC-Data-Analysis-Certification

This repository contains a collection of the relevant coursework I completed in earning the Data Analysis with Python certification from [freeCodeCamp.org](https://www.freecodecamp.org/learn/data-analysis-with-python/). You can verify the certification [here](https://www.freecodecamp.org/certification/JustinTurner/data-analysis-with-python-v7). If you want a strong sense of my fluency in Python as well as my ability to communicate in the context of code development, there's a notebook file (identified by the \**.ipynb* extension) in each project folder that is an example of my output when it's waxed and polished. Copies of the files I submitted to earn the certification are also present in each project folder, and are named using the actual project title (for example, Project 1's submission file is *mean_var_std.py*).

I gained proficiency with several Python modules while completing the requirements for this certification. I've listed them below, loosely ordered by how much focus I felt I had to give them in order to fulfill those requirements:

- Pandas  
- Matplotlib  
- Seaborn  
- Numpy  

Here's just one example of my work, in this case, from project 4 ('Time Series Visualizer'):

```python

def draw_bar_plot():

    # Copy and modify data for monthly bar plot
    # Extract months and years to individual columns with a lambda
    # retitle the columns so they'll match the project requirements
    df_bar = pd.DataFrame(
        data={
            'Years': df.index.to_series().apply(lambda t: t.year),
            'Month': df.index.to_series().apply(lambda t: t.month),
            'Average Page Views': df['value']
        }
    )

    # use groupby to select each unique month/year combination, returning the mean.
    # reset the index so we don't confuse ourselves or our plotting backend.
    df_bar = df_bar.groupby(['Month', 'Years']).mean().reset_index()

    # now that everything is grouped and we have the mean for the pageviews,
    # set the values for the "Month" column to actual month names.
    df_bar['Month'] = df_bar['Month'].apply(lambda t: month_labels[int(t) - 1])

    # Use seaborn to draw the plot.
    fig = sns.catplot(
        data=df_bar,
        x='Years',
        y='Average Page Views',
        kind='bar',
        hue='Month',
        legend_out=False
    )

    # Need to set the return value to "fig.fig" because we used a seaborn figure-level function,
    # And the actual matplotlib figure is a property of the returned object.
    fig = fig.fig
    
    fig.savefig('bar_plot.png')
    return fig
    
```
    
And the output:

![Image of a bar plot constructed using the Seaborn module](/Project 4/bar_plot.png)
