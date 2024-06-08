#How do all the escape sequences work? I'll find out.

print("""
1) \\
2) \'
3) \"
What does that do? It used to produce a sound. It's called a Bell character:
4) \"\a\\a\"
5) Hello\b world!
6) \"\f\\f\" has something to do with printing. It instructs python to continue printing on the next line.
7) In that way it has a similar function as: \n\"\\n\"
8) \N{LATIN CAPITAL LETTER A}
...I bet this does something weird.\r9) a
10)\tjump\tjump\tjump\tjump
11) \uAFFF
12) \"\U00000004\"
13) \v Line skip + vertical tab
14) \777
15) \xFF
""")