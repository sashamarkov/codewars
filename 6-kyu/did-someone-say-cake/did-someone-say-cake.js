function cake(ingredient, amount) {
  var recipe = {'caster sugar': 160, 'butter': 170, 'eggs': 3, 'self-raising flour': 115, 'cocoa powder': 55};
  const factor = amount / recipe[ingredient];
  return Object.fromEntries(Object.entries(recipe).map(([key, val]) => 
    [key, key === 'eggs' ? Math.round(val * factor * 10) / 10 : Math.round(val * factor * 10) / 10 + 'g']
  ));
}