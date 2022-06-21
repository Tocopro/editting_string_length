
package com.company;
import java.io.*;
import java.io.FileWriter;
import java.util.Scanner;

public class Main {

    public static <Int> void main(String[] args) throws FileNotFoundException {
        File text_file;
        try {
            text_file = new File("C:\\Users\\NEAK\\Documents\\Text\\Composing_text.txt");
            if (text_file.createNewFile()) {
                System.out.println("File Created: " + text_file);
            } else {
                System.out.println("File already Exists");
            }
        } catch (IOException e) {
            System.out.println("An Error Occurred");
            e.printStackTrace();
        }
        int count = 0;
        String line_edit = "";
        try
        {
            FileReader reading = new FileReader("C:\\Users\\NEAK\\Documents\\Text\\Composing_text.txt");
            Scanner line = new Scanner(new File("C:\\Users\\NEAK\\Documents\\Text\\Composing_text.txt"));
            FileWriter edit = new FileWriter("C:\\Users\\NEAK\\Documents\\Text\\Edited_text.txt");
            while (line.hasNextLine())
            {
                String line_text = line.nextLine();
                String [] text_words = line_text.split(" ");

                for (String new_line : text_words)
                {
                    int measure = new_line.length();
                    if (measure > 15)
                    {
                        edit.write("\n");
                        System.out.println(new_line.length());
                        measure = 0;
                    }
                    else
                    {
                        edit.write( new_line + " " );
                    }
                }
            }
            edit.close();
    }catch (IOException e)
        {
            e.printStackTrace();
        }
    }
}
