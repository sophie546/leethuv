class Solution {
    public int majorityElement(int[] nums) {
        int first = nums[0];
        int count =1;
        for(int i=1; i < nums.length; i++){
            if(first == nums[i]){
                count++;
            } else{
                count--;
                if(count == 0){
                    count=1;
                    first = nums[i];
                }
            }
        }
        return first;
    }
}