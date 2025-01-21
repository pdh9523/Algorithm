import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    static StringBuffer sb = new StringBuffer();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] counter = new int[2000001];
        int N = Integer.parseInt(br.readLine());
        for (int i=0; i<N; i++) {
            int num = Integer.parseInt(br.readLine()) + 1000000;
            counter[num] ++;
        }

        for (int i=0; i<2000001; i++) {
            for (int j=0; j<counter[i]; j++) {
                sb.append(i-1000000).append("\n");
            }
        }

        System.out.println(sb);
    }
}