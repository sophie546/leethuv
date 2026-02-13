int longestBalancedLimited(string s, int k) {
    vector<int> cnt(k, 0);
    map<vector<int>, int> firstPos;
    firstPos[cnt] = -1;
    int ans = 0;
    for(int i = 0; i < (int)s.size(); i ++){
        int x = s[i] - 'a';
        cnt[x] ++;
        vector<int> gcnt(k);
        int ref = cnt[0];
        gcnt[0] = 0;
        for(int j = 1; j < k; j ++){
            gcnt[j] = cnt[j] - ref;
        }
        auto it = firstPos.find(gcnt);
        if(it != firstPos.end()){
            ans = max(ans, i - it -> second);
        }
        else{
            firstPos[gcnt] = i;
        }
    }
    return ans;
}