input = "interviewquery"
output = "i"

def char_check(s1):
    set_ck = set()
    for i in s1:
        if i in set_ck:
            return i
        else:
            set_ck.add(i)
    return None


def is_sequency(s1,s2):
    m = len(s1)
    n = len(s2)
    i = 0
    j = 0

    while i < m and j < n:
        if s1[i] == s2[j]:
            i += 1
        j += 1
    return i == m



import numpy as np
import matplotlib.pyplot as plt

# def generate_and_plot_normal_samples(N, mean=0, std_dev=1):
#     """
#     Generate N samples from a normal distribution with given mean and standard deviation,
#     and plot them on a histogram.

#     Parameters:
#     N (int): Number of samples to generate.
#     mean (float): Mean of the normal distribution.
#     std_dev (float): Standard deviation of the normal distribution.
#     """
#     # Generate N samples from a normal distribution
#     samples = np.random.normal(loc=mean, scale=std_dev, size=N)

#     # Plot the histogram
#     plt.hist(samples, bins=30, alpha=0.7, color='blue', edgecolor='black')

#     # Add titles and labels
#     plt.title('Histogram of Normally Distributed Samples')
#     plt.xlabel('Value')
#     plt.ylabel('Frequency')

#     # Show the plot
#     plt.show()

# Example usage
# generate_and_plot_normal_samples(1000)

def cal_dev(lst_dict):
    temp_dict = {}
    for i in lst_dict:
        key = i.get('key')
        values = i.get('values', [])
        # Calculate the standard deviation using numpy
        std_dev = round(np.std(values),2)
        temp_dict[key] = std_dev

    return temp_dict


from datetime import datetime, timedelta

def weekly_aggregation(timestamps):
    '''
    Given a list of timestamps in sequential order, 
    return a list of lists grouped by week (seven days) using the first timestamp as the starting point.
    exeample: ts = ['2019-01-01', '2019-01-02','2019-01-08', '2019-02-01', '2019-02-02','2019-02-05'],
    then output will be: [['2019-01-01', '2019-01-02'], ['2019-01-08'], ['2019-02-01', '2019-02-02'],['2019-02-05']]
    '''
    if not timestamps:
        return []

    datetime_list = [datetime.strptime(ts, '%Y-%m-%d') for ts in timestamps]
    grouped_weeks = []
    current_week = []
    start_date = datetime_list[0]
    end_date = start_date + timedelta(days=7)

    for dt in datetime_list:
        if dt < end_date:
            current_week.append(dt.strftime('%Y-%m-%d'))
        else:
            grouped_weeks.append(current_week)
            temp = (dt - end_date).days // 7
            start_date = start_date + timedelta(weeks = temp + 1)
            current_week = [dt.strftime('%Y-%m-%d')]
            end_date = start_date + timedelta(days=7)
    # Append the last week
    if current_week:
        grouped_weeks.append(current_week)
    
    return grouped_weeks
   

result = char_check(input)
print(result)

result2 = is_sequency("abk", "ahbgdc")
print(result2)

result3 = cal_dev([
    { 'key': 'list1', 'values': [4,5,2,3,4,5,2,3]},
    { 'key': 'list2', 'values': [1,1,34,12,40,3,9,7]}])
print(result3)

result4 = weekly_aggregation(['2019-01-01', '2019-01-02','2019-01-08', '2019-02-01', '2019-02-02','2019-02-05'])
print(result4)