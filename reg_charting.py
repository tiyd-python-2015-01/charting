import matplotlib.pyplot as plt
import statistics as st
import seaborn as sb
import random


def flip_coin():
    options = ['heads', 'tails']
    return random.choice(options)

def flip_multiple_coins(n = 100000):
    output_list =[]
    count_list = []
    count = 0
    total_flips = [flip_coin() for _ in range(n)]

    while 2 ** count <= n:
        total_count =(total_flips[:2 ** count].count('heads') ,
                      total_flips[:2 ** count].count('tails'))
        output_list.append(total_count)
        count_list.append(2 ** count)
        count += 1

    if 2 ** count != n:
        total_count =(total_flips.count('heads') , total_flips.count('tails'))
        output_list.append(total_count)
        count_list.append(n)

    return count_list, output_list

def heads_tails_ratio(a_list):
    count, total = a_list
    return [(heads / tails) for heads, tails in total]


def heads_tails_ratio_total(a_list):
    count, total = a_list
    head_count = 0
    tail_count = 0

    for heads, tails in total:
        head_count += heads
        tail_count += tails

    return head_count / tail_count

def trials_dif_ratio(trials=100000, flips = 100):
    return [heads_tails_ratio_total(flip_multiple_coins(flips))
            for _ in range(trials)]


# Graphing 100,000 trials of 100 flips on a histogram
#ratio_many_trials_100 = trials_dif_ratio(flips=100)
#mean = st.mean(ratio_many_trials_100)
#std = st.pstdev(ratio_many_trials_100)
#plt.hist(ratio_many_trials_100)
#ymin, ymax = plt.ylim()
#plt.title('100 flips per 100,000 trials')
#plt.vlines(mean, ymin, ymax)
#plt.vlines([(mean - std), (mean + std)], ymin, ymax, linestyles = 'dashed')
#plt.show()

# Graphing 100,000 trials of 100 flips on a box plot
#plt.boxplot(ratio_many_trials_100)
#plt.title('100 flips per 100,000 trials')
#plt.show()


# Graphing 100,000 trials of 1,000 flips
#ratio_many_trials_1000 = trials_dif_ratio(flips=1000)
#plt.hist(ratio_many_trials_1000)
#plt.title('1000 flips per 100,000 trials')
#plt.show()

# Graphing 100,000 trials of 1,000 flips on a box plot
#plt.boxplot(ratio_many_trials_100)
#plt.title('100 flips per 100,000 trials')
#plt.show()







def flip_multiple_coins_dif(n = 100000):
    output_list =[]
    count_list = []
    count = 0
    total_flips = [flip_coin() for _ in range(n)]

    while 2 ** count <= n:
        total_heads_count = total_flips[:2 ** count].count('heads')
        total_tails_count = total_flips[:2 ** count].count('tails')
        if total_tails_count == 0:
            total_tails_count +=1

        output_list.append((total_heads_count -
                            total_tails_count) / total_tails_count)
        count_list.append(2 ** count)
        count += 1

    if 2 ** count != n:
        total_heads_count = total_flips[:2 ** count].count('heads')
        total_tails_count = total_flips[:2 ** count].count('tails')

        output_list.append(total_heads_count / total_tails_count)
        count_list.append(n)

    return output_list

def trials_dif_ratio_simple(trials=100000, flips = 100):
    return [flip_multiple_coins_dif(flips) for _ in range(trials)]

def transpose_results(a_list_of_lists):
    new_list = list(zip(*a_list_of_lists))
    return new_list

def mean_passed_list(passed_list):
    passed_list = transpose_results(passed_list)
    return [st.mean(a_list) for a_list in passed_list]

def str_passed_list(passed_list):
    passed_list = transpose_results(passed_list)
    return [st.pstdev(a_list) for a_list in passed_list]


#mean_ratio = mean_passed_list(trials_dif_ratio_simple())
flip_count, output_list = flip_multiple_coins(100)

#plt.scatter(flip_count, mean_ratio)
#plt.title('Mean of Heads/Tails difference per level')
#plt.xscale('log')
#plt.xlabel('exponential intervals: 2** x')
#plt.ylabel('mean at each interval')
#plt.show()

mean_std = str_passed_list(trials_dif_ratio_simple())

plt.scatter(flip_count, mean_std)
plt.title('Standard deviation of Heads/Tails difference per level')
plt.xscale('log')
plt.xlabel('exponential intervals: 2** x')
plt.ylabel('standard deviation at each interval')
plt.show()
