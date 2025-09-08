class Solution {
    public int[] getNoZeroIntegers(int n) {
       int[] num = new int[2];
       for(int i = 1; i < n; i++){
            int a = i;
            int b = n - i;
            if(isNoZero(a) && isNoZero(b)){
                num[0] = a;
                num[1] = b;
                return num;
            }
       }
       return num;
    }

    public boolean isNoZero(int x){
        while(x > 0){
            if(x % 10 == 0){
                return false;
            }
            x /= 10;
        }
        return true;
    }
    
}