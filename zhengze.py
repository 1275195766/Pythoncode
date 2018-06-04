import re
re_email=re.compile(r'([0-9a-zA-Z_.]+)@([0-9a-zA-Z]+)\.(\w{3})')
print(re_email.match('wuyaoxue.erert@microsoft.com').groups())
print(re_email.match('someone@gmail.com').groups())
