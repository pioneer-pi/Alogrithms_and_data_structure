'''
Suppose that there are n jobs that need to use a meeting room,
the ith job occupies the meeting room in the time interval [si, fi).
please make an optimal schedule to arrange jobs as much as possible for the meeting room using a greedy approach.
You are asked to give which jobs can be arranged in the meeting room compatibly and the maximum number of these jobs.
'''
# a is list of jobs, which are presented by time intervals.
def job_selection(a):
    Choose = []
    length = len(a)
    Choose.append(a[0])
    k = 0
    for i in range(1,length):
        if a[i][0] >= a[k][1]:
            Choose.append(a[i])
            k = i
    return Choose

a = [(1, 4), (3, 5), (4, 6), (5, 7), (6, 9)]
print(job_selection(a))