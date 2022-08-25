/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package javaapplication5;

/**
 *
 * @author CS-15
 */

abstract class Animal{
    public abstract void printAnimal();
    public abstract void printHuman();
}


class Dog extends Animal{
    @Override
    public void printAnimal(){
        System.out.println("Printing from Dog");
    }

    @Override
    public void printHuman(){}
 
}

class Cat extends Animal{
    @Override
    public void printAnimal(){
        System.out.println("Printing from Cat");
    }

    @Override
    public void printHuman(){}
 
}


class Human extends Animal{
    @Override
    public void printAnimal(){
    }

    @Override
    public void printHuman(){
        System.out.println("Printing form Human");
    }
 
}





public class Abstraction {
    public static void main(String args[]){
        Dog dog = new Dog();
        Cat cat = new Cat();
        Human human = new Human();


        dog.printAnimal();
        cat.printAnimal();
        human.printHuman();
    }    
}
