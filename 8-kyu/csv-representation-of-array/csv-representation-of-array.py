def toCsvText(array) :
   return '\n'.join([",".join([str(i) for i in sub]) for sub in array])