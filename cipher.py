class Cipher(object):
    def __init__(self):
        self._plain_dict__ = {}
        self._cipher_dict__ = {}
        self._id__ = ""

    def encrypt(self, string):
        result = ''
        for i in list(string.lower()):
            if i == ' ' or ord(i) > ord('z') or ord(i) < ord('a'):
                result += i
                continue
            result += self._cipher_dict__[i]
        return result

    def decrypt(self, string):
        result = ''
        for i in list(string.lower()):
            if i == ' ' or ord(i) > ord('z') or ord(i) < ord('a'):
                result += i
                continue
            result += self._plain_dict__[i]
        return result

    def __str__(self):
        res = self._id__ + ":\n"
        res += "Plain:  |"
        sorted_cipher = sorted(self._cipher_dict__.items())
        for (key, value) in sorted_cipher:
            res += key + "|"
        res += "\nCipher: |"
        for (key, value) in sorted_cipher:
            res += value + "|"
        return res + "\n"


class KeywordCipher(Cipher):
    def __init__(self, keyword):
        self._plain_dict__ = {}
        self._cipher_dict__ = {}
        self._id__ = "Keyword Cipher"
        self._keyword__ = keyword
        order = 'a'
        for i in list(keyword.lower()):
            self._cipher_dict__[order] = i
            self._plain_dict__[i] = order
            order = chr(ord(order) + 1)
        for i in range(ord('a'),ord('z')+1):
            if chr(i) in self._cipher_dict__.values():
                continue
            else:
                self._cipher_dict__[order] = chr(i)
                self._plain_dict__[chr(i)] = order
                order = chr(ord(order) + 1)


class Caesar(Cipher):
    def __init__(self, key):
        self._plain_dict__ = {}
        self._cipher_dict__ = {}
        self._id__ = "Caesar Cipher"
        self._key__ = key
        order = 'a'
        for i in range(ord('a'),ord('z')+1):
            char = chr(((i - ord('a') - key) % 26) + ord('a'))
            self._cipher_dict__[order] = char
            self._plain_dict__[char] = order
            order = chr(ord(order) + 1)

# *****************************************************************************
caesar = Caesar(3)
print str(caesar)
keyword = KeywordCipher('Mograbi')
print str(keyword)

# keyword -> caesar e
# caesar -> keyword d
