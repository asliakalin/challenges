 
# Your previous Python 3 content is preserved below:
# 
# #Given an input string and a list of substrings to bold, return the same input string with HTML bold tags <b> and </b> around the substrings which are found in the input string.
# 
# # >>> embolden_substrings('abcxyz', [])
# # 'abcxyz'
# 
# # >>> embolden_substrings('abcxyz', ['abc'])
# # '<b>abc</b>xyz'
# 
# # >>> embolden_substrings('abcabc’, ['abc'])
# # '<b>abcabc</b>’
# 
# # >>> embolden_substrings('abcxyz123', ['abc', '123'])
# # '<b>abc</b>xyz<b>123</b>'
# 
# 
# #  >>> embolden_substrings('abcdxyz1234abc', ['abc', '123', 'bcd'])
# #  '<b>abcd</b>xyz<b>123</b>4<b>abc</b>'

import re 
def boldThings(text, subs):
    indices = []
    count = 0
    if not subs:
        return text
    for pattern in subs:
        look = 0
        while text.find(pattern, look) != -1:
            start = text.find(pattern, look)
            if start != -1:
                end = start + len(pattern)
            indices += [[start, end]] #[[],[]]
            look += end   
    merged = mergeRange(indices)
    count = 0
    for thing in merged:
        start = thing[0] + count # [1,2]
        end = thing[1] + count
        
        text = text[:start] + '<b>' + text[start:end] + '</b>' + text[end:]
        count += 7
    return text


# a<b>bcd</b>e [1,3]
# [[0, 4], [7, 10], [1, 4]], 
# [[0, 4], [7, 10], [1, 4]]
# 
def mergeRange(arr):
    sorted(arr, key=lambda index: index[0])
    final = []
    # iterate all pairs
    for i in range(len(arr)):
        if i == 0:
            final.append(arr[0])
        else:
            interval = arr[i]
            # compare to final pairs
            added = False
            for j in range(len(final)):
                comp = final[j]
                if comp[0]<=interval[0]<=comp[1]:
                    final[j][1] = arr[i][1]
                    added = True
            if not added:
                final.append(interval)
    return sorted(final, key=lambda pair: pair[0])
        

text = 'abcdxyz1234abc'
subs = ['abc', '123', 'bcd']
# <b>abcd</b>xyz<b>123</b>4<b>abc</b>
# <b>abcd</b>xyz1234<b><b>abc</b></b>

print(boldThings(text,subs))