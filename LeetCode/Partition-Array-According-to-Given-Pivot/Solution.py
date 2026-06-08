for(int x: nums){
    if (x<pivot) nums[l++]=x;
    else if (x>pivot) R.push_back(x);
    else m++;
}