S = ''' Khát vọng
   Hãy sống như đời sống để biết yêu nguồn cội  .
Hãy sống như đổi núi   ,  vươn tới những  tầm cao.
  Hãy  sống   như  biển trào,như biển trào để thấy bờ bến rộng .
Hãy sống như ước vọng  để   thấy đời mênh mông.
Và sao  không    là gió,    là mây để thấy trời bao la  .
Và sao không là phù sa dâng mỡ màu cho hoa.
 Sao không là bài ca của tình yêu đôi lứa.
Sao không là mặt trời gieo hạt nắng vô tư.
Và sao  không là bão ,   là giông  ,là ánh lửa đêm đông     .
     Và sao không là hạt giống xanh đất mẹ bao dung.
Sao không là đàn    chim gọi bình minh thức giấc  .
 Sao không là  mặt trời gieo hạt nắng vô tư.
     Phạm Minh Tuấn      '''

def xuly(S):
    S = S.strip()
    while S.find(' .') >= 0:
        S = S.replace(' .', '.')
    while S.find(' ,') >= 0:
        S = S.replace(' ,', ',')
    while S.find('\n ') >= 0:
        S = S.replace('\n ', '\n')
    vt = 0
    while vt < len(S):
        temp = S.find(',', vt, len(S))
        if temp > -1:
            S = S[0:temp + 1] + ' ' + S[temp + 1:len(S)]
            vt = temp + 1
        else:
            break
    while S.find('  ') >= 0:
        S = S.replace('  ', ' ')
    return S

S = xuly(S)
print(S)
