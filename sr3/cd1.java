package sr3;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long k = sc.nextLong();
        long x = sc.nextLong();

        // Smallest n such that no valid string exists
        long n = k * x + 1;

        System.out.println(n);
        sc.close();
    }
}
