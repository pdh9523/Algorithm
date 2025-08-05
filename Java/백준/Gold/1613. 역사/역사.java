import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        boolean[][] distance = new boolean[N+1][N+1];

        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            distance[a][b] = true;
        }

        for (int k=1; k<N+1; k++) {
            for (int i=1; i<N+1; i++) {
                for (int j=1; j<N+1; j++) {
                    distance[i][j] = distance[i][j] || (distance[i][k] && distance[k][j]);
                }
            }
        }
        int Q = Integer.parseInt(br.readLine());
        for (int i=0; i<Q; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            boolean ans = distance[s][e];
            boolean ansReversed = distance[e][s];

            if (ans) {
                System.out.println(-1);
            } else if (ansReversed) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }
}