def get_colors(color_array):
    result = []
    for subarray in color_array:
        counts = {"Red": 0, "Green": 0, "Blue": 0}
        for code in subarray:
            r, g, b = (int(code[i:i+2], 16) for i in range(0, 6, 2))
            max_val = max(r, g, b)
            if r == max_val:
                counts["Red"] += 1
            elif g == max_val:
                counts["Green"] += 1
            else:
                counts["Blue"] += 1        
        major, minor = sorted(counts, key=counts.get, reverse=True)[:2]
        result.append(f"{major}+{minor}")
    return ",".join(result)