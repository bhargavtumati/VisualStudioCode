import java.util.ArrayList;
import java.util.List;

class MyCalendar {
    private List<int[]> events;

    public MyCalendar() {
        events = new ArrayList<>();
    }

    public boolean book(int start, int end) {
        for (int[] event : events) {
            int eventStart = event[0];
            int eventEnd = event[1];
            if (start < eventEnd && end > eventStart) {
                // Overlapping events, cannot book
                return false;
            }
        }
        events.add(new int[]{start, end});
        return true;
    }


// Example usage

    public static void main(String[] args) {
        MyCalendar calendar = new MyCalendar();
        System.out.println(calendar.book(10, 20)); // true
        System.out.println(calendar.book(15, 25)); // false (overlaps with [10, 20])
        System.out.println(calendar.book(20, 30)); // true
    }
}
