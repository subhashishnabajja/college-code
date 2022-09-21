import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Semaphore;

class Producer extends Thread {

    private List<Integer> buffer;
    private Semaphore semaphore;

    Producer(List<Integer> buffer, Semaphore semaphore) {
        this.buffer = buffer;
        this.semaphore = semaphore;
    }

    @Override
    public void run() {
        for (int i = 1; i <= 50; i++) {
            try {
                this.semaphore.acquire(); // Acquire lock
                System.out.println("Produced: " + i);
                this.buffer.add(i);

                this.semaphore.release();
                Thread.sleep((long) (Math.random() * 1000));
            } catch (InterruptedException e) {
                System.out.println("An error ocurred" + e.getLocalizedMessage());
            }

        }

    }
}

class Consumer extends Thread {

    private List<Integer> buffer;
    private Semaphore semaphore;

    Consumer(List<Integer> buffer, Semaphore semaphore) {
        this.buffer = buffer;
        this.semaphore = semaphore;
    }

    @Override
    public void run() {
        while (true) {
            try {
                this.semaphore.acquire();
                System.out.println("Buffer size :" + this.buffer.size());
                if (!this.buffer.isEmpty()) {
                    int data = this.buffer.get(this.buffer.size() - 1);
                    System.out.println("Consumed : " + data);
                    this.buffer.remove(this.buffer.size() - 1);
                }
                this.semaphore.release();
                Thread.sleep((long) (Math.random() * 1000));
            } catch (InterruptedException e) {
                System.out.println("An error ocurred" + e.getLocalizedMessage());
            }
        }
    }
}

public class ProducerConsumerUsingSharedMemory {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        List<Integer> sharedbuffer = new ArrayList<Integer>(10);
        Semaphore semaphore = new Semaphore(1);

        Producer producer = new Producer(sharedbuffer, semaphore);
        Consumer consumer = new Consumer(sharedbuffer, semaphore);

        producer.start();
        consumer.start();

    }

}
