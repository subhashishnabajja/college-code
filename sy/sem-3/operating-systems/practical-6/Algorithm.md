# Problem Statement

The Round Robin algorithm is a CPU scheduling algorithm in which the process are selected in FCFS order but each process is not allowed to exceed a fixed time quantam. This algorithm is a preemptive algorithm.

## Algorithm (Revision 1)

1. Start
2. Initialize data structures
3. Procedures
4. End

## Algorithm (Revision 2)

1. Start
2. Initialize a FIFO `queue` to store all the processes and a constant `time_quantam`.
3. New processes are added to the tail of the `queue`.
4. The processes are select from the head of the `queue`.
5. If burst time of the process at the head of the `queue` is greater than the `time_quantam` then execute the process for constant `time_quantam` and then put the process back to the `queue`.
6. Execute the process at the head of the `queue`.
7. Repeat Step (4) to (6) until the `queue` is empty.
8. End
