

def stack_operation(operations):
    stack=[]
    min_stack=[]
    result=[]
    for item in operations:
        parts=item.split()
        if parts[0].lower()=='push':
            val=int(parts[1])
            stack.append(val)
            if not min_stack:
                min_stack.append(val)
            else:
                min_stack.append(min(val,min_stack[-1]))
        elif parts[0].lower()=='pop':
            stack.pop()
            min_stack.pop()
        elif parts[0].lower()=='top':
            result.append(stack[-1])
        elif parts[0]=='getMin':
            result.append(min_stack[-1])

    return result
if __name__=='__main__':
    operation_count=int(input().strip())
    operation=[]
    for _ in range(operation_count):
        op=input()
        operation.append(op)
    result1=stack_operation(operation)
    print('\n'.join(map(str,result1)))
