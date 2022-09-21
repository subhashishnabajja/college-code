## Problem statement

In the producer consumer problem the producer produces some data and the consumer consumes the data. The producer and consumer running at different rates creates a problem of synchronization.

The problem is solved using message passing

## The algorithm (Revision 1)

1. Start
2. Data structure initialization
3. Producer produces the message
4. Consumer consumes the message
5. Stop

## The algorithm (Revision 2)

1. Start
2. Initialize a producer with a fixed size message queue that is used to store the messages.
3. The producer then produces a message and then places the in the message queue.
4. If the message queue is full then the producer waits for the consumer.
5. The consumer reads the message from the message queue.
6. If the message queue is empty then the consumer has to wait for the producer.
7. Stop
