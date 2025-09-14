class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer,Integer> map = new HashMap<>();
        
        for(int num : nums1){
            map.put(num,map.getOrDefault(num,0)+1);
        }

        List<Integer> resTemp = new ArrayList<>();
        for(int num : nums2){
            if(map.containsKey(num) && map.get(num) > 0){
                resTemp.add(num);
                map.put(num, map.get(num) - 1);
            }
        }

        int[] res = new int[resTemp.size()];
        int index = 0;
        for(int num : resTemp){
            res[index++] = num;
        }
        
        return res;
    }
}