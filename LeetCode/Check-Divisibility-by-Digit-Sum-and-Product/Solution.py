for(int x=n; x>0; x/=10){
    const int r=x%10;
    s+=r;
    p*=r;
}