s = 'radar'
# cau a
sReverse = s[::-1]
if s == sReverse:
    print('Chuoi doi xung!')
else:
    print('Chuoi bat doi xung!')

# cau b
sReverse = ''.join(reversed(s))
if s == sReverse:
    print('Chuoi doi xung!')
else:
    print('Chuoi bat doi xung!')

# cau c
sReverse = ''
for i in range(len(s) - 1, -1, -1):
    sReverse += s[i]
if s == sReverse:
    print('Chuoi doi xung!')
else:
    print('Chuoi bat doi xung!')