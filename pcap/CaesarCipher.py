


"""_summary_: Generate a chiper with input of shift
"""
class SubstitutitionCipher():
    def __init__(self, shift: int) -> None:
        if type(shift) != int:
            raise ValueError("Please enter valid input")
        self.shift = shift

    def generateCipher(self, input: str) -> str:
        result = [ self.shiftCharacters(x) for x in input]
        cipher = "".join(result)
        print(input)
        print(cipher)
        return cipher

    def decrypt(self, input: str) -> str:
        print(input)
        result = [ self.deShiftCharacters(x) for x in input]
        clear = "".join(result)
        print(clear)
        return clear
    
    @property
    def shiftAdjustment(self) -> int:
        if self.shift is None:
            return 0
        else:
            return self.shift

    def deShiftCharacters(self, char)-> str:
        myString = char
        if not myString.isalpha():
            return myString
        myString = myString.upper()
        code = ord(myString) - self.shiftAdjustment
        if code < ord("A"):
            code = code + (ord('Z') - ord('A')) + 1
        myString = chr(code)
        return myString

    def shiftCharacters(self, char)-> str:
        myString = char
        if not myString.isalpha():
            return myString
        myString = myString.upper()
        code = ord(myString) + self.shiftAdjustment
        if code > ord("Z"):
            code = code - (ord('Z') - ord('A') + 1)
        myString = chr(code)
        return myString
   

def main():
    sub = SubstitutitionCipher(3)
    cipher =  sub.generateCipher("the long brown fox jumped over the lazy dog")
    sub.decrypt(cipher)

    for x in range(5):
        if (x==3):
            continue
        print(x)


if __name__ == "__main__":
    main()
    
"""
0-0x29     0-47 non printing and symbos
0x30-0x39  48-67  0-9

0x41-0x5A    41-66   A-Z
0x62-0x7B    98-103  a-z


  0 | 0x0 |       1 | 0x1 | ☺     2 | 0x2 | ☻     3 | 0x3 | ♥     4 | 0x4 | ♦     5 | 0x5 | ♣
  6 | 0x6 | ♠     7 | 0x7 |       8 | 0x8 |       9 | 0x9 | HT   10 | 0xa | LF   11 | 0xb | VT
 12 | 0xc | FF   13 | 0xd | CR   14 | 0xe |      15 | 0xf |      16 | 0x10 | ►   17 | 0x11 | ◄
 18 | 0x12 | ↕   19 | 0x13 | ‼   20 | 0x14 | ¶   21 | 0x15 | §   22 | 0x16 | ▬   23 | 0x17 | ↨
 24 | 0x18 | ↑   25 | 0x19 | ↓   26 | 0x1a | →   27 | 0x1b | ES  28 | 0x1c | ∟   29 | 0x1d | ↔
 30 | 0x1e | ▲   31 | 0x1f | ▼   32 | 0x20 |     33 | 0x21 | !   34 | 0x22 | "   35 | 0x23 | #
 36 | 0x24 | $   37 | 0x25 | %   38 | 0x26 | &   39 | 0x27 | '   40 | 0x28 | (   41 | 0x29 | )
 42 | 0x2a | *   43 | 0x2b | +   44 | 0x2c | ,   45 | 0x2d | -   46 | 0x2e | .   47 | 0x2f | /
 48 | 0x30 | 0   49 | 0x31 | 1   50 | 0x32 | 2   51 | 0x33 | 3   52 | 0x34 | 4   53 | 0x35 | 5
 54 | 0x36 | 6   55 | 0x37 | 7   56 | 0x38 | 8   57 | 0x39 | 9   58 | 0x3a | :   59 | 0x3b | ;
 60 | 0x3c | <   61 | 0x3d | =   62 | 0x3e | >   63 | 0x3f | ?   64 | 0x40 | @   65 | 0x41 | A
 66 | 0x42 | B   67 | 0x43 | C   68 | 0x44 | D   69 | 0x45 | E   70 | 0x46 | F   71 | 0x47 | G
 72 | 0x48 | H   73 | 0x49 | I   74 | 0x4a | J   75 | 0x4b | K   76 | 0x4c | L   77 | 0x4d | M
 78 | 0x4e | N   79 | 0x4f | O   80 | 0x50 | P   81 | 0x51 | Q   82 | 0x52 | R   83 | 0x53 | S
 84 | 0x54 | T   85 | 0x55 | U   86 | 0x56 | V   87 | 0x57 | W   88 | 0x58 | X   89 | 0x59 | Y
 90 | 0x5a | Z   91 | 0x5b | [   92 | 0x5c | \   93 | 0x5d | ]   94 | 0x5e | ^   95 | 0x5f | _
 96 | 0x60 | `   97 | 0x61 | a   98 | 0x62 | b   99 | 0x63 | c  100 | 0x64 | d  101 | 0x65 | e
102 | 0x66 | f  103 | 0x67 | g  104 | 0x68 | h  105 | 0x69 | i  106 | 0x6a | j  107 | 0x6b | k
108 | 0x6c | l  109 | 0x6d | m  110 | 0x6e | n  111 | 0x6f | o  112 | 0x70 | p  113 | 0x71 | q
114 | 0x72 | r  115 | 0x73 | s  116 | 0x74 | t  117 | 0x75 | u  118 | 0x76 | v  119 | 0x77 | w
120 | 0x78 | x  121 | 0x79 | y  122 | 0x7a | z  123 | 0x7b | {  124 | 0x7c | |  125 | 0x7d | }
126 | 0x7e | ~  127 | 0x7f |    128 | 0x80 |    129 | 0x81 |    130 | 0x82 |    131 | 0x83 |
132 | 0x84 |    133 | 0x85 |    134 | 0x86 |    135 | 0x87 |    136 | 0x88 |    137 | 0x89 |
138 | 0x8a |    139 | 0x8b |    140 | 0x8c |    141 | 0x8d |    142 | 0x8e |    143 | 0x8f |
144 | 0x90 |    145 | 0x91 |    146 | 0x92 |    147 | 0x93 |    148 | 0x94 |    149 | 0x95 |
150 | 0x96 |    151 | 0x97 |    152 | 0x98 |    153 | 0x99 |    154 | 0x9a |    155 | 0x9b |
156 | 0x9c |    157 | 0x9d |    158 | 0x9e |    159 | 0x9f |    160 | 0xa0 |    161 | 0xa1 | ¡
162 | 0xa2 | ¢  163 | 0xa3 | £  164 | 0xa4 | ¤  165 | 0xa5 | ¥  166 | 0xa6 | ¦  167 | 0xa7 | §
168 | 0xa8 | ¨  169 | 0xa9 | ©  170 | 0xaa | ª  171 | 0xab | «  172 | 0xac | ¬  173 | 0xad | ­
174 | 0xae | ®  175 | 0xaf | ¯  176 | 0xb0 | °  177 | 0xb1 | ±  178 | 0xb2 | ²  179 | 0xb3 | ³
180 | 0xb4 | ´  181 | 0xb5 | µ  182 | 0xb6 | ¶  183 | 0xb7 | ·  184 | 0xb8 | ¸  185 | 0xb9 | ¹
186 | 0xba | º  187 | 0xbb | »  188 | 0xbc | ¼  189 | 0xbd | ½  190 | 0xbe | ¾  191 | 0xbf | ¿
192 | 0xc0 | À  193 | 0xc1 | Á  194 | 0xc2 | Â  195 | 0xc3 | Ã  196 | 0xc4 | Ä  197 | 0xc5 | Å
198 | 0xc6 | Æ  199 | 0xc7 | Ç  200 | 0xc8 | È  201 | 0xc9 | É  202 | 0xca | Ê  203 | 0xcb | Ë
204 | 0xcc | Ì  205 | 0xcd | Í  206 | 0xce | Î  207 | 0xcf | Ï  208 | 0xd0 | Ð  209 | 0xd1 | Ñ
210 | 0xd2 | Ò  211 | 0xd3 | Ó  212 | 0xd4 | Ô  213 | 0xd5 | Õ  214 | 0xd6 | Ö  215 | 0xd7 | ×
216 | 0xd8 | Ø  217 | 0xd9 | Ù  218 | 0xda | Ú  219 | 0xdb | Û  220 | 0xdc | Ü  221 | 0xdd | Ý
222 | 0xde | Þ  223 | 0xdf | ß  224 | 0xe0 | à  225 | 0xe1 | á  226 | 0xe2 | â  227 | 0xe3 | ã
228 | 0xe4 | ä  229 | 0xe5 | å  230 | 0xe6 | æ  231 | 0xe7 | ç  232 | 0xe8 | è  233 | 0xe9 | é
234 | 0xea | ê  235 | 0xeb | ë  236 | 0xec | ì  237 | 0xed | í  238 | 0xee | î  239 | 0xef | ï
240 | 0xf0 | ð  241 | 0xf1 | ñ  242 | 0xf2 | ò  243 | 0xf3 | ó  244 | 0xf4 | ô  245 | 0xf5 | õ
246 | 0xf6 | ö  247 | 0xf7 | ÷  248 | 0xf8 | ø  249 | 0xf9 | ù  250 | 0xfa | ú  251 | 0xfb | û
"""