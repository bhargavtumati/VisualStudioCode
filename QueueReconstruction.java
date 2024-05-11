import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class QueueReconstruction {
    public int[][] reconstructQueue(int[][] people) {
        // Sort people in descending order of height and ascending order of ki
        Arrays.sort(people, (a, b) -> {
            if (a[0] != b[0]) {
                return b[0] - a[0];//sort by height(taller first)
            } else {
                return a[1] - b[1];//sort by number ki (smaller ki first)
            }
        });

        // Initialize an empty queue
        List<int[]> queue = new ArrayList<>();

        // Insert each person into the queue at the specified position
        for (int[] p : people) {
            queue.add(p[1], p);
        }

        // Convert List to array
        return queue.toArray(new int[people.length][]);
    }

    public static void main(String[] args) {
        QueueReconstruction solution = new QueueReconstruction();
        int[][] people1 = {{7, 0}, {4, 4}, {7, 1}, {5, 0}, {6, 1}, {5, 2}};
        int[][] result1 = solution.reconstructQueue(people1);
        System.out.println(Arrays.deepToString(result1));

        int[][] people2 = {{6, 0}, {5, 0}, {4, 0}, {3, 2}, {2, 2}, {1, 4}};
        int[][] result2 = solution.reconstructQueue(people2);
        System.out.println(Arrays.deepToString(result2));
    }
}