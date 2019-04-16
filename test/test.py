

import re

# line = "bobby123"
line = "boooooooobby123"

# regex_str = "^b.*"  # .表示任意字符，*表示前面的字符可以重复任意多次
# regex_str = "^b.*3$"  # 3$表示必须以3结尾

# regex_str = ".*(b.*b).*"
# 上面正则表达式想要提取boooooooobby123中的boooooooob，()表示提取子串 这个正则表达式的意思是：可以匹配xxxxxbxxxxxbxxxx
# 结果却是bb,因为它是从右边开始匹配的，看到第一个b,就去匹配第二个b，满足条件就不再往左匹配了
# regex_str = ".*?(b.*b).*"
# 改成如上的正则表达式则，它在第一个b 前加了一个？让它从左边开始匹配
# 但是它的结果是boooooooobb，还是没有满足我们的要求
regex_str = ".*?(b.*?b).*"
# 得出了满意的答案：boooooooob，就是在后面的b前加？好，让它不要再进行贪婪匹配了，匹配到一个就可以了

match_obj = re.match(regex_str, line)

if match_obj:
    print(match_obj.group(1))