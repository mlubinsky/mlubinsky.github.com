import java.util.*;
//A trie (prefix Tree) node should contains the character, its children and the flag that marks if it is a leaf node.
class TrieNode {
   char c;
   HashMap<Character, TrieNode> children = new HashMap<Character, TrieNode>();
   boolean isLeaf;
   public TrieNode() {}
   public TrieNode(char c){
      this.c = c;
   }
}
//------------

public class TrieText {
   private TrieNode root;
   public TrieText(){
      root = new TrieNode();
}
   // Adds a word into the data structure.
   public void addWord(String word) {
      HashMap<Character, TrieNode> children = root.children;
      for(int i=0; i<word.length(); i++){
        char c = word.charAt(i);
        TrieNode t = null;
      } // end for loop
}

// Returns if the word is in the trie.
   public boolean search(String word) {
      TrieNode t = searchNode(word);
      if(t != null && t.isLeaf)
         return true;
      else
         return false;
}
   // Returns if there is any word in the trie
   // that starts with the given prefix.
   public boolean startsWith(String prefix) {
      if(searchNode(prefix) == null)
         return false;
      else
         return true;
}
   public TrieNode searchNode(String str){
      Map<Character, TrieNode> children = root.children;
      TrieNode t = null;
      for(int i=0; i<str.length(); i++){
         char c = str.charAt(i);
         if(children.containsKey(c)){
            t = children.get(c);
            children = t.children;
         }else{
            return null;
         }
      }
      return t;
}



// Returns if the word is in the data structure. A word could
// contain the dot character ’.’ to represent any one letter.
public boolean searchGeneric(String word) {
  return dfsSearch(root.children, word, 0);
}
 public boolean dfsSearch(HashMap<Character, TrieNode> children, String word, int start) {
   if(start == word.length()){
      if(children.size()==0)
         return true;
      else
         return false;
   }
   char c = word.charAt(start);
   if(children.containsKey(c)){
      if(start == word.length()-1 && children.get(c).isLeaf){
         return true;
      }
      return dfsSearch(children.get(c).children, word, start+1);
   }else if(c == '.'){
      boolean result = false;
      for(Map.Entry<Character, TrieNode> child: children.entrySet()){
         if(start == word.length()-1 && child.getValue().isLeaf){
            return true;
         }
         //if any path is true, set result to be true;

         if(dfsSearch(child.getValue().children, word, start+1)){
               result = true;
         }
       }  //end for loop
         return result;
      }else{
         return false;
      }
 }  //end of dfsSearch
}