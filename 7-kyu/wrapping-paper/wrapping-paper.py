def wrapping_paper(boxes):
    return sum(2 * (l*w + w*h + h*l) + min(l*w, w*h, h*l) for l, w, h in boxes)