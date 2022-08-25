
class LevelOne {
    public void levelOneMethod() {
        System.out.println("This method exists in LevelOne class");
    }
}

class LevelTwo extends LevelOne {
    public void levelTwoMethod() {
        System.out.println("This method exists in LevelTwo class");
    }
}

class LevelThree extends LevelTwo {
    public void levelThreeMethod() {
        System.out.println("This method exists in LevelThree class");
    }
}

public class MultiLevelInheritance {
    public static void main(String args[]) {
        LevelThree obj = new LevelThree();
        obj.levelOneMethod();
        obj.levelTwoMethod();
        obj.levelThreeMethod();
    }
}
