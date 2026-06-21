for(int x=1; x<=xMax; x++){
    const int f=freq[x];
    if (f==0) continue;
    int buy=min(coins/x, f);// the number buying for cost x
    if (buy==0) break;// cannot buy anymore
    cnt+=buy; // add buy to cnt
    coins-=buy*x;// update coins
}