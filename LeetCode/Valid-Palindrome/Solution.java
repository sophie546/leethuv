class Solution {
    public boolean isPalindrome(String s) {
        String reverse = "";
        String orig = s.toLowerCase();
        orig = orig.replaceAll("[^a-z0-9]","");
        for(int i = orig.length() - 1; i >=0; i--){
            reverse += Character.toLowerCase(orig.charAt(i));
        }

        if(reverse.equals(orig)){
            return true;
        } else{
            return false;
        }
    }
}