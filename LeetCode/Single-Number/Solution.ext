class Solution {
    public int singleNumber(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        int sumAll =0, uniqueSum =0;

        for(int num : nums){
            if(!set.contains(num)){
                set.add(num);
                uniqueSum += num;
            }
            sumAll += num;
        }

        return 2 * uniqueSum - sumAll;
    }
}
