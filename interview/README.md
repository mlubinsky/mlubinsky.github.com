https://habr.com/ru/company/skillfactory/blog/582450/



https://www.udemy.com/course/leetcode-in-python-50-algorithms-coding-interview-questions/

https://github.com/BitPunchZ/Leetcode-in-python-50-Algorithms-Coding-Interview-Questions/

https://www.udemy.com/course/master-the-coding-interview-big-tech-faang-interviews

Hard Interview Questions in FAANG - 4 | Live Problem Solving | Interview Cracking Series

https://www.youtube.com/watch?v=8Uk2e7cCuyw


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
