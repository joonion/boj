import java.util.*;

public class Main {

    static char solve(String s) {
        String word = s.toUpperCase();
        int[] freq = new int[26];
        for (int i = 0; i < word.length(); i++)
            freq[word.charAt(i) - 'A']++;
    
        int best = Arrays.stream(freq).max().getAsInt();
        int answer = -1;
        for (int i = 0; i < 26; i++)
            if (freq[i] == best)
                if (answer != -1)
                    return '?';
                else
                    answer = i;
        return (char)('A' + answer);    
    }

    public static final void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        char answer = solve(s);
        System.out.println(answer);
        scanner.close();
    }
}