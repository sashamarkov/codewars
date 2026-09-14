#nullable enable
using System;
using System.Collections.Generic;
using System.Linq;
​
public class User {
  public int Id { get; set; }
  public bool IsActive { get; set; }
}
​
public class UserCache {
  private readonly object _lock = new object();
  private readonly List<User> _activeUsers = new List<User>();
​
  public void Refresh(IQueryable<User> database) {
    var newUsers = database.Where(u => u.IsActive).ToList();
    lock (_lock) {
      _activeUsers.Clear();
      _activeUsers.AddRange(newUsers);
    }
  }
​
  public IEnumerable<User> GetUsers() {
    List<User> users;
    lock (_lock) {
      users = new List<User>(_activeUsers);
    }
    return users;
  }
}