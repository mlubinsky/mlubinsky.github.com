
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
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 


```



https://habr.com/ru/company/skillfactory/blog/582450/

https://habr.com/ru/company/skillfactory/blog/539058/

https://habr.com/ru/company/ruvds/blog/515258/. Algorithms

https://habr.com/ru/company/skillfactory/blog/538536/ interview

https://medium.com/swlh/my-preparation-journey-for-google-interviews-f41e2dc3cdf9 interview

https://habr.com/ru/post/539166/ Algo

https://habr.com/ru/post/535216/ interview

https://habr.com/ru/post/550088/ interview

https://paddy3118.blogspot.com/2021/02/longest-common-substring-investigation.html. longest common substr


find the longest palindrome subsequence of a string optimally

https://alkeshghorpade.me/post/leetcode-longest-substring-without-repeating-characters

https://oddblogger.com/recursion-memoization-dynamic-programming-lcs-problem/

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

<https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46>

<https://habr.com/ru/post/503602/>

<https://crunchskills.com/binary-tree-interview-questions-and-practice-problems/>

<https://crunchskills.com/google-interview-questions-for-software-engineering-roles/>


https://medium.com/dev-genius/15-binary-tree-coding-problems-from-faang-interview-2ba1ec67d077

https://medium.com/@srajaninnov/find-the-diameter-of-a-binary-tree-efc45b9129a7


<https://habr.com/ru/company/spice/blog/478250/>

<https://habr.com/ru/company/spice/blog/479320/>

<https://rcoh.me/posts/linear-time-median-finding/>.      MEDIAN finding 


<https://github.com/programmercave0/Algo-Data-Structure/blob/master/README.md>

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



<https://yangshun.github.io/tech-interview-handbook/>

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

https://www.udemy.com/course/master-the-coding-interview-big-tech-faang-interviews/. Udemy

https://www.udemy.com/course/leetcode-in-python-50-algorithms-coding-interview-questions/

https://github.com/BitPunchZ/Leetcode-in-python-50-Algorithms-Coding-Interview-Questions/


https://www.pythonforbeginners.com/queue/queue-in-python


https://www.youtube.com/watch?v=Dx5eiQdv4k8 Find 2 closest points on plain

https://ekamperi.github.io/programming/2021/04/14/longest-non-repeating-substring.html

https://kalkicode.com/data-structure/1500-most-common-data-structures-and-algorithms-solutions

https://stackoverflow.com/questions/67526076/what-is-the-most-efficient-way-of-getting-the-intersection-of-k-sorted-arrays

https://github.com/StBogdan/CTCI_python Cracking code interview

https://runestone.academy/runestone/books/published/pythonds/index.html#problem-solving-with-algorithms-and-data-structures-using-python

https://news.ycombinator.com/item?id=25519718 Interview advice that got me offers 

https://www.youtube.com/watch?v=kbx7xpSKBaI climbing stairs



https://www.udemy.com/course/master-the-coding-interview-big-tech-faang-interviews


https://habr.com/ru/company/otus/blog/565988/ . Median in the stream


https://betterprogramming.pub/top-5-hardest-coding-questions-from-recent-faang-interviews-d46bcb4dd8dc


https://www.pythonforbeginners.com/data-structures

https://mccme.ru/shen/progbook/7edition.pdf

https://habr.com/ru/post/576558/

https://habr.com/ru/post/579410/ interview for ML



Hard Interview Questions in FAANG - 4 | Live Problem Solving | Interview Cracking Series

https://www.youtube.com/watch?v=8Uk2e7cCuyw

System design interview

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
