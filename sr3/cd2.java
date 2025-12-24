import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    
    // Using a global reader to simplify method calls
    static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        // Read number of test cases
        String line = reader.readLine();
        if (line == null) return;
        
        int testCount = Integer.parseInt(line.trim());
        StringBuilder outputBuffer = new StringBuilder();

        // Loop through each test case
        for (int i = 0; i < testCount; i++) {
            long result = solve();
            outputBuffer.append(result).append("\n");
        }

        System.out.print(outputBuffer);
    }

    private static long solve() throws IOException {
        int n = Integer.parseInt(reader.readLine().trim());
        int[] values = new int[n];
        
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < n; i++) {
            values[i] = Integer.parseInt(tokenizer.nextToken());
        }

        // 1. Calculate the initial sum of differences for the full array
        long currentTotalDiff = 0;
        for (int i = 0; i < n - 1; i++) {
            currentTotalDiff += Math.abs(values[i] - values[i + 1]);
        }

        // If array is too small to have a "middle", return 0 (though constraints usually prevent this)
        if (n <= 1) return 0;

        long minDiffAfterRemoval = currentTotalDiff;

        // 2. Check removal of the first element
        long tempTotal = currentTotalDiff - Math.abs(values[0] - values[1]);
        if (tempTotal < minDiffAfterRemoval) {
            minDiffAfterRemoval = tempTotal;
        }

        // 3. Check removal of the last element
        tempTotal = currentTotalDiff - Math.abs(values[n - 1] - values[n - 2]);
        if (tempTotal < minDiffAfterRemoval) {
            minDiffAfterRemoval = tempTotal;
        }

        // 4. Check removal of any middle element
        // Logic: Remove connections to neighbors, add connection between neighbors
        for (int i = 1; i < n - 1; i++) {
            long oldConnection = Math.abs(values[i] - values[i - 1]) + Math.abs(values[i] - values[i + 1]);
            long newConnection = Math.abs(values[i - 1] - values[i + 1]);
            
            long adjustedTotal = currentTotalDiff - oldConnection + newConnection;
            
            if (adjustedTotal < minDiffAfterRemoval) {
                minDiffAfterRemoval = adjustedTotal;
            }
        }

        return minDiffAfterRemoval;
    }
}