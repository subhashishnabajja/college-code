
import java.util.HashSet;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;

class FibonacciSequence {

    public SortedSet<Integer> seq = new TreeSet();

    public synchronized void addNumber(int number) {
        this.seq.add(number);
    }

    public synchronized void printSequence() {

        System.out.println(this.seq);

    }
}

class Fibonacci extends Thread {

    public int x;
    public int solution;
    public FibonacciSequence seq;

    public Fibonacci(int x, FibonacciSequence seq) {
        this.x = x;
        this.seq = seq;

    }

    @Override
    public void run() {
        if (this.x == 0) {
            this.solution = 0;

        } else if (this.x == 1) {
            this.solution = 1;
        } else {
            try {
                Fibonacci f1 = new Fibonacci(this.x - 1, this.seq);
                Fibonacci f2 = new Fibonacci(this.x - 2, this.seq);

                f1.start();
                f2.start();

                f1.join();
                f2.join();
                System.out.println(f1.solution);
                System.out.println(f2.solution);
                this.solution = f1.solution + f2.solution;

            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
        }

        this.seq.addNumber(this.solution);
    }

}

public class MultiThreadedFib {

    public static void main(String args[]) throws InterruptedException {
        FibonacciSequence fibonacciSequence = new FibonacciSequence();

        Fibonacci fib = new Fibonacci(8, fibonacciSequence);

        fib.start();
        
        fib.join();

        fibonacciSequence.printSequence();

    }
}
