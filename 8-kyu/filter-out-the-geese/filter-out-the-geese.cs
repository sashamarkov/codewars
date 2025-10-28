using System.Collections.Generic;
using System.Linq;
​
public static class Filter {
    public static IEnumerable<string> GooseFilter( IEnumerable<string> birds ) {
        var filter = new HashSet<string> {"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"};
        return birds.Where( b => !filter.Contains( b ) );
    }
}