public class MultiThreaded{
    public static void main(String args[]){
        Thread t1 = new Thread(new Runnable(){
            @Override
            public void run(){
                for (int i = 1; i <= 10; i++){
                    System.out.println(i);
                }
            }
        })

    }

}