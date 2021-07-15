def merge_sorted_lists(l1, l2):
    sorted_list = []

    while (l1 and l2):
        if (l1[0] <= l2[0]): # Compare both heads
            item = l1.pop(0) # Pop from the head
        else:
            item = l2.pop(0)
            
        sorted_list.append(item)

    # Add the remaining of the lists
    sorted_list.extend(l1 if l1 else l2)

    return sorted_list


print " FIND 2 elements in list where sum=target"
#-------------------------------------------
l=[6,2,3,4,5,1]
target=6
d={}

for el in l:
    if d.has_key(target-el):
          print "Found:", el, d[target-el]
    else:
          d[el]=el

################
print " Dictionary examples"
################
print " dict traversal  #1"
for key in d.keys():
   print "key=", key, "value=", d[key]

print " dict traversal  #2"
for key, value in d.items():
   print "key=", key, "value=", value

missing=d.get(15,0)
print "missing key=15 default value=", missing
print d.keys()
print d.values()
print d.items()


print "Count the number of times each word is seen in a file"
myfile=("A","B","C","D","A")
words = {}

for word in myfile:
    occurrences = words.setdefault(word, 0)
    words[word] = occurrences + 1

for key, value in words.items():
   print "key=", key, "value=", value

##################
print " List examples"
###############
print "list=", l
l.sort()
print "sorted=", l
l.sort(reverse=True)
print "reverse sorted=",l

#################
print " SET examples"
################
my_list=[1,2,2,3,3,3,4]
a=set(my_list)
print a
b=set([3,4,22])
print b.issubset(a)
print a.difference(b)
print b.difference(a)
if len(a.difference(a)) == 0:
   print "No difference with myself"

a.discard(4)
a.discard(8)

union= a | b
print union
print a.union(b)

####################
print  "String examples"
####################
s='abcdef'
print len(s)
print "find example exists", s.find('a')
print "find example not exists", s.find('g')
try:
    s.index('g')
except:
   print "exceptioni in index()"
else:
  print "else"




def permutations(word):
    print "All permutations of " , word
    if len(word)<=1:
        return [word]

    #get all permutations of length N-1
    perms=permutations(word[1:])
    char=word[0]
    result=[]
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result

print permutations("123")

