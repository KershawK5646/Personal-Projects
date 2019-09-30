/*
 * This program will randomly generate a number and the user will guess it.
 */
package guessthenumber;

import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author kyler
 */
public class GuessTheNumber {

    /**
     * @param args the command line arguments
     */
    
    public static void intro(){
        System.out.print("Welcome to the guess the number game: \n");
    }
    
    public static void formatting(){
        System.out.print("========================================\n");
    }
    
    public static Integer getGuessFromUser(){
        Integer userGuess;
        
        // Construct a new Scanner
        Scanner kb = new Scanner(System.in);
        
        // Get a number from the user.
        while (true){
            try{
                System.out.print("Guess a number between 1 and 100: \n");
                userGuess = Integer.parseInt(kb.nextLine());
                break;
            }
            catch(NumberFormatException e){
                System.out.print("Invalid input. please enter a number. \n");
            }
        }
        
        // return the guess
        return userGuess;
    }
    
    public static void game(){
        // Variables
        int randomNumber =0;
        int userGuess;
        Boolean gameOver = false;

        
        // Needed Objects
        Scanner kb = new Scanner(System.in);
        Random generator = new Random();
        
        // Create random number
        randomNumber = generator.nextInt(99)+1;
        
        while (gameOver == false){
            userGuess = 0;
            // Get the user guess
            while (userGuess == 0){
                userGuess = getGuessFromUser();            
            }

            // Evaluate the users guess.
            if (userGuess == randomNumber){
                System.out.print("Congrats! You guessed the number!!!\n");
                gameOver = true;
            }
            else if (userGuess > randomNumber){
                System.out.print("Too high...Try again!\n");
                gameOver = false;
            }
            else{
                System.out.print("Too low...Try again!\n");
                gameOver = false;
            }
        }

        
    }
    
    public static void main(String[] args) {
        
        // startup
        intro();
        formatting();
        game();
    }
    
}
