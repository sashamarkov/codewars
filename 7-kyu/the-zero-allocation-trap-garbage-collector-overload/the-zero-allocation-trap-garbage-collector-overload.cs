using System;
​
public static class TelemetryProcessor {
    public static int GetMaxAnomaly(params ReadOnlySpan<int> readings) {
      int max = 0;
      for (int i = 1; i < readings.Length; i++) {
        max = Math.Max(max, Math.Abs(readings[i] - readings[i - 1]));
      }
      return max;
    }
​
    public static int GetMinAnomaly(params ReadOnlySpan<int> readings) {
      if (readings.Length < 2) return 0;
      int min = int.MaxValue;
      for (int i = 1; i < readings.Length; i++) {
        min = Math.Min(min, Math.Abs(readings[i] - readings[i - 1]));
      }
      return min;
    }
}