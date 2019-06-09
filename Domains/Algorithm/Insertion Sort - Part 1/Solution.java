import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void printArr(int[] arr){
        for(int i : arr){
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void insertIntoSorted(int[] ar) {
        int temp = -20000, j;
        for(int i=ar.length-1; i>1; --i){
            if(ar[i] < ar[i-1]){
                temp = ar[i];
                j = i;

                try{
                    while(temp < ar[j-1] && j > 0){
                        ar[j] = ar[j-1];
                        printArr(ar);
                        --j;
                    }
                }catch(ArrayIndexOutOfBoundsException e){
                    // nothing here!!!!
                }
                ar[j] = temp;
                printArr(ar);
                temp = -20000;
                i = j+1;
            }else if(temp != -20000 && temp < ar[i]){
                ar[i] = temp;
                printArr(ar);
            }
        }
    }


/* Tail starts here */
     public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();
        int[] ar = new int[s];
         for(int i=0;i<s;i++){
            ar[i]=in.nextInt();
         }
         insertIntoSorted(ar);
    }


    private static void printArray(int[] ar) {
      for(int n: ar){
         System.out.print(n+" ");
      }
        System.out.println("");
   }


}
