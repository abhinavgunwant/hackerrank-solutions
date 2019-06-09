import java.io.*;
import java.util.*;

public class Sol{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = (new StringBuilder(A)).reverse().toString();
        System.out.println(B);
        if((new StringBuffer(A)).equals(new StringBuffer(B))){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}
