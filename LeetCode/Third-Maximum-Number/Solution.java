class Solution {
    public int thirdMax(int[] nums) {
      HashSet<Integer> set = new HashSet<>();
      int res = 0;
      for(int num : nums){
        set.add(num);
      }

      if(set.size() < 3){
        for(int num : set){
            res = Math.max(res, num);
        }
        return res;
      }
      List<Integer> list = new ArrayList<>(set);
      Collections.sort(list, Collections.reverseOrder());
      return list.get(2);
      
    }
}
