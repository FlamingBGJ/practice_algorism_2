# -*- coding: utf-8 -*-
"""순차검색.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M8ok4eabBLj4X_n7ph6b5E5i37jPPmps
"""

## 함수
import random
def seqSearch(ary, fData) :
    pos = -1
    size = len(ary)

    for i in range(size) :
        if (ary[i] == fData)  :
            pos = i
            break

    return pos
## 변수
SIZE=8
dataAry = [random.randint(40, 200) for _ in range(SIZE)]
findData = random.choice(dataAry)

## 메인
print('배열-->', dataAry)
position = seqSearch(dataAry, findData)
if (position == -1) :
    print(findData,'는', position, '없어요 ㅠㅠ')
else :
    print(findData,'는', position, '위치에 있음 ^^')