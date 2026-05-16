#nullable enable
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
​
public record UserProfile(int Id, string Name);
​
public interface IDatabase
{
    Task<string> FetchUserNameAsync(int id);
}
​
public class CachedUserProvider
{
    private readonly IDatabase _database;
    private readonly Dictionary<int, UserProfile> _cache = new();
​
    public CachedUserProvider(IDatabase database)
    {
        _database = database;
    }
​
    public ValueTask<UserProfile> GetUserAsync(int id)
    {
        if (_cache.TryGetValue(id, out var cached))
        {
            return new ValueTask<UserProfile>(cached);
        }
​
        return new ValueTask<UserProfile>(FetchAndCacheAsync(id));
    }
​
    private async Task<UserProfile> FetchAndCacheAsync(int id)
    {
        var name = await _database.FetchUserNameAsync(id);
        var profile = new UserProfile(id, name);
        _cache[id] = profile;
        return profile;
    }
}