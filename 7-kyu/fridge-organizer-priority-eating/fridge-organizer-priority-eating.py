def fridge_organizer(items):
    fresh_items = [item for item in items if item.expiry_days >= 0]
    return [item.name for item in sorted(fresh_items, key=lambda x: (not x.is_almost_empty, x.expiry_days, x.name))]
​