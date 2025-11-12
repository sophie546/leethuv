class Solution {

    public static int gcd(int a , int b){
        if(b == 0){
            return a;
        }
        return gcd(b, a % b);
    }


    public int minOperations(int[] nums) {
        int minLength = Integer.MAX_VALUE;
        int n = nums.length;
        int countOnes = 0;
        for(int num : nums) if(num == 1) countOnes++;

        if(countOnes > 0) return n - countOnes;

        for(int i =0; i < n; i++){
            int currentGCD = nums[i];
            for(int j = i; j < n;j++){
                currentGCD = gcd(currentGCD, nums[j]);
                if(currentGCD == 1){
                    minLength = Math.min(minLength, j - i + 1);
                    break;
                }
            }
        } 

        if(minLength == Integer.MAX_VALUE) return -1;
        return (minLength - 1) + (n - 1);
    }
}