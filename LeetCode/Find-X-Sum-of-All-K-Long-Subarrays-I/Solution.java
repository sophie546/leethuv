import java.util.*;

class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int n = nums.length;
        int[] answer = new int[n - k + 1];
        Map<Integer, Integer> freq = new HashMap<>();

    
        for (int i = 0; i < k; i++) {
            freq.put(nums[i], freq.getOrDefault(nums[i], 0) + 1);
        }

        
        for (int i = 0; i <= n - k; i++) {
    
            List<int[]> list = new ArrayList<>();
            for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
                list.add(new int[]{entry.getKey(), entry.getValue()});
            }

            
            list.sort((a, b) -> {
                if (b[1] == a[1]) return b[0] - a[0];
                return b[1] - a[1];
            });

            
            int sum = 0, count = 0;
            for (int[] pair : list) {
                sum += pair[0] * pair[1];
                count++;
                if (count == x) break;
            }
            answer[i] = sum;

        
            if (i + k < n) {
                int remove = nums[i];
                freq.put(remove, freq.get(remove) - 1);
                if (freq.get(remove) == 0) freq.remove(remove);

                int add = nums[i + k];
                freq.put(add, freq.getOrDefault(add, 0) + 1);
            }
        }

        return answer;
    }
}
