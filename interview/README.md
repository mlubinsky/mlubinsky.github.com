### Udemy

https://www.udemy.com/course/master-the-coding-interview-big-tech-faang-interviews/. Udemy

https://www.udemy.com/course/leetcode-in-python-50-algorithms-coding-interview-questions/

https://www.udemy.com/course/master-the-coding-interview-big-tech-faang-interviews


<https://www.udemy.com/11-essential-coding-interview-questions/?couponCode=AMAZON2>


### Github

<https://github.com/programmercave0/Algo-Data-Structure/blob/master/README.md>

<https://yangshun.github.io/tech-interview-handbook/>

<https://github.com/mission-peace/interview/tree/master/src/com/interview>

<https://github.com/donnemartin/interactive-coding-challenges>

<https://github.com/alexhagiopol/cracking-the-coding-interview>

<https://github.com/charulagrl/data-structures-and-algorithms>

<https://github.com/thundergolfer/interview-with-python/tree/master/solutions/python>

<https://github.com/anubhavshrimal/Data_Structures_Algorithms_In_Python>

<https://github.com/bt3gl/Python-and-Algorithms-and-Data-Structures/>

https://github.com/BitPunchZ/Leetcode-in-python-50-Algorithms-Coding-Interview-Questions/

https://ekamperi.github.io/programming/2021/04/14/longest-non-repeating-substring.html

https://github.com/StBogdan/CTCI_python Cracking code interview

<https://github.com/parineeth/tbboci-3rd-edition-python>

https://github.com/alexeygrigorev/data-science-interviews . 

https://github.com/labuladong/fucking-algorithm/tree/english. Leetcode guide

<https://github.com/30-seconds/30-seconds-of-python-code>

<https://github.com/TheAlgorithms/Python>


<https://github.com/devAmoghS/Practice-Problems>

<https://github.com/tayllan/awesome-algorithms>

<https://github.com/karan/Projects>



## Merging 2 sorted arrays
into 1st array where 1st array has the capacity for both
```
private void merge(int[] a, int n, int[] b, int m) {
	int i = n - 1;
	int j = m - 1;
	int k = n + m - 1;
	
	while (j >= 0) {
		if (i>=0 && a[i] > b[j])
			a[k--] = a[i--];
		else
			a[k--] = b[j--];
	}
}


# Python program to determine if two trees are identical 
  
# A binary tree node has data, pointer to left child 
# and a pointer to right child 
class Node: 
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
      
  
# Given two trees, return true if they are structurally 
# identical 
def identicalTrees(a, b): 
      
    # 1. Both empty 
    if a is None and b is None: 
        return True 
  
    # 2. Both non-empty -> Compare them 
    if a is not None and b is not None: 
        return ((a.data == b.data) and 
                identicalTrees(a.left, b.left)and
                identicalTrees(a.right, b.right)) 
      
    # 3. one empty, one not -- false 
    return False
  
# Driver program to test identicalTress function 
root1 = Node(1) 
root2 = Node(1) 
root1.left = Node(2) 
root1.right = Node(3) 
root1.left.left = Node(4) 
root1.left.right = Node(5) 
  
root2.left = Node(2) 
root2.right = Node(3) 
root2.left.left = Node(4) 
root2.left.right = Node(5) 
  
if identicalTrees(root1, root2): 
    print "Both trees are identical"
else: 
    print "Trees are not identical"

```
http://www.cmsmagazine.ru/library/items/programming/80-problems-with-it-interviews/



https://habr.com/ru/company/skillfactory/blog/582450/

https://habr.com/ru/company/skillfactory/blog/539058/

https://habr.com/ru/company/ruvds/blog/515258/. Algorithms

https://habr.com/ru/company/skillfactory/blog/538536/ interview

https://medium.com/swlh/my-preparation-journey-for-google-interviews-f41e2dc3cdf9 interview

https://habr.com/ru/post/539166/ Algo

https://habr.com/ru/post/535216/ interview

https://habr.com/ru/post/550088/ interview

### String Algo

https://paddy3118.blogspot.com/2021/02/longest-common-substring-investigation.html. longest common substr


find the longest palindrome subsequence of a string optimally

https://alkeshghorpade.me/post/leetcode-longest-substring-without-repeating-characters



https://johnlekberg.com/blog/2020-08-01-task-order.html . topological sort

https://medium.com/javascript-in-plain-english/facebook-coding-interview-questions-9e40bdbbec35

https://akshayr.me/blog/articles/python-dictionaries

https://medium.com/better-programming/dynamic-programming-interview-questions-maximum-profit-in-job-scheduling-6c5ec15c4cc5

https://medium.com/better-programming/cracking-the-amazon-interview-cf6a6c5f954a

https://blog.pragmaticengineer.com/data-structures-and-algorithms-i-actually-used-day-to-day/


https://www.youtube.com/watch?v=2yWf3TrJ6Xs&feature=youtu.be

<https://habr.com/ru/post/499394/>

https://www.youtube.com/channel/UCZCFT11CWBi3MHNlGf019nw/videos

<https://www.algoexpert.io/systems/product>

<https://algorithmica.org/ru/>

<https://medium.com/@andreimargeloiu/how-to-prepare-for-competitive-programming-396d557e0c12>

<https://medium.com/swlh/binary-search-cheat-sheet-for-coding-interviews-9c5425af357e>

<https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46> Median of 2 sorted attays

<https://habr.com/ru/post/503602/>

<https://crunchskills.com/binary-tree-interview-questions-and-practice-problems/>

<https://crunchskills.com/google-interview-questions-for-software-engineering-roles/>


https://medium.com/dev-genius/15-binary-tree-coding-problems-from-faang-interview-2ba1ec67d077

https://medium.com/@srajaninnov/find-the-diameter-of-a-binary-tree-efc45b9129a7


<https://habr.com/ru/company/spice/blog/478250/>

<https://habr.com/ru/company/spice/blog/479320/>

<https://rcoh.me/posts/linear-time-median-finding/>.      MEDIAN finding 




<https://data-flair.training/blogs/python-programming-interview-questions/>

<https://data-flair.training/blogs/top-python-interview-questions-answer/>

<https://firstround.com/review/40-favorite-interview-questions-from-some-of-the-sharpest-folks-we-know/>

<https://news.ycombinator.com/item?id=20897510>

<https://medium.com/@alexgolec/google-interview-problems-ratio-finder-d7aa8bf201e3>

<https://habr.com/ru/post/467371/> Разбор задачи с собеседования Google: поиск соотношения

<https://www.youtube.com/watch?v=xYBKMV92YrM>



<https://classicproblems.com/>

<https://teachyourselfcs.com/>

<https://web.stanford.edu/class/cs9/>

<https://algodaily.com/challenges>

<https://news.ycombinator.com/item?id=20729252>

<https://habr.com/ru/company/skillbox/blog/462979/>





<https://www.youtube.com/watch?v=EuPSibuIKIg>


<https://www.youtube.com/channel/UCaYQbIciTyBFMTRE2Zp81tw>

<https://www.youtube.com/watch?v=2H_2UGsRmLE&list=PLuVT2Ug8ISOXYhtc-mSeAnJYMbI3WKY5o&index=5&t=0s>

<https://medium.com/@ratulsaha/preparing-for-programming-interview-as-a-phd-student-with-python-5f8af8b40d5f>

<https://www.youtube.com/watch?v=jM2dhDPYMQM>. Sliding window

<https://malisper.me/an-algorithm-for-passing-programming-interviews/>

### Facebook

https://levelup.gitconnected.com/cracking-the-top-40-facebook-coding-interview-questions-185bab32489f

https://daqo.medium.com/facebook-senior-software-engineer-interview-the-only-post-youll-need-to-read-e4604ff2336d

https://news.ycombinator.com/item?id=25658098

https://doisinkidney.com/posts/2019-06-04-solving-puzzles-without-your-brain.html

https://cp-algorithms.com/

https://tproger.ru/articles/problems/


https://www.pythonpool.com/knapsack-problem-python/






https://www.pythonforbeginners.com/queue/queue-in-python


https://www.youtube.com/watch?v=Dx5eiQdv4k8 Find 2 closest points on plain



https://kalkicode.com/data-structure/1500-most-common-data-structures-and-algorithms-solutions

https://stackoverflow.com/questions/67526076/what-is-the-most-efficient-way-of-getting-the-intersection-of-k-sorted-arrays



https://runestone.academy/runestone/books/published/pythonds/index.html#problem-solving-with-algorithms-and-data-structures-using-python

https://news.ycombinator.com/item?id=25519718 Interview advice that got me offers 

https://www.youtube.com/watch?v=kbx7xpSKBaI climbing stairs





https://habr.com/ru/company/otus/blog/565988/ . Median in the stream


https://betterprogramming.pub/top-5-hardest-coding-questions-from-recent-faang-interviews-d46bcb4dd8dc


https://www.pythonforbeginners.com/data-structures

https://mccme.ru/shen/progbook/7edition.pdf

https://habr.com/ru/post/576558/

https://habr.com/ru/post/579410/ interview for ML

## Print the outlier nodes in binary tree
<https://www.jeffcarp.com/posts/2018-how-to-solve-every-software-engineering-interview-question/> 


<https://habr.com/ru/post/457042/> . Tree traversal using 2 threads (Java)

## LCA
<https://en.wikipedia.org/wiki/Lowest_common_ancestor>
<https://sites.google.com/site/mytechnicalcollection/algorithms/trees/lca-of-binary-tree>
<https://stackoverflow.com/questions/1484473/how-to-find-the-lowest-common-ancestor-of-two-nodes-in-any-binary-tree>


<https://www.youtube.com/channel/UCcAWgbpROQrPok18E6UozWw/videos>

<https://www.facebook.com/tusharroy25/>



<https://blog.finxter.com/python-interview-questions/>

<https://stackoverflow.com/questions/11897088/diameter-of-binary-tree-better-design>

<http://www.interviewdruid.com/>

<https://www.amazon.com/dp/1983861189>

<https://www.algoexpert.io/product>

<https://www.hackerrank.com/>

<https://www.interviewbit.com/>

<https://www.quora.com/How-do-I-learn-algorithms-2>

<https://skillupper.com/>

<https://moultano.wordpress.com/2018/11/08/minhashing-3kbzhsxyg4467-6/>

<https://moultano.wordpress.com/2018/11/08/minhashing-3kbzhsxyg4467-6/>

<https://habr.com/post/430788/>

<https://stackabuse.com/graph-data-structure-interview-questions/>

<http://www.java67.com/2018/05/top-75-programming-interview-questions-answers.html>

Hard Interview Questions in FAANG - 4 | Live Problem Solving | Interview Cracking Series

https://www.youtube.com/watch?v=8Uk2e7cCuyw



<https://techiedelight.quora.com/500-Data-Structures-and-Algorithms-interview-questions-and-their-solutions>

<https://blog.usejournal.com/i-interviewed-at-six-top-companies-in-silicon-valley-in-six-days-and-stumbled-into-six-job-offers-fe9cc7bbc996>

<https://www.businessinsider.fr/us/microsoft-new-developer-interview-process-2018-12>

<https://stackabuse.com/programming-interview-questions/>

<https://bradfieldcs.com/algos/>

<http://rachitiitr.blogspot.com/>

<https://www.youtube.com/watch?v=4NIb9l3imAo>

disjoint set union (DSU) или Union-Find.
<https://habr.com/ru/post/104772/>
создать быструю структуру, которая поддерживает следующие операции:

MakeSet(X) — внести в структуру новый элемент X, создать для него множество размера 1 из самого себя.
Find(X) — возвратить идентификатор множества, которому принадлежит элемент X. В качестве идентификатора мы будем выбирать один элемент из этого множества — представителя множества. Гарантируется, что для одного и того же множества представитель будет возвращаться один и тот же, иначе невозможно будет работать со структурой: не будет корректной даже проверка принадлежности двух элементов одному множеству if (Find(X) == Find(Y)).

Unite(X, Y) — объединить два множества, в которых лежат элементы X и Y, в одно новое.


<http://iolivia.me/posts/4-bloom-filter-part-3/> Bloom filter

<https://stackoverflow.com/questions/2936213/explain-how-finding-cycle-start-node-in-cycle-linked-list-work>

<https://stackoverflow.com/questions/41515081/algorithm-find-all-permutations-of-string-a-in-string-b>

<https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/>

<http://www.java67.com/2018/05/top-75-programming-interview-questions-answers.html>

<http://www.algorithmsilluminated.org/>

<https://able.bio/daqo/landing-a-software-engineering-job-at-facebook--78k4a0s>

<https://habr.com/ru/company/digital-ecosystems/blog/473018/> Facebook 
 


<https://www.geeksforgeeks.org/union-find/> union-find (disjoint-set)

<https://habr.com/ru/company/edison/blog/481304/>

<http://blog.amynguyen.net/?p=853>

<https://news.ycombinator.com/item?id=18236396> .  Favorite algos

<https://aryaboudaie.com/interviews/python/technical/2017/11/06/python-for-interviews.html>

<https://algoexpert.io/rachit>  Use "rachit" as coupon code to get 30% off

<http://quiz.geeksforgeeks.org/amazons-most-frequently-asked-interview-questions-set-2/>

<https://www.geeksforgeeks.org/amazons-asked-interview-questions/>

<https://habr.com/ru/post/112222/> heap

<https://medium.com/educative/3-month-coding-interview-bootcamp-904422926ce8>

<https://habr.com/ru/post/437702/> Разбор задачи с собеседования в Google: синонимичные запросы

<http://algorithms.wtf/> 

<https://www.byte-by-byte.com/google-interview/>

<https://courses.csail.mit.edu/iap/interview/materials.php>


https://www.advancedalgorithms.com/ru. Advanced algo (ru)



<https://m.stopa.io/10-offers-100-days-the-journey-16a0407b8d95> interview
<https://habr.com/ru/post/454264/> . Inteview

<https://hackernoon.com/20-string-coding-interview-questions-for-programmers-6b6735b6d31c>

<https://medium.com/@fahimulhaq/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed>

<https://www.solutionfactory.in/posts/Floyd-Cycle-Detection-Algorithm-in-Java> Cycle detection

<https://docs.google.com/spreadsheets/d/1GOO4s1NcxCR8a44F0XnsErz5rYDxNbHAHznu4pJMRkw/edit#gid=0>

<https://www.youtube.com/watch?v=9clnwaqOU2E> string algo

<https://www.globalsoftwaresupport.com/most-common-programming-interview-questions-in-2019/>



<https://habr.com/ru/post/442352/> Бинарные деревья поиска

<https://www.youtube.com/watch?v=lpO_arK69vg> LCA


<https://www.youtube.com/watch?v=bBPHpH8aKjw> look fo links here!

##  Google interview
<https://habr.com/post/419945/>

<https://news.ycombinator.com/item?id=18374938>

<https://habr.com/company/google/blog/425279/> 

https://medium.com/@alexgolec/google-interview-questions-deconstructed-the-knights-dialer-f780d516f029


<https://www.youtube.com/watch?v=5o-kdjv7FD0>

<https://interviewing.io/recordings>

<https://habr.com/post/419725/> Non-symmetric dime simulation

<http://www.cmsmagazine.ru/library/items/programming/80-problems-with-it-interviews/>

<https://saru.science/tech/2017/01/18/judy-arrays.html> Judy array

<https://www.reddit.com/r/cpp/comments/9afpq7/whats_your_favorite_data_structure/>

<https://habr.com/post/420605/>

<https://discuss.codechef.com/questions/48877/data-structures-and-algorithms>

<https://www.youtube.com/watch?v=1CxyVdA_654> Running mediam in stream

<https://www.youtube.com/watch?v=IHsX70r-fIQ> Max sub-sequence in string

<https://hackernoon.com/50-data-structure-and-algorithms-interview-questions-for-programmers-b4b1ac61f5b0>

<https://stackoverflow.com/questions/3260653/algorithm-to-find-top-10-search-terms/3260905#3260905>

<https://blog.datopia.io/2018/11/03/hitchhiker-tree/>



<http://yucoding.blogspot.com/2017/01/leetcode-question-range-sum-query.html>
<http://massivealgorithms.blogspot.com/>
<http://ruslanledesma.com/>
<http://algorithms.tutorialhorizon.com/>







### System design interview

https://www.amazon.com/System-Design-Interview-Insiders-Guide-ebook-dp-B08B3FWYBX/dp/B08B3FWYBX/ref=mt_other?_encoding=UTF8&me=&qid=


https://www.educative.io/blog/cracking-top-facebook-coding-interview-questions

https://platform.stratascratch.com/coding

https://www.interviewquery.com/blog-google-data-engineer-interview-questions/

Salary website: https://www.levels.fyi/
System design youtube channel (Gaurav Sen): https://www.youtube.com/channel/UCRPM...
System design website: https://github.com/donnemartin/system...
Amazon leadership principles: https://www.amazon.jobs/en/principles
Competitive coding:  leetcode.com, geeksforgeeks.org
Mock interviews, salary negotiation consulting:  interviewing.io, interviewkickstart.com

https://cloudirregular.substack.com/p/the-greatest-resume-ive-ever-seen


## Fibonacci

https://habr.com/ru/post/261159/

<https://habr.com/ru/post/449616/> 

<https://habr.com/ru/post/450594/> 

<http://www.oranlooney.com/post/fibonacci/>

<https://news.ycombinator.com/item?id=19216356>

<https://www.reddit.com/r/programming/comments/d1tgmy/computing_fibonacci_numbers_in_olog_n_using/>  Computing Fibonacci Numbers In O(log n) using matrices and eigenvalues



Inverting a binary tree:
The root is still the root, but everything else is just flipped:
https://leetcode.com/problems/invert-binary-tree/
```

  TreeNode* invertTree(TreeNode* root) {
    if (root) {
      invertTree(root->left);
      invertTree(root->right);
      std::swap(root->left, root->right);
    }
    return root;
  }


 invert(tree):
      if(tree not null):
        temp := tree.left
        tree.left <- tree.right
        tree.right <- temp
        invert(tree.left)
        invert(tree.right)
        
 ```       
 
 
 
### Find 1st element in rotated sorted array

 ```
    def bs(lst, start, end):
       print ("start=",start, "end=", end)
       if start == end:  return start
       m = (start+end)//2
       print ("middle=",m, lst[m])

       if m < end and lst[m+1] < lst[m]:
          return m+1
       if m > start and lst[m] < lst[m-1]:
          return m

       if lst[end] > lst[m]:
          return bs(lst, start, m -1)
       else:
          return  bs(lst, m+1, end)

    def find(l):
      start=0
      end=len(l)-1
      i= bs(l, start, end)
      return i

    if __name__ =="__main__":
      print ("main")
      l1=[5,10,20, 1,2,3,4]
      print(l1)
      i=find(l1)
      print ("index=",i)

      l2=[20, 1,2,3,4]
      print(l2)
      i=find(l2)
      print ("index=",i)
```
