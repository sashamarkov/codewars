class Format:
    tags = frozenset(("div", "h1", "p", "span"))
    def __init__(self, chain=None):
        self._chain = chain or []
        
    def __getattr__(self, name):
        if name in self.tags:
            return Format(self._chain + [name])
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
            
    def __call__(self, *args):
        if not args:
            return ""
        content = "".join(str(arg) for arg in args)
        result = content
        for tag in reversed(self._chain):
            result = f"<{tag}>{result}</{tag}>"
        return result
​
format = Format()