class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int minCost = prices[0];

        for(int i = 1; i < prices.length; i++){
            int newProfit = prices[i] - minCost;

            if(profit < newProfit){
                profit = newProfit;
            }

            if(minCost > prices[i]){
                minCost = prices[i];
            }

        }
        return profit;
    }
}