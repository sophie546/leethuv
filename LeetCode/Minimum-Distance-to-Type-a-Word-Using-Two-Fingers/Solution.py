if (x==26 || y==26) return 0; // 26 denotes hovering 
return abs(x/6-y/6)+abs(x%6-y%6);