class Solution {
    public int firstMissingPositive(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        for(int num : nums){
            set.add(num);
        }
        for(int i = 1; i < nums.length + 2; i++){
            if(!set.contains(i)){
                return i;
            }
        }

        return 0;
    }
}