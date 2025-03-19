import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

    static StringBuffer sb = new StringBuffer();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        String[] arr = br.readLine().split(" ");
        Arrays.sort(arr,(a, b)
                -> b.repeat(10).compareTo(a.repeat(10))
                );
        for (int i=0; i<N; i++) {
            sb.append(arr[i]);
        }
        if (sb.toString().charAt(0) == '0') {
            System.out.println("0");
        } else {
            System.out.println(sb);
        }
    }
}