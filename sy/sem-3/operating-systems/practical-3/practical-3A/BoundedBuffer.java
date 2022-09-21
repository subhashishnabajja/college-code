import java.util.Random;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.Semaphore;

class Producer extends Thread {
	public int BUFFER_SIZE;
	public ArrayBlockingQueue<Integer> buffer;
	public Semaphore mutex, empty, full;

	public Producer(int BUFFER_SIZE, ArrayBlockingQueue<Integer> buffer, Semaphore mutex, Semaphore empty,
			Semaphore full) {
		this.BUFFER_SIZE = BUFFER_SIZE;
		this.buffer = buffer;
		this.mutex = mutex;
		this.empty = empty;
		this.full = full;
	}

	@Override
	public void run() {
		try {
			for (int i = 0; i <= 10; i++) {

				empty.acquire();
				mutex.acquire();

				buffer.add(i);

				System.out.println(buffer);

				mutex.release();
				full.release();

				sleep(2500);
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}

}

class Consumer extends Thread {
	public int BUFFER_SIZE;
	public ArrayBlockingQueue<Integer> buffer;
	public Semaphore mutex, empty, full;

	public Consumer(int BUFFER_SIZE, ArrayBlockingQueue<Integer> buffer, Semaphore mutex, Semaphore empty,
			Semaphore full) {
		this.BUFFER_SIZE = BUFFER_SIZE;
		this.buffer = buffer;
		this.mutex = mutex;
		this.empty = empty;
		this.full = full;
	}

	@Override
	public void run() {

		while (true) {
			try {

				this.full.acquire();
				this.mutex.acquire();

				System.out.println("Consumed :" + this.buffer.remove());

				this.mutex.release();
				this.empty.release();

				sleep(1000);

			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}

public class BoundedBuffer {
	public static void main(String args[]) {
		int n = 5;
		ArrayBlockingQueue<Integer> buffer = new ArrayBlockingQueue<Integer>(n);
		Semaphore mutex = new Semaphore(1);
		Semaphore empty = new Semaphore(n);
		Semaphore full = new Semaphore(0);

		Producer producer = new Producer(n, buffer, mutex, empty, full);
		Consumer consumer = new Consumer(n, buffer, mutex, empty, full);
		producer.start();
		consumer.start();

	}
}
