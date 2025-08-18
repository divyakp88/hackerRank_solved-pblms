import re
def fun(s):
    try:
        username,domain=s.split("@")
        web,exten=domain.split(".")
        if  re.fullmatch(r'[A-Za-z0-9_-]+',username):
            if re.fullmatch(r'[a-zA-Z0-9]+',web):
                if re.fullmatch(r'[a-zA-Z]+',exten) and len(exten)<=3:
                    return True
        return False
    except:
        return False

# return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)