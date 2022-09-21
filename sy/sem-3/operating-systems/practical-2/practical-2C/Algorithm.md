## Problem Statement

Generate fibonacci series using threads.

## Algorithm (Revision 1)
1. Start
2. Data Structures
3. Procedure
4. End

## Algorithm (Revision 2)
1. Start
2. Input `n` for extend of the sequence
3. Initialize a `sorted_set`
4. Initialize a thread and perform the following to recursively calcualte the fibonacci series:
    i. Base Condition: If `n == 0` then return 0 or if `n == 1` return 1
    ii. Initialize thread `t1` to calculate fibonacci serice for `n - 1`
    iii. Initialize thread `t2` to calculate fibonacci serice for `n - 2`
    iv. Start threads `t1` and `t2`
    v. Add the results of both the threads and append it to the `sorted_set`
    vi. Repeat Steps i. to iii. until the condition of step i. is fullfilled
5. Print the elements of the `sorted_set`
6. End
