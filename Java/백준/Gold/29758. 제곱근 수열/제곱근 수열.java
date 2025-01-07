import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static StringBuffer sb = new StringBuffer();
    public static void main(String[] args) throws Exception { 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int tc = Integer.parseInt(st.nextToken());
        for (int t=0; t<tc; t++) {
            st = new StringTokenizer(br.readLine());
            
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            if (M>=6) {
                sb.append(0).append("\n");
                continue;
            }

            int[][] DP = new int[M][N+1];
            DP[0][N] = 1;

            for (int i=0; i<M-1; i++) {
                for (int j=N; j>1; j--) {
                    if (DP[i][j]>0) {
                        for (int k=1; k<=(int) Math.sqrt(j-1); k++) {
                            DP[i+1][k] += DP[i][j];
                        }
                    }
                }
            }
            sb.append(DP[M-1][1]).append("\n");
        }
        System.out.println(sb);
    }
}