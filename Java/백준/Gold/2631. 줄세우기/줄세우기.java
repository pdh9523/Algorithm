import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {

    public static void main(String[] args) throws Exception {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

         int N = Integer.parseInt(br.readLine());
         int[] arr = new int[N];
         int[] DP = new int[N];

         for (int i=0; i<N; i++) {
             arr[i] = Integer.parseInt(br.readLine());
             DP[i] = 1;
         }

        for (int i=1; i<N; i++) {
            for (int j=0; j<i; j++) {
                if (arr[j] < arr[i]) {
                    DP[i] = Math.max(DP[i], DP[j] + 1);
                }
            }
        }
        System.out.println(N-max(DP));
    }

    static int max(int[] arr) {
        int res = 0;
        for (int i=0; i<arr.length; i++) {
            if (res < arr[i]) {
                res = arr[i];
            }
        }
        return res;
    }
}