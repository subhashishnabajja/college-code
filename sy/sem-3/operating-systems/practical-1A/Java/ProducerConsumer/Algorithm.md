## Problem Statement

The producer consumer problem consists of two components: Producer and Consumer. The producer produces some value and store it in the shared section of the memory that is shared between the producer and the consumer.The consumer the consumes the data from the shared section of the memory.
The characteristics of the algorithm:

1. The algoritm used an unbounded buffer
2. The producer does not have to wait
3. The consumer has to wait if the buffer is empty

The algorithm must satify the following conditions:

1. Must prevent race condition between the producer and consumer
2. Implement mutual exclusion i.e ensure that only one process/thread could enter the critical section

## The algorithm block

1. Start
2. Data structures used
3. Producer produces the data
4. Consumer consumes the data

## The algorithm (Revision 1)

1. Start
2. Initialize a shared unbounded buffer and semaphore = 1
3. Decrement the semaphore to indicate that the producer has entered its critical section and to obtain mutual exclusion and then the producer writes data to the shared unbounded buffer and then increment the semaphore indicating that the producer has exited its critical section.
4. The consumer initially waits for the producer to produce some data.
5. Decrement the semaphore to indicate that the consumer has entered its critical section and then consume the data from the unbounded buffer. Then increment the semaphore to indicate that the consumer has exited its critical section
6. Stop

## The alogritm (Revision 2)

1. Start
2. Initialize a shared unbounded buffer and semaphore = 1.
3. Decrement the semaphore to indicate that the producer has entered its critical section and to obtain mutual exclusion.
4. The producer then produces the data and store it in the shared unbounded buffer.
5. Increment the semaphore to indicate that the producer has exited its mutual exclusion.
6. The consumer initially waits for the producer to produce some data.
7. Decrement the semaphore to indicate that the consumer has entered its critical section.
8. If the buffer has empty then wait for the producer.
9. Consume the data from the buffer and then increment the semaphore to indicate that the consumer has exited its critical section.
10. Stop
