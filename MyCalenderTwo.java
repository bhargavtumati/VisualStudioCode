
import java.util.TreeMap;

class MyCalendarTwo {
    private TreeMap<Integer, Integer> delta; // Keeps track of the change in bookings

    public MyCalendarTwo() {
        delta = new TreeMap<>();
    }

    public boolean book(int start, int end) {
        // Update the delta for the start and end times
        delta.put(start, delta.getOrDefault(start, 0) + 1);
        delta.put(end, delta.getOrDefault(end, 0) - 1);

        int active = 0; // Number of active bookings
        for (int d : delta.values()) {
            active += d;
            if (active >= 3) {
                // Triple booking detected, revert the changes
                delta.put(start, delta.get(start) - 1);
                delta.put(end, delta.get(end) + 1);
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
        System.out.println(myCalendarTwo.book(10, 20)); // true
        System.out.println(myCalendarTwo.book(50, 60)); // true
        System.out.println(myCalendarTwo.book(10, 40)); // true
        System.out.println(myCalendarTwo.book(5, 15));  // false
        System.out.println(myCalendarTwo.book(5, 10));  // true
        System.out.println(myCalendarTwo.book(25, 55)); // true
    }
}
