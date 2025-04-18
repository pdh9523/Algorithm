import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class Main {

    public static void main(String[] args) throws Exception {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

         int N = Integer.parseInt(br.readLine());
         int[] arr = new int[N];
         for (int i=0; i<N; i++) {
             arr[i] = Integer.parseInt(br.readLine());
         }

         ArrayList<Integer> DP = new ArrayList<>();
         for (int num: arr) {
             if (DP.isEmpty() || DP.get(DP.size() -1) < num) {
                 DP.add(num);
             } else {
                 DP.set(binarySearch(DP, num), num);
             }
         }

        System.out.println(N - DP.size());

    }

    static int binarySearch(ArrayList<Integer> arr, int target) {
        int left = 0, right = arr.size();
        while (left <= right) {
            int mid = (left + right) / 2;
            if (arr.get(mid) == target) {
                return mid;
            }

            if (arr.get(mid) < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}