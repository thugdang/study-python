s = '''Thuyền và biển
(Xuân Quỳnh)
Em sẽ kể anh nghe
Chuyện con thuyền và biển:

"Từ ngày nào chẳng biết
Thuyền nghe lời biển khơi
Cánh hải âu, sóng biếc
Đưa thuyền đi muôn nơi

Lòng thuyền nhiều khát vọng
Và tình biển bao la
Thuyền đi hoài không mỏi
Biển vẫn xa... còn xa

Những đêm trăng hiền từ
Biển như cô gái nhỏ
Thầm thì gửi tâm tư
Quanh mạn thuyền sóng vỗ   
Cũng có khi vô cớ
Biển ào ạt xô thuyền
(Vì tình yêu muôn thuở
Có bao giờ đứng yên?)

Chỉ có thuyền mới hiểu
Biển mênh mông nhường nào
Chỉ có biển mới biết
Thuyền đi đâu, về đâu

Những ngày không gặp nhau
Biển bạc đầu thương nhớ
Những ngày không gặp nhau
Lòng thuyền đau - rạn vỡ 
Nếu từ giã thuyền rồi
Biển chỉ còn sóng gió"

Nếu phải cách xa anh
Em chỉ còn bão tố

Tháng 4 năm 1963'''

discard = '(),"-.?:'
print('Cau a:')
print('Dict:')
d = {}
for char in s.split():
    char = char.strip(discard).lower()
    if char in d:
        d[char] += 1
    elif char == '':
        pass
    else:
        d[char] = 1
for k, v in d.items():
    print("'{}': {}".format(k, v), end='; ')
print('\nTuple:')
l1 = ()
l2 = ()
for char in s.split():
    char = char.strip(discard).lower()
    if char == '':
        pass
    elif char not in l1:
        count = 0
        l1 += (char,)
        for c in s.split():
            c = c.strip(discard).lower()
            if char == c:
                count += 1
        l2 += (count,)
t = tuple(zip(l1, l2))
print(t)

print('\nCau b:')
print('Dict:')
most = 0
for k, v in d.items():
    if most < v:
        most = v
for k, v in d.items():
    if most == v:
        print("'{}': {}".format(k, v), end='; ')

print('\nCau c:')
count = 0
for k, v in d.items():
    if count < len(k):
        count = len(k)
for k, v in d.items():
    if count == len(k):
        print(k, end='; ')

print('\nCau d:')
l = {}
for k, v in d.items():
    l[k] = len(k)
l = dict(sorted(l.items(), key=lambda item: item[1], reverse=True))
import itertools
out5 = dict(itertools.islice(l.items(), 5))
for k, v in out5.items():
    print(f'{k}: {v} ky tu', end='; ')

print('\nCau e:')
l = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
out5 = dict(itertools.islice(l.items(), 5))
for k, v in out5.items():
    print(f'{k}: {v} lan', end='; ')