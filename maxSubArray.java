class maxSubArray {
    public int Solution(int[] nums) {
        int maxSum = Integer.MIN_VALUE; // Initialize maxSum to negative infinity
        int currentSum = 0;

        for (int num : nums) {
            currentSum = Math.max(num, currentSum + num);
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum; 
    }

   public static void main(String args[]){
    int ar[]={-2,-3,-1};
maxSubArray ms=new maxSubArray();
System.out.println(ms.Solution(ar));
   } 
}