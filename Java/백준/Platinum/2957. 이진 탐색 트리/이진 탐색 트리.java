import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.TreeMap;

public class Main {

    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        TreeMap<Integer, Integer> map = new TreeMap<>();

        map.put(0,-1);
        map.put(N+1,-1);
        long ans = 0;
        for (int i=0; i<N; i++) {
            int x = Integer.parseInt(br.readLine());

            Integer lowerKey = map.lowerKey(x);
            Integer upperKey = map.higherKey(x);

            int leftDepth = map.get(lowerKey);
            int rightDepth = map.get(upperKey);

            int depth = Math.max(leftDepth, rightDepth) + 1;
            map.put(x, depth);

            ans += depth;
            sb.append(ans).append("\n");
        }
        System.out.println(sb);
    }
}
