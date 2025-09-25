class Solution {
    public int smallestRangeI(int[] nums, int k) {
       int maxVal = Integer.MIN_VALUE;
       int minVal = Integer.MAX_VALUE;

       for(int num : nums){
            if(maxVal < num){
                maxVal = num;
            } 
            if(minVal > num){
                minVal = num;
            }
       }
        int score = (maxVal - minVal) - 2*k;
        return Math.max(0,score);     
    }
}
