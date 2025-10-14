def isAlphabeticPalindrome(code):
    # Write your code here
    f=False
    alpha=[]
    for c in code:
        if c.isalpha():
            alpha.append(c.lower())
    if alpha==alpha[::-1]:
        f=True
    return f

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
