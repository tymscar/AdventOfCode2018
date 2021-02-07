package com.tymscar.day01;

import java.io.File;
import java.io.FileNotFoundException;
import java.net.URL;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
        System.out.println("Part1: " + part1());
        System.out.println("Part2: " + part2());
    }

    private static int part1() throws FileNotFoundException{
        URL url = Main.class.getResource("input.txt");
        File inputFile = new File(url.getPath());
        Scanner inputScanner = new Scanner(inputFile);

        int sum = 0;

        String input = inputScanner.nextLine();
        for (int i = 0; i < input.length() - 1; i++) {
            if(input.charAt(i) == input.charAt(i+1)){
                sum += Integer.parseInt(String.valueOf(input.charAt(i)));
            }
        }

        if(input.charAt(input.length()-1) == input.charAt(0)){
            sum += Integer.parseInt(String.valueOf(input.charAt(0)));
        }

        return sum;
    }

    private static int part2() throws FileNotFoundException{
        URL url = Main.class.getResource("input.txt");
        File inputFile = new File(url.getPath());
        Scanner inputScanner = new Scanner(inputFile);

        int sum = 0;

        String input = inputScanner.nextLine();
        for (int i = 0; i < input.length(); i++) {
            int whereToCheck = (i + (input.length()/2)) % input.length();
            if(input.charAt(i) == input.charAt(whereToCheck)){
                sum += Integer.parseInt(String.valueOf(input.charAt(i)));
            }
        }

        return sum;
    }
}
