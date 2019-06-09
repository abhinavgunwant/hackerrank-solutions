import java.io.*;
import java.util.*;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";

        int len = s.length();
        int p = len - k;
        ArrayList<String> strList = new ArrayList<String>();

        for(int i=0; i<=p; ++i){
            strList.add(s.substring(i, i+k));
        }

        Object sArr[] = strList.toArray();
        Arrays.sort(sArr);
        smallest = (String)sArr[0];
        largest = (String)sArr[sArr.length-1];
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}
