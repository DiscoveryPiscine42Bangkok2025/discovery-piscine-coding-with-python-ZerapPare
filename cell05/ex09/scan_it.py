# import sys
# import re

# if len(sys.argv) == 3:
#     keyword = sys.argv[1]
#     text = sys.argv[2]

#     matches = re.findall(keyword, text)

#     if matches:
#         print(len(matches))
#     else:
#         print("none")
# else:
#     print("none")


import re
import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    word = sys.argv[2]
    
    found = re.findall(keyword, word)
    
    if found:
        print(len(found))
    else:
        print("none")