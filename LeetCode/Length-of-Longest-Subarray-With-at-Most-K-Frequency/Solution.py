for (int l=0, r=0; r<n; r++){// move r to extend window
    const int x=nums[r];// get x
    auto it=freq.find(x); // set iterator it
    // if it not found, set f=freq[x]=1 by passing ref
    // otherwise set f=++(it->second) by passing ref
    int& f=(it==freq.end())?freq[x]=1:++(it->second);
    while (f>k)//as long as f>k
        // decrease freq[nums[l]]] by 1, 
        // then shrink the window by l++
        freq[nums[l++]]--;
        
    cnt=max(cnt,r-l+1);// max len
}
return cnt;