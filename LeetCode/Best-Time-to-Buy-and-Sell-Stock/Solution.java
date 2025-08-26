class Solution {
    public int maxProfit(int[] prices) {
        int minCost = prices[0];
        int profit = 0;
        for(int i= 1; i < prices.length; i++){
            int newProfit =  prices[i] - minCost;

            if(profit < newProfit){
                profit = newProfit;
            }

            if(prices[i] < minCost){
                minCost = prices[i];
            }

        }
        return profit;
    }
}