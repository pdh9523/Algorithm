import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        int start = 0, end = 10000*100000, ans = 0;
        while (start <= end) {
            int mid = (start + end) / 2;

            if (check(mid, M, arr)) {
                end = mid - 1;
                ans = mid;
            } else {
                start = mid + 1;
            }
        }
        System.out.println(ans);
    }

    private static boolean check(int n, int m, int[] arr) {
        int tmp = 0;
        int cnt = 0;
        for (int a : arr) {

            if (a > n) {
                return false;
            }

            if (tmp + a > n) {
                tmp = 0;
                cnt++;
            }
            tmp += a;
        }
        if (tmp > 0) {
            cnt ++;
        }
        return cnt <= m;
    }
}