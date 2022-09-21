number_of_processes = 5
number_of_resources = 3

resource_instances = [10, 5, 7]


def calculate_need(allocated, max):
    global number_of_processes, number_of_resources, resource_instances

    need = [[0 for i in range(number_of_resources)]
            for i in range(number_of_processes)]
    for i in range(number_of_processes):
        for j in range(number_of_resources):

            need[i][j] = max[i][j] - allocated[i][j]

    return need


def calculate_available(allocated):
    global number_of_processes, number_of_resources, resource_instances

    available = [0 for i in range(number_of_resources)]
    sum = [0 for i in range(number_of_resources)]
    for i in range(number_of_processes):
        for j in range(number_of_resources):
            sum[j] += allocated[i][j]

    for i in range(number_of_resources):
        available[i] = resource_instances[i] - sum[i]

    return available


allocated = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
max = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]

need = calculate_need(allocated, max)

available = calculate_available(allocated)

to_do = available  # 1 x m
finished_process = [0 for i in range(number_of_processes)]
answers = [0 for i in range(number_of_processes)]
index = 0

for k in range(number_of_processes):
    for i in range(number_of_processes):
        if finished_process[i] == 0:

            flag = 0

            for x in range(number_of_resources):
                if (need[i][x] > available[x]):
                    flag = 1
                    break

            if (flag == 0):
                answers[index] = i
                index += 1

                for y in range(number_of_resources):
                    available[y] += allocated[i][y]
                finished_process[i] = 1

print("Following is the SAFE Sequence", answers)

for i in range(number_of_processes - 1):
    print(" P", answers[i], " ->", sep="", end="")
print(" P", answers[number_of_processes - 1], sep="")