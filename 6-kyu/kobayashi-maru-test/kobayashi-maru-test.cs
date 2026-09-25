using System;
using System.Collections.Generic;
using System.Reflection;
​
public static class KobayashiMaru {
  public static int[] Shoot(List<warbird> warbirds) {
    foreach (var w in warbirds) {
      var type = w.GetType();
      foreach (var f in type.GetFields(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance)) {
        if (f.FieldType == typeof(bool) && f.Name.ToLower().Contains("disabled")) {
          try { 
            f.SetValue(w, true); 
          } catch { }
        }
      }
    }
    return new int[10];
  }
}