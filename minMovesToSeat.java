import java.util.Arrays;
class minMovesToSeat {
    public int Solution(int[] seats, int[] students) {
        int count=0;
        Arrays.sort(seats);
        Arrays.sort(students);
      for(int i=0;i<students.length;i++){
            
          
          count+=  Math.abs(seats[i] - students[i]);
           
             
            }
          
        
return count;
    }
    public static void main(String[] args) {
      int  arr[]={3,1,5};
      int arr2[]={2,7,5};
      minMovesToSeat k = new minMovesToSeat();
System.out.println(k.Solution(arr, arr2));
    }
}