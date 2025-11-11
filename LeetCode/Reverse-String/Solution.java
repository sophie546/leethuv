class Solution {
    public void reverseString(char[] s) {
        char[] n = new char[s.length];
        int count = 0;
        for(int i = s.length - 1; i >= 0; i--){
            n[count] = s[i];
            count++;
        }

        for(int i =0; i < s.length; i++){
            s[i] = n[i];
        }
    }
}