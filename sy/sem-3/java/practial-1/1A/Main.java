package javaapplication5;


class Parent{
   public void parentPrint(){
       System.out.println("Printing from Parent class");    
   }
}

class ChildOne extends Parent{
   public void childOnePrint(){
       System.out.println("Printing from ChildOne class");
   }
}

class ChildTwo extends ChildOne{
    public void childTwoPrint(){
        System.out.println("Printing from ChildTwo class");
    }
}


public class JavaApplication5 {
    public static void main(String[] args) {
        ChildTwo obj = new ChildTwo();

        obj.parentPrint();
        obj.childOnePrint();
        obj.childTwoPrint();
    }
    
}
