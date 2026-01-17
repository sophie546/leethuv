public class Solution {
    public long LargestSquareArea(int[][] bottomLeft, int[][] topRight) {
        var rs = 0L;
        for (int i = 0; i < bottomLeft.Length - 1; i++)
        {
            for (int j = i + 1; j < bottomLeft.Length; j++)
            {
                var rs0 = LargestSquareArea(bottomLeft[i], topRight[i], bottomLeft[j], topRight[j]);
                rs = Math.Max(rs, rs0);
            }
        }
        return rs;
    }
    private long LargestSquareArea(int[] a0, int[] b0, int[] a1, int[] b1)
    {
        var rs = 0L;
        var left = Math.Max(a0[0], a1[0]);
        var right = Math.Min(b0[0], b1[0]);
        if (left >= right) return rs;
        var bottom = Math.Max(a0[1], a1[1]);
        var top = Math.Min(b0[1], b1[1]);
        if (bottom >= top) return rs;
        long side = Math.Min(right - left, top - bottom);
        rs = side * side;
        return rs;
    }
}