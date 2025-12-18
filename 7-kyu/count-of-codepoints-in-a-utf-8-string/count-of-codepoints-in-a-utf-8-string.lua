local function count_codepoints(utf8_str)
    local count = 0
    local i = 1
    while i <= #utf8_str do
        local b = utf8_str:byte(i)
        i = i + ((b >= 0xF0 and 4) or (b >= 0xE0 and 3) or (b >= 0xC0 and 2) or 1)
        count = count + 1
    end
    return count
end
​
return count_codepoints