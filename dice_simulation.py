import random
import seaborn
import math
import statistics as st
import matplotlib.pyplot as plt


def flipcoin():
    coin = ["H", "T"]
    return random.choice(coin)


def flip_simulation(n=100000):
    obs_to_store = [pow(2, num) for num in range(n) if pow(2, num) <= n]
    flip_counts = []
    counter = {'Heads': 0, 'Tails': 0}
    for flip in range(1, n+1):
        result = flipcoin()
        if result == "H":
            counter['Heads'] += 1
        elif result == "T":
            counter['Tails'] += 1
        if flip in obs_to_store:
            flip_counts.append(dict(counter))
    flip_counts.append(dict(counter))
    return flip_counts


def head_minus_tail(object_list):
    return [object_list[ind]['Heads'] - object_list[ind]['Tails']
            for ind in range(0, len(object_list))]


def ratios(object_list):
    return ([object_list[ind]['Heads'] /
            (object_list[ind]['Tails'] + object_list[ind]['Heads'])
            for ind in range(0, len(object_list))])


def line_plot(object_list, xlabel, ylabel, title):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot(object_list)
    plt.show()


def log_line_plot(object_list, title, x=True, y=False):
    plt.plot(object_list, 'bo')
    if x:
        plt.xscale('log')
    if y:
        plt.yscale('log')
    plt.title(title)
    plt.show()


def run_trial(trials, flips):
    return [flip_simulation(flips)
            for flip in range(trials)]


def trial_ratio(trial_object_list):
    return [ratios(trial_object_list[trial])
            for trial in range(len(trial_object_list))]


def means(all_list):
    return [st.mean(all_list[ratio])
            for ratio in range(len(all_list))]


def std_dev(all_list):
    return [st.stdev(all_list[ratio])
            for ratio in range(len(all_list))]


def histogram(list_to_plot, title):
    plt.hist(list_to_plot)
    plt.xlabel("Number")
    plt.ylabel("frequency")
    plt.title(title)
    plt.show()


def box_plot(list_to_plot, title, xticks):
    plt.boxplot(list_to_plot)
    plt.title(title)
    plt.xticks(range(1, len(list_to_plot)), xticks)
    plt.show()


def box_plot_seaborn(list_to_plot):
    sns.set_style("whitegrid")
    data = list_to_plot
    sns.boxplot(data)

if __name__ == '__main__':
    heads_tails = flip_simulation(100000)
    diff_head_tail = head_minus_tail(heads_tails)
    ratio_head_tail = ratios(heads_tails)
    # Charts
    line_plot(diff_head_tail, "Obs#", "Difference", "100,000 Coin Flips")
    line_plot(ratio_head_tail, "Obs#", "Heads Ratio", "100,000 Coin Flips")
    log_line_plot(diff_head_tail, "Log Scale - 100,000 Coin Flips")
    log_line_plot(ratio_head_tail, "Log Scale - 100,000 Coin Flips")

    trials = run_trial(20, 100000)
    trial_ratios = trial_ratio(trials)
    ratio_means = means(trial_ratios)
    ratio_std = std_dev(trial_ratios)
    log_line_plot(ratio_means, "Means")
    log_line_plot(ratio_std, "Standard Deviations", y=True)

    trials100 = run_trial(100000, 100)
    trial_ratios100 = trial_ratio(trials100)
    means100 = means(trial_ratios100)
    histogram(means100, "Histogram for 100,000 Trials of 100 flips")
    trials1000 = run_trial(100000, 1000)
    trial_ratios1000 = trial_ratio(trials1000)
    means1000 = means(trial_ratios1000)
    histogram(means1000, "Histogram for 100,000 Trials of 1000 flips")
    box_plot([means100, means1000], "Box Plot",  ["100 flips", "1000 flips"])
