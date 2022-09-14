# Problem Statement

The reader writer problem is a problem in which there is a shared resource in the writer can write data to and reader can read data from. Multiple writers cannot write simultaneously, but multiple readers can read the same resource.

## Algorithm (Revision 1)

1. Start
2. Initialize data structures
3. Procedures
4. End

## Algorithm (Revision 2)

1. Start
2. Initialize `read_count = 0` and semaphores `rw_mutex = 1` for obtaining mutual exclusion between the reader and writer, `mutex = 1` for modifying `read_count`.
3. Set `rw_mutex--` and write data to the shared resource.
4. Set `rw_mutex++` to release mutex.
5. Set `mutex--` and set `read_count++` to indicate that a reader is reading from the shared resource.
6. If `read_count == 1` then set `rw_mutex--` to ensure that no writer can write to the shared resource and then set `mutex++` to release the mutex lock.
7. Read the data from the shared resource.
8. Set `mutex--` and set `read_count--` indicate the reading has been done.
9. If `read_count == 0` then set `rw_mutex++` to release the mutex lock, so that the writers can write to the shared resource.
10. End.
