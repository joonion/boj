import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] A = new int[N][M];
        for (int i = 0; i < N; i++) {
            StringTokenizer st2 = new StringTokenizer(reader.readLine());
            for (int j = 0; j < M; j++)
                A[i][j] = Integer.parseInt(st2.nextToken());
        }
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                System.out.println(A[i][j] + " ");
    }
}
