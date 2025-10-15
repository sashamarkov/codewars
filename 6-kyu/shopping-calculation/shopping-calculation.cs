            var items = new List<string>();
            if (purchases.ContainsKey(customer)) {
                ProcessCustomerPurchases(customer, purchases, products, ref money, items);
            }
            result.Add((customer, $"${money}", string.Join(", ", items)));
        }
        
        return result;
    }
​
    private static void ProcessCustomerPurchases(
        string customer,
        Dictionary<string, List<(string, int)>> purchases,
        Dictionary<string, int> products,
        ref int money,
        List<string> items) {
        foreach (var (product, quantity) in purchases[customer]) {
            ProcessSinglePurchase(product, quantity, products, ref money, items);
        }
    }
​
    private static void ProcessSinglePurchase(
        string product,
        int quantity,
        Dictionary<string, int> products,
        ref int money,
        List<string> items) {
        string matchingProduct = product;
        if (products.ContainsKey(product)) {
            money -= quantity * products[product];
            items.Add($"{quantity} {product}");
        }
        else {
            var singular = product.EndsWith("s") ? product.Substring(0, product.Length - 1) : product;
            if (products.ContainsKey(singular)) {
                money -= quantity * products[singular];
                items.Add($"{quantity} {(quantity > 1 ? singular + "s" : singular)}");
            }
        }
    }
}