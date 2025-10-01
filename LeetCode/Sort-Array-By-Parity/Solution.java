class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int[] res = new int[nums.length];
        int count =0;
        for(int num : nums){
            if(num % 2 == 0){
                res[count++] = num;
            }
        }

        for(int num : nums){
            if(num % 2 != 0){
                res[count++] = num;
            }
        }

        return res;
    }
}