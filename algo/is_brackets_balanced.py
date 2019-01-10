# https://codereview.stackexchange.com/questions/180567/checking-for-balanced-brackets-in-python

def isBalanced(s):
  i=0
  for c in s:
    if c=='(': i+=1
    if c==')': i-=1
    if i < 0: return False

  return i == 0

s1="(())("
s2="(())"

print(isBalanced(s1))
print(isBalanced(s2))

def is_matched(expression):
    mapping = dict(zip('({[', ')}]'))
    queue = []
    for letter in expression:
        if letter in mapping:
            queue.append(mapping[letter])
        elif not (queue and letter == queue.pop()):
            return False
    return not queue

def pairs_stack(string, pairs = {'[': ']', '{': '}', '(': ')'}):

    print("string=",string)
    opening = list(pairs.keys())
    closing = list(pairs.values())
    match = list()
    for s in string:
        if s in opening:
            match.insert(0, s)
        elif s in closing:
            if len(match) == 0:
                return False
            #print ("match[0]=", match[0], "s=", s, "closing=",closing)
            if match[0] == opening[closing.index(s)]:
                match.pop(0)
            else:
                return False

    if len(match) == 0:
        return True

    return False


string = "[]{}()[][][]"
print ("Should be true")
print (str(pairs_stack(string)))
print (str(is_matched(string)))

exit(0)

string = "([()][][{}])"
print ("Should be true")
print (str(pairs_stack(string)))

string = "[(])"
print ("Should be false")
print (str(pairs_stack(string)))

string = "[([])()({})]"
print ("Should be true")
print (str(pairs_stack(string)))

string = "[(,,),(,,[])]"
print ("Should be true")
print (str(pairs_stack(string)))

string = "[(,,,(,,[])]"
print ("Should be false")
print (str(pairs_stack(string)))

string = "]"
print ("Should be false")
print (str(pairs_stack(string)))

string = "["
print ("Should be false")
print (str(pairs_stack(string)))

string = "{[{}][][({})]}"
print ("Should be true")
print (str(pairs_stack(string)))

string = """
    public static void main(String args[])
    {
        System.out.println("Hello world");
    }
"""

print ("Should be true")
print (str(pairs_stack(string)))

string = "[[[((({{{}}})))]]]"
print ("Should be true")
print (str(pairs_stack(string)))

