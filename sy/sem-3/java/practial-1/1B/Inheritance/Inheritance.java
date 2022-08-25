
class Parent {
    public void parentPrint() {
        System.out.println("Printing from Parent class");
    }

    public void methodToBeOveridden() {
        System.out.println("Original Method");
    }
}

class ChildOne extends Parent {
    public void childOnePrint() {
        System.out.println("Printing from ChildOne class");
    }

    public void methodToBeOveridden() {
        System.out.println("Method Overriden by ChildOne class");
    }
}

class ChildTwo extends ChildOne {
    public void childTwoPrint() {
        System.out.println("Printing from ChildTwo class");
    }

    public void methodToBeOveridden() {
        System.out.println("Method Overriden by ChildTwo class");
    }
}

public class Inheritance {
    public static void main(String[] args) {
        ChildTwo obj = new ChildTwo();

        obj.parentPrint();
        obj.childOnePrint();
        obj.childTwoPrint();

        Parent p1 = new Parent();
        ChildOne c1 = new ChildOne();
        ChildTwo c2 = new ChildTwo();

        p1.methodToBeOveridden();
        c1.methodToBeOveridden();
        c2.methodToBeOveridden();
    }

}
