for(int x: nums){
    hasX[x]=1;
    xMin=min(x, xMin);
    xMax=max(x, xMax);
}