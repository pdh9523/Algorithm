import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        String[] arr = new String[N];
        for (int i=0; i<N; i++) {
            String word = br.readLine();
            arr[i] = word;
            K -= word.length();
        }

        StringBuilder sb = new StringBuilder();

        int[] cnt = new int[N];
        for (int i=1; i<N; i++) {
            int tmp;
            if (arr[i].charAt(0) > '_') {
                tmp = (K - 1) / (N - i) + 1;
            } else {
                tmp = K / (N - i);
            }
            cnt[i] = tmp;
            K -= tmp;
        }

        for (int i=0; i<N; i++) {
            sb.append("_".repeat(cnt[i]));
            sb.append(arr[i]);
        }
        System.out.println(sb);
    }
}