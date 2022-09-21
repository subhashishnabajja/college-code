import numpy as np

n_processes = int(input('Number of processes? '))
n_resources = int(input('Number of resources? '))

available_resources = [int(x) for x in input('Claim vector? ').split(' ')]

currently_allocated = np.array([[
    int(x)
    for x in input(f'Currently allocated for process {i + 1}? ').split(' ')
] for i in range(n_processes)])
max_demand = np.array([[
    int(x) for x in input(f'Maximum demand from process {i + 1}? ').split(' ')
] for i in range(n_processes)])

total_available = available_resources - np.sum(currently_allocated, axis=0)

running = np.ones(
    n_processes
)  # An array with n_processes 1's to indicate if process is yet to run

while np.count_nonzero(running) > 0:
    at_least_one_allocated = False
    for p in range(n_processes):
        if running[p]:
            if all(i >= 0 for i in total_available -
                   (max_demand[p] - currently_allocated[p])):
                at_least_one_allocated = True
                print(f'{p} is running')
                running[p] = 0
                total_available += currently_allocated[p]
    if not at_least_one_allocated:
        print('Unsafe')
        break  # exit
else:
    print('Safe')