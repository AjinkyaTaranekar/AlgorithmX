import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int k = input.nextInt();
        int sum = 0, max = -1000000000;
        for (int i = 0; i < n; i++) {
            int f = input.nextInt();
            int t = input.nextInt();
            if (t > k) {
                sum = f - (t - k);
            } else {
                sum = f;
            }

            if (sum >= max) {
                max = sum;
                sum = 0;
            } else {
                sum = 0;
            }
        }

        System.out.println(max);

    }
}