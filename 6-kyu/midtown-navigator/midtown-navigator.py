import re
​
def midtown_nav(start, end):
    start_ave, start_st = parse_location(start)
    end_ave, end_st = parse_location(end)
    street_dir, street_diff = get_street_dir(start_st, end_st)
    ave_dir, ave_diff = get_ave_dir(start_ave, end_ave)
    return f"Walk {abs(street_diff)} blocks {street_dir}, and {abs(ave_diff)} blocks {ave_dir}"
​
def parse_location(loc):
    match = re.match(r'(\d+)(?:st|nd|rd|th) Ave and [WE] (\d+)(?:st|nd|rd|th) St', loc)
    return int(match.group(1)), int(match.group(2))
​
def get_street_dir(start_st, end_st):
    street_diff = end_st - start_st
    dir = "north" if street_diff > 0 else "south" if street_diff < 0 else "north"
    return dir, street_diff
​
def get_ave_dir(start_ave, end_ave):
    ave_diff = end_ave - start_ave
    dir = "west" if ave_diff > 0 else "east" if ave_diff < 0 else "west"
    return dir, ave_diff