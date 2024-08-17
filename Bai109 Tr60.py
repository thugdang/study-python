lst = [[a, b, c] for a in range(1, 21) for b in range(a, 21) for c in range(b, 21) if a**2 + b**2 == c**2]
print('3 for: ', lst)

import math
lst = [[a, b, int(math.sqrt(a**2 + b**2))] for a in range(1, 20) for b in range(1, 20) if math.sqrt(a**2 + b**2).is_integer()]
print('2 for: ', lst)