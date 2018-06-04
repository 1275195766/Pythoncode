import re
email2=re.compile(r'<([0-9a-zA-Z\s]+)>\s([0-9a-zA-Z_.]+)@([0-9a-zA-Z]+)\.(\w{3})')
print(email2.match('<Tom Paris> tom@voyager.org').groups())
