import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = "0" + br.readLine();
        if (s.charAt(1) == '0') {
            System.out.println(0);
        } else {
            int[] DP = new int[s.length()];
            DP[0] = 1;
            DP[1] = 1;
            for (int i = 2; i < DP.length; i++) {
                if (Integer.parseInt(s.charAt(i) + "") > 0) {
                    DP[i] += DP[i - 1];
                }
                int tmp = Integer.parseInt(s.charAt(i - 1) + "" + s.charAt(i));
                if (10 <= tmp && tmp <= 26) {
                    DP[i] += DP[i - 2];
                }

                if (DP[i] == 0) {
                    break;
                }
                DP[i] %= 1000000;
            }
            System.out.println(DP[s.length() - 1]);
        }
    }
}