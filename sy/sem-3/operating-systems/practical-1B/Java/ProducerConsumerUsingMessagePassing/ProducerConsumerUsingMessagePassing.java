
import java.util.Date;
import java.util.LinkedList;
import java.util.Queue;

class Producer extends Thread {

    private int MAX_SIZE = 10;
    private Queue<String> messageQueue = new LinkedList<String>();

    @Override
    public void run() {
        try {
            while (true) {
                this.putMessage(new Date().toString());

                sleep(((long) (Math.random() * 1000)));
            }
        } catch (InterruptedException ex) {
            System.out.println("Error Ocurred" + ex.getLocalizedMessage());

        }

    }

    public synchronized void putMessage(String message) {

        try {
            while (this.messageQueue.size() == MAX_SIZE) {
                wait();
            }

            messageQueue.add(message);
            notify();

        } catch (InterruptedException ex) {
            System.out.println("Error Ocurred" + ex.getLocalizedMessage());
        }
    }

    public synchronized String getMessage() {
        try {

            while (this.messageQueue.isEmpty()) {
                wait();
            }

            String message = this.messageQueue.remove();

            System.out.println("Recieved : " + message);

            notify();

            return message;

        } catch (InterruptedException ex) {
            System.out.println("Error Ocurred" + ex.getLocalizedMessage());
        }

        return null;
    }

}

class Consumer extends Thread {

    private Producer producer;

    Consumer(Producer producer) {
        this.producer = producer;
    }

    @Override
    public void run() {
        try {
            while (true) {
                String message = producer.getMessage();

                // sends a reply to producer got a message
                System.out.println("Got message: " + message);
                sleep(2000);
            }
        } catch (InterruptedException ex) {
            System.out.println("Error Ocurred" + ex.getLocalizedMessage());
        }

    }
}

public class ProducerConsumerUsingMessagePassing {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Producer producer = new Producer();
        producer.start();
        new Consumer(producer).start();
    }

}
