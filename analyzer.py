import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# generate sample data
# user_id, policy_id, size in characters
def generate_data():
    a, n, multiplier = 3.0, 100000, 0.2
    sample = np.random.default_rng(123).zipf(a, size=n) * multiplier
    return sample

# save data
def write_data():
    pass

# read data
def read_data(file):
    pass

# process data, print stats, create graphs
def process_data(data):
    fig1, axs = plt.subplots(1, 2, figsize=(10, 5), dpi=192)
    fig1.suptitle('Frequency Distribution of Largest Policy String per User')

    bin_size = 5
    bins = np.arange(min(data), max(data) + bin_size, bin_size)
    axs[0].hist(data, bins=bins)
    axs[0].set_title('Log Graph')
    axs[0].set_yscale('log')
    axs[0].set_ylabel('Number of Users')
    axs[0].set_xlabel('Size of Largest Policy String in kB')
    
    yticks = np.arange(0, 11)
    yrange = (yticks[0], yticks[-1])
    axs[1].set_title('Linear Graph Capped at 10 Users')
    axs[1].hist(data, bins=bins)
    axs[1].set_yticks(yticks)
    axs[1].set_ylim(yrange)
    axs[1].set_ylabel('Number of Users')
    axs[1].set_xlabel('Size of Largest Policy String in kB')

    fig2, ax0 = plt.subplots(1, 1, figsize=(5, 5), dpi=192)
    fig2.suptitle('Frequency Distribution of\nLargest Policy String per User')
    ax0.hist(data, bins=bins)
    ax0.set_yticks(yticks)
    ax0.set_ylim(yrange)
    ax0.set_ylabel('Number of Users')
    ax0.set_xlabel('Size of Largest Policy String in kB')

    fig3, ax1 = plt.subplots(1, 1, figsize=(5, 5), dpi=192)
    fig3.suptitle('Frequency Distribution of\nLargest Policy String per User')
    ax1.hist(data, bins=bins)
    ax1.set_yticks(yticks)
    ax1.set_ylim(yrange)
    ax1.set_ylabel('Number of Users')
    ax1.set_xlabel('Size of Largest Policy String in kB')
    threshold = 10
    ax1.axvline(x=threshold, color='xkcd:red', linestyle='-')
    ax1.text(x=threshold+2, y=2.5, s=f'{threshold} kB', color='xkcd:red', bbox=dict(facecolor='#FFFFFF88', linewidth=0))
    info_text = f'Number of users with\npolicy strings over {threshold} kB: {data[data > threshold].size}'
    props = dict(boxstyle='round', facecolor='wheat')
    ax1.text(0.95, 0.95, info_text, transform=ax1.transAxes, fontsize=8, verticalalignment='top', horizontalalignment='right',
             bbox=props)
    plt.show()


def main():
    # if data doesn't exist generate data and save it
    # data_filename = input('filename')
    
    data = generate_data()
    process_data(data)


if __name__ == "__main__":
    main()