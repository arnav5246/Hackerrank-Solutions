import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
    Scanner io = new Scanner(System.in);
        int i=0;
        while(io.hasNextLine())
        {
            String s = io.nextLine();
            if (s.contains("end-of-file"))
            {
                i++;
                System.out.println(i+" "+s);
                break;
            }
            else
            {
                i++;
                System.out.println(i+" " +s);       
            }
        }
        
    }
}
