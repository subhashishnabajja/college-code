# Problem statement

The first come first serve algorithm is a CPU scheduling algorithm in which the first process which requests for the CPU enters the CPU first.

# Algorithm (Revision 1)

1. Start
2. Initialize Datastructures
3. Procedure
4. End

# Algorithm (Revision 2)

1. Start
2. Initialize a `queue` to store the oncoming processes.
3. A new process is added to the tail of the `queue`.
4. If the CPU is idle then allocate the head of the `queue` to the CPU.
5. Repeat Step (4) until the `queue` is empty.
6. End
