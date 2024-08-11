# using sorting method

# def arrangement(x):
#     x = sorted(x)
#     waiting_time = []
#     time = 0
#     for i in x:
#         waiting_time.append(time)
#         time += i
#     print(sum(waiting_time))
#
# arrangement([20, 15, 10])

# finding minimum treatment time and treating them first

# def arrangement(x):
#     queue_arrangement = []
#     total_time = 0
#     while len(x) != 0:
#         min = x[0]
#         for i in x:
#             if i < min:
#                 min = i
#         x.remove(min)
#         queue_arrangement.append(min)
#     time = 0
#     for i in queue_arrangement:
#         total_time += time
#         time += i
#     print(total_time)
#
# arrangement([20, 15, 10])

