    
安利一句话：字符串是不可变的对象，所以任何操作对原字符串是不改变的！

1.字符串的切割
    def split(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
        """
        S.split(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are
        removed from the result.
        """
        return []

        用法:返回字符串中所有单词的列表，使用 sep 作为分隔符(默认值是空字符（空格）)用什么切就去掉什么。
             可以使用 maxsplit 指定最大切分数。
        例子：     s = 'STriSSB'
                  print(s.split('STriSSB')) ----> ['', '']
                  print(s.split('S')) ----> ['', 'Tri', '', 'B']
        注意:如果切分的参数 sep 在字符串的左边或者右边，最后切得的链表中会存在一个空字符串。(如：['',等])
             如果切分的参数 sep 是整个字符串，那么切分结果为两个空字符串组成的列表。(['',''])

    def rsplit(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
        """
        S.rsplit(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string, starting at the end of the string and
        working to the front.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified, any whitespace string
        is a separator.
        """
        return []

        用法:返回字符串中所有单词的列表，使用 sep 作为分隔符(默认值是空字符（空格）)
             可以使用 maxsplit 指定最大切分数。只不过切的时候是从右边开始切。
        例子:    s = 'STriSSB'
                print(s.split('STriSSB'))       ----------> ['', '']
                print(s.rsplit('STriSSB'))      ----------> ['', '']
                print(s.split('S'))             ----------> ['', 'Tri', '', 'B']
                print(s.rsplit('S'))            ----------> ['', 'Tri', '', 'B']
                print(s.split('S', maxsplit=1)) ----------> ['', 'TriSSB']
                print(s.rsplit('S', maxsplit=1))----------> ['STriS', 'B']

2.字符串连接
    def join(self, iterable): # real signature unknown; restored from __doc__
        """
        S.join(iterable) -> str
        
        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.
        """
        return ""

        用法:用S连接序列iterable的所有元素并返回。序列iterable的元素必须全是字符串。
             join()方法是split()方法的逆方法，用来把列表中的个字符串联起来。

3.字符串的查找
    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    用法:返回字符串sub的第一个索引，如果不存在这样的索引则返回-1，可定义搜索的范文为S[start:end].

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found, 
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

        用法:返回字符串sub的第一个索引，或者在找不到索引的时候引发 ValueError异常，可定义索引的范围为S[start:end].

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

        用法:检测S是否是以prefix开始，可定义搜索范围为S[start:end].

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

        用法:检测S是否以suffix结尾，可定义搜索范围为S[start:end]


4.字符串的替换
    def replace(self, old, new, count=None): # real signature unknown; restored from __doc__
        """
        S.replace(old, new[, count]) -> str
        
        Return a copy of S with all occurrences of substring
        old replaced by new.  If the optional argument count is
        given, only the first count occurrences are replaced.
        """
        return ""

        用法:返回字符串的副本，其中old的匹配项都被替换为new，可选择最多替换count个(从左往右替换)。如果count超过了最大替换个数，会报错


5.字符串的删除
    def strip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.strip([chars]) -> str
        
        Return a copy of the string S with leading and trailing
        whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

        用法:返回字符串的副本，其中所有的chars(默认为空格)都被从字符串的开头和结尾删除(默认为所有的空白字符，如空格，tab和换行符。)

    def lstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.lstrip([chars]) -> str
        
        Return a copy of the string S with leading whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

        用法:返回一个字符串副本，其中所有的char(默认为所有的空白字符，如空格，tab和换行符。)都被从字符串左端删除。

    def rstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.rstrip([chars]) -> str
        
        Return a copy of the string S with trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""
        
        用法:返回一个字符串副本，其中所有的char(默认为所有的空白字符，如空格，tab和换行符。)都被从字符串右端删除。


6.统计字符串出现次数
    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

        用法:计算字符串sub的出现次数，可以定义搜索的范围为S[start:end]


7.字符串字母大小写转换
    def upper(self): # real signature unknown; restored from __doc__
        """
        S.upper() -> str
        
        Return a copy of S converted to uppercase.
        """
        return ""

        用法:返回字符串的副本，其中所有小写字母都转换为大写字母。


    def lower(self): # real signature unknown; restored from __doc__
        """
        S.lower() -> str
        
        Return a copy of the string S converted to lowercase.
        """
        return ""

        用法:返回字符串的副本，其中所有大写字母都转换为小写字母。

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        S.swapcase() -> str
        
        Return a copy of S with uppercase characters converted to lowercase
        and vice versa.
        """
        return ""

        用法:返回字符串副本，其中大小写进行了互换。

    def title(self): # real signature unknown; restored from __doc__
        """
        S.title() -> str
        
        Return a titlecased version of S, i.e. words start with title case
        characters, all remaining cased characters have lower case.
        """
        return ""

        用发:返回字符串副本，其中单词都已大写字母开头。


8.字符串条件判断
    def isalnum(self): # real signature unknown; restored from __doc__
        """
        S.isalnum() -> bool
        
        Return True if all characters in S are alphanumeric
        and there is at least one character in S, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        S.isalpha() -> bool
        
        Return True if all characters in S are alphabetic
        and there is at least one character in S, False otherwise.
        """
        return False

    def isdecimal(self): # real signature unknown; restored from __doc__
        """
        S.isdecimal() -> bool
        
        Return True if there are only decimal characters in S,
        False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        S.isdigit() -> bool
        
        Return True if all characters in S are digits
        and there is at least one character in S, False otherwise.
        """
        return False

    def isidentifier(self): # real signature unknown; restored from __doc__
        """
        S.isidentifier() -> bool
        
        Return True if S is a valid identifier according
        to the language definition.
        
        Use keyword.iskeyword() to test for reserved identifiers
        such as "def" and "class".
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        S.islower() -> bool
        
        Return True if all cased characters in S are lowercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def isnumeric(self): # real signature unknown; restored from __doc__
        """
        S.isnumeric() -> bool
        
        Return True if there are only numeric characters in S,
        False otherwise.
        """
        return False

    def isprintable(self): # real signature unknown; restored from __doc__
        """
        S.isprintable() -> bool
        
        Return True if all characters in S are considered
        printable in repr() or S is empty, False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        S.isspace() -> bool
        
        Return True if all characters in S are whitespace
        and there is at least one character in S, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        S.istitle() -> bool
        
        Return True if S is a titlecased string and there is at least one
        character in S, i.e. upper- and titlecase characters may only
        follow uncased characters and lowercase characters only cased ones.
        Return False otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        S.isupper() -> bool
        
        Return True if all cased characters in S are uppercase and there is
        at least one cased character in S, False otherwise.
        """
        return False
        






















