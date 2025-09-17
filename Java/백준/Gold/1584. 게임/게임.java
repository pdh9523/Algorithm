import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static class Node implements Comparable<Node> {
        int dist;
        int x;
        int y;

        public Node(int dist, int x, int y) {
            this.dist = dist;
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Node o) {
            return this.dist - o.dist;
        }
    }

    public static int[] dx = new int[] {-1, 1, 0, 0};
    public static int[] dy = new int[] {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int size = 501;

        int[][] arr = new int[size][size];

        int a = Integer.parseInt(br.readLine());
        for (int i=0; i<a; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            if (x1 > x2) {
                int tmp = x1;
                x1 = x2;
                x2 = tmp;
            }
            if (y1 > y2) {
                int tmp = y1;
                y1 = y2;
                y2 = tmp;
            }

            for (int x=x1; x<x2+1; x++) {
                for (int y=y1; y<y2+1; y++) {
                    arr[x][y] = 1;
                }
            }
        }

        int b = Integer.parseInt(br.readLine());
        for (int i=0; i<b; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            if (x1 > x2) {
                int tmp = x1;
                x1 = x2;
                x2 = tmp;
            }
            if (y1 > y2) {
                int tmp = y1;
                y1 = y2;
                y2 = tmp;
            }

            for (int x=x1; x<x2+1; x++) {
                for (int y=y1; y<y2+1; y++) {
                    arr[x][y] = -1;
                }
            }
        }

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(0,0,0));

        int[][] distance = new int[size][size];
        for (int i=0; i<size; i++) {
            for (int j=0; j<size; j++) {
                distance[i][j] = Integer.MAX_VALUE;
            }
        }
        distance[0][0] = 0;

        while (!pq.isEmpty()) {
            Node now = pq.poll();
            int dist = now.dist;
            int x = now.x;
            int y = now.y;

            for (int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < size && 0 <= ny && ny < size) {
                    if (arr[nx][ny] == -1) continue;

                    if (distance[nx][ny] > dist + arr[nx][ny]) {
                        distance[nx][ny] = dist + arr[nx][ny];
                        pq.offer(new Node(distance[nx][ny], nx, ny));
                    }
                }
            }
        }
        System.out.println(distance[size-1][size-1] == Integer.MAX_VALUE ? -1 : distance[size-1][size-1]);
    }
}