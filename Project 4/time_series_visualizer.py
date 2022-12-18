import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')

# Clean data
# *** The above comment is referring to the project requirement that we trim the
# *** top and bottom 2.5% of pageview values.
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]

month_labels = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']


def draw_line_plot():
    fig, ax = plt.subplots(figsize=(16, 5))
    ax.plot(df.index, df['value'], 'w', linewidth=1)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():

    # Copy and modify data for monthly bar plot
    # *** Extract months and years to individual columns with a lambda
    # *** retitle the columns so they'll match the project requirements and look good, too
    df_bar = pd.DataFrame(
        data={
            'Years': df.index.to_series().apply(lambda t: t.year),
            'Month': df.index.to_series().apply(lambda t: t.month),
            'Average Page Views': df['value']
        }
    )

    # *** use groupby to select each unique month/year combination, returning the mean.
    # *** reset the index so we don't confuse ourselves or our plotting backend.
    df_bar = df_bar.groupby(['Month', 'Years']).mean().reset_index()

    # *** now that everything is grouped and we have the mean for the pageviews,
    # *** set the values for the "Month" column to actual month names.
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

    fig = fig.fig
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    # *** I did it a little differently than the template code
    # *** in order to ensure the monthly box plot was in order from Jan to Dec.
    working_df_box = df.copy()
    working_df_box.reset_index(inplace=True)
    working_df_box['Year'] = [d.year for d in working_df_box.date]
    # *** Keep the months in numeric form for sorting.
    working_df_box['Month'] = [d.month for d in working_df_box.date]
    working_df_box.sort_values('Month', inplace=True)
    # *** this is the version of the data we'll use for plotting.
    # *** Since seaborn automatically pulls column names as labels, I
    # *** declared a new dataframe instead of renaming the columns in the old one
    # *** because it felt more readable at the time. Haven't bothered to go back
    # *** and re-do it, but it could be done.
    df_box = pd.DataFrame(
        {
            'Month': working_df_box['Month'].apply(lambda t: month_labels[t - 1][:3]),
            'Year': working_df_box['Year'],
            'Page Views': working_df_box['value']
        }
    )

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    sns.boxplot(data=df_box, ax=axes[0], x='Year', y='Page Views')
    sns.boxplot(data=df_box, ax=axes[1], x='Month', y='Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
