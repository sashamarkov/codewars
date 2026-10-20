def battery_bars(percent):
    return f"[{'#' * (percent // 20)}{'.' * (5 - percent // 20)}]"