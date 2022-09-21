## Problem Statement

The bounded buffer problem is a classical problem including producer and consumers.

## Algoritm (Blocking)
1. Start
2. Initialize data structures
3. Procedure
4. End

## Algorithm (Revision 1)

1. Start
2. Initialize a `bounded_buffer` to store the data, `BUFFER_SIZE` to indicate the maximum size of the buffer, and semaphores `mutex = 1` for mutual exclusion, `empty = BUFFER_SIZE` to count the number of empty buffers and `full = 0` to count the number of full buffers
3. Set `empty--`  and `mutex--` to obtain mutual exclusion and then the producer produces the data and places it in the `bound_buffer`
4. Set `mutex++` to release mutex and `full++`
5. Set `full--` and `mutex--` to obtain mutual exclusion and then the consumer consumes the data from the `bounded_buffer`.
6. Set `mutex++` to release the mutex and `empty++`
7. End