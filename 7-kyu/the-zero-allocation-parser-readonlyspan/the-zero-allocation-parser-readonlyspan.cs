#nullable enable
using System;
​
public class FinancialParser {
    public static double ParseStockPrice(ReadOnlySpan<char> rawData) {
        ReadOnlySpan<char> prcMarker = stackalloc[] { 'P', 'R', 'C', ':' };
        ReadOnlySpan<char> volMarker = stackalloc[] { '|', 'V', 'O', 'L', ':' };
​
        int prcIndex = rawData.IndexOf(prcMarker);
        if (prcIndex == -1) return 0.0;
​
        int startIndex = prcIndex + 4;
​
        var remaining = rawData.Slice(startIndex);
        int endIndex = remaining.IndexOf(volMarker);
​
        ReadOnlySpan<char> priceSlice = endIndex == -1
            ? remaining
            : remaining.Slice(0, endIndex);
        return double.Parse(priceSlice);
    }
}