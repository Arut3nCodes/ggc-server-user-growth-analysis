import matplotlib.pyplot as plt
import numpy as np

def plot_user_gained(user_gained_list, titles_list):
    for data_title_pair in zip(user_gained_list, titles_list):
        
        if data_title_pair[1] == 'Daily':
            fig, ax = plt.subplots(figsize=(20, 5))  # Create a figure and axis for the 
            ax.plot( # Create a line plot for user gains over time
                data_title_pair[0]['timestamp'],
                data_title_pair[0]['user_gained'],
                color='orange',
                linewidth=3,
                marker='o'
                )
        elif data_title_pair[1] == 'Weekly':
            fig, ax = plt.subplots(figsize=(15, 5))  # Create a figure and axis for the 
            ax.step(
                data_title_pair[0]['timestamp'],
                data_title_pair[0]['user_gained'],
                where='post',
                color='blue',
                linewidth=3,
                marker='s'
            )
        else:  # Monthly
            fig, ax = plt.subplots(figsize=(15, 5))  # Create a figure and axis for the 
            ax.bar(
                data_title_pair[0]['timestamp'],
                data_title_pair[0]['user_gained'],
                color='green',
                width=20,
            )

        ax.set_title( # Plot title with custom font properties
            label= data_title_pair[1] + ' User gains', # plot title
            fontsize=16,
            fontweight='bold'
            ) 

        ax.set_xlabel( # Label the x-axis
            xlabel='Time unit',
            fontsize=12,
            fontweight='bold'
            )  

        ax.set_ylabel( # Label the y-axis
            ylabel='Number of Users gained',
            fontsize=12,
            fontweight='bold'
            )  

        ax.grid(
            which='major',
            linestyle='--',
            alpha=0.35,
        )
        if data_title_pair[1] == 'Daily':
            ax.set_xticks(data_title_pair[0]['timestamp'][::7]) # set x-ticks to every 7th date for better readability
            ax.tick_params(axis='x', rotation=45) # Rotate x-tick labels for better readability
        elif data_title_pair[1] == 'Weekly':
            ax.set_xticks(data_title_pair[0]['timestamp'])
            ax.tick_params(axis='x', rotation=45) # Rotate x-tick labels for better readability
        elif data_title_pair[1] == 'Monthly':
            ax.set_xticks(data_title_pair[0]['timestamp'])
            ax.tick_params(axis='x', rotation=0) # Rotate x-tick labels for better readability
            ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))  # Format x-axis labels to show month and year
        
        ax.set_ylabel('Number of Users')  # Label the y-axis
            
        plt.show()  # Show the plot of user growth over time

def plot_user_lost(user_lost_list, titles_list):
    for data_title_pair in zip(user_lost_list, titles_list):
        
        if data_title_pair[1] == 'Daily':
            fig, ax = plt.subplots(figsize=(20, 5))  # Create a figure and axis for the 
            ax.plot( # Create a line plot for user gains over time
                data_title_pair[0]['timestamp'],
                data_title_pair[0]['user_lost'],
                color='orange',
                linewidth=3,
                marker='o'
                )
        elif data_title_pair[1] == 'Weekly':
            fig, ax = plt.subplots(figsize=(15, 5))  # Create a figure and axis for the 
            ax.step(
                data_title_pair[0]['timestamp'],
                data_title_pair[0]['user_lost'],
                where='post',
                color='blue',
                linewidth=3,
                marker='s'
            )
        else:  # Monthly
            fig, ax = plt.subplots(figsize=(15, 5))  # Create a figure and axis for the 
            ax.bar(
                data_title_pair[0]['timestamp'],
                data_title_pair[0]['user_lost'],
                color='green',
                width=20,
            )

        ax.set_title( # Plot title with custom font properties
            label= data_title_pair[1] + ' User losses', # plot title
            fontsize=16,
            fontweight='bold'
            ) 

        ax.set_xlabel( # Label the x-axis
            xlabel='Time unit',
            fontsize=12,
            fontweight='bold'
            )  

        ax.set_ylabel( # Label the y-axis
            ylabel='Number of Users lost',
            fontsize=12,
            fontweight='bold'
            )  

        ax.grid(
            which='major',
            linestyle='--',
            alpha=0.35,
        )
        if data_title_pair[1] == 'Daily' or data_title_pair[1] == 'Weekly':
            ax.set_xticks(data_title_pair[0]['timestamp'][::7]) # set x-ticks to every 7th date for better readability
            ax.tick_params(axis='x', rotation=45) # Rotate x-tick labels for better readability
        elif data_title_pair[1] == 'Monthly':
            ax.set_xticks(data_title_pair[0]['timestamp'])
            ax.tick_params(axis='x', rotation=0) # Rotate x-tick labels for better readability
            ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))  # Format x-axis labels to show month and year
        
        ax.set_ylabel('Number of Users')  # Label the y-axis
            
        plt.show()  # Show the plot of user growth over time
        
def plot_user_net_daily(user_net_list):
    fig, ax = plt.subplots(figsize=(20, 5))  # Create a figure and axis for the plot

    ax.bar(
        label='Users gained',
        x=user_net_list['timestamp'],
        height=user_net_list['user_gained'],
        color='green',
        alpha=1
    )

    ax.bar(
        label='Users lost',
        x=user_net_list['timestamp'],
        height=-user_net_list['user_lost'],
        color='red',
        alpha=1
    )
    
    ax.bar(
        x=user_net_list['timestamp'],
        height=user_net_list['user_net_growth'],
        color='black',
        alpha=0.375
    )
    
    ax.step( # Create a line plot for user gains over time
        label='Net value',
        x=user_net_list['timestamp'],
        y=user_net_list['user_net_growth'],
        color='black',
        alpha=1,
        marker='o',
        markersize=3,
        where='mid',
        )

    ax.set_title( # Plot title with custom font properties
        label='Daily User Net Change', # plot title
        fontsize=16,
        fontweight='bold'
        ) 

    ax.set_xlabel( # Label the x-axis
        xlabel='Date',
        fontsize=12,
        fontweight='bold'
        )  

    ax.set_ylabel( # Label the y-axis
        ylabel='Net Change in Users',
        fontsize=12,
        fontweight='bold'
        )  

    ax.grid(
        which='major',
        linestyle='--',
        alpha=0.35,
    )
    
    ax.legend()
    
    ax.set_xticks(user_net_list['timestamp'][::7]) # set x-ticks to every 7th date for better readability
    ax.tick_params(axis='x', rotation=45) # Rotate x-tick labels for better readability
    
    plt.show()  # Show the plot of user growth over time

def plot_user_net_weekly(user_net_list):
    fig, ax = plt.subplots(figsize=(20, 5))  # Create a figure and axis for the plot
    
    ax.set_title( # Plot title with custom font properties
        label='Weekly User Net Change', # plot title
        fontsize=16,
        fontweight='bold'
        ) 

    ax.bar(
        label='Users gained',
        x=np.arange(len(user_net_list)),
        height=user_net_list['user_gained'],
        color='green',
        alpha=1,
        width=0.975,
    )

    ax.bar(
        label='Users lost',
        x=np.arange(len(user_net_list)),
        height=-user_net_list['user_lost'],
        color='red',
        alpha=1,
        width=0.975,
    )
    
    ax.step( # Create a line plot for user gains over time
        label='Net value',
        x=np.arange(len(user_net_list)),
        y=user_net_list['user_net_growth'],
        color='black',
        alpha=1,
        marker='o',
        markersize=3,
        where='mid',
        )

    ax.set_xlabel( # Label the x-axis
        xlabel='Date',
        fontsize=12,
        fontweight='bold'
        )  

    ax.set_ylabel( # Label the y-axis
        ylabel='Net Change in Users',
        fontsize=12,
        fontweight='bold'
        )  

    ax.grid(
        which='major',
        linestyle='--',
        alpha=0.1,
    )
    
    ax.legend()
    ax.set_xticklabels(user_net_list['timestamp'].dt.strftime('%d %b'))
    ax.tick_params(axis='x', rotation=45) # Rotate x-tick labels for better readability
    plt.show()  # Show the plot of user growth over time
    
def plot_total_users_daily(user_total_list):
    fig, ax = plt.subplots(figsize=(10, 5))  # Create a figure and axis for the plot

    ax.plot( # Plot total users over time
        user_total_list['timestamp'],
        user_total_list['total_users'],
        linewidth=3,
        marker='o',
        markersize=6, 
        markevery=7,
        markeredgecolor='darkblue',
            )  

    ax.set_title( # Plot title with custom font properties
        label='Total user growth over time', # plot title
        fontsize=16,
        fontweight='bold'
        )

    ax.set_xlabel( # Label the x-axis
        xlabel='Date',
        fontsize=12,
        fontweight='bold'
        )  

    ax.set_ylabel( # Label the y-axis
        ylabel='Number of Users',
        fontsize=12,
        fontweight='bold'
        )  

    # Add value labels every 7 points
    for i in range(0, len(user_total_list), 7):
        ax.annotate(
            f"{user_total_list['total_users'].iloc[i]:,}",
            (
                user_total_list['timestamp'].iloc[i],
                user_total_list['total_users'].iloc[i]
            ),
            textcoords="offset points",
            xytext=(0, 10),
            ha='center',
            fontsize=9
        )

    ax.set_xticks(user_total_list['timestamp'][::7]) # set x-ticks to every 7th date for better readability
    ax.tick_params(axis='x', rotation=45) # Rotate x-tick labels for better readability

    ax.set_ylabel('Number of Users')  # Label the y-axis

    plt.show()  # Show the plot of user growth over time