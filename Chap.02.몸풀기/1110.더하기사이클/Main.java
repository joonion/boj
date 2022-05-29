import java.util.*;

public class Main {

    static int solve(int n) {
        int m = n;
        int cnt = 1;
        while (true) {
            int s = 0, t = m;
            while (t != 0) {
                s += t % 10;
                t /= 10;
            }
            m = (m % 10) * 10 + (s % 10);
            if (m == n)
                break;
            cnt++;
        }
        return cnt;        
    }

    public static final void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int answer = solve(N);
        System.out.println(answer);
        scanner.close();
    }
}