for (int i = 1; i < s.length(); i++) {
    if (s.charAt(i) == s.charAt(i - 1)) {
        strk++;              // still in the same group
                             // extend current streak
    } else {
        prev = strk;         // group changed, store length
        strk = 1;            // reset
    }

    // *
    if (strk <= prev)
        res++;
}

return res;