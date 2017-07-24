import pandas as pd
# Create two lists
i = ["Product1","Product2","Product3"]
j = ["Product1","Product2","Product3"]
# List every single x in i with every single y (i.e. Cartesian product)
[(x, y) for x in i for y in j]
