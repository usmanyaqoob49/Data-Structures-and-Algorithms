"""Examples of Balanced Brackets
{ }
{ } { }
( ( { [ ] } ) )

Examples of Unbalanced Brackets
( ( )
{ { { ) } ]
[ ] [ ] ] ]"""
from stack import Stack
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def balance_brackets(bracket_string):
    sta = Stack()
    is_balance = True
    index = 0

    while index<len(bracket_string) and is_balance:
        #saving each character first
        each_bracket = bracket_string[index]
        if each_bracket == '(' or each_bracket == '[' or each_bracket == '{':
            sta.push_item(each_bracket)
            #if we encounter closing bracket
        else:
            if sta.is_empty():
                is_balance = False
                break
            else:
                top = sta.pop_item()
                if not is_match(top, each_bracket):
                    is_balance = False
                    break
        index +=1

    if sta.is_empty() and is_balance:
        return True
    else:
        return False

print("String : (((({})))) Balanced or not?")
print(balance_brackets("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(balance_brackets("[][]]]"))

print("String : [][] Balanced or not?")
print(balance_brackets("[][]"))