https://scala-cli.virtuslab.org/ CLI

https://scastie.scala-lang.org/ Online Scala compiler

<https://riiswa.github.io/Scala-CheatSheet/>

https://github.com/LucDuponcheelAtGitHub/programming_course

https://habr.com/ru/articles/799235/ Имплиситы и тайпклассы в Scala

https://alvinalexander.com/scala/fp-book/how-write-functions-take-function-input-parameters/

### Examples of partition, sortBy, minBy, head, filter, case, collect, take, drop, split and map
```
val xs=List(1,8,5,6,9,58,23,15,4) ;
val (even, odd) = xs.partition(_ % 2 == 0)

val minByAbs1 = xs.sortBy(Math.abs).head
val minByAbs2 = xs.minBy(Math.abs)    <- this is better because no need to sort

val maxByAbs1 = xs.sortBy(Math.abs).last
val maxByAbs2=xs.maxBy(Math.abs)   <- this is better because no need to sort

val doublesOfPositive = xs.filter(_ > 0).map(2 * _)

val doublesOfPositive = xs.collect {  -- . this is better - why?
  case x if x > 0 => 
    2 * x
}

val leftHalf = xs.take(3)
val rightHalf = xs.drop(3)
val (leftHalf, rightHalf) = xs.splitAt(3)  -- this is better
```

#### grouped

grouped(n) splits the collection into collections with n elements each
(the last one may contain less than n elements, depending on the size of the original collection):
```
xs.grouped(3).toList // List(List(4, 5, 2), List(-1, -3, 4))
```
###

https://blog.indoorvivants.com/2022-02-13-maintaining-scala-open-source-library-part-I

### Scala 3
https://blog.indoorvivants.com/2020-12-30-scala3-video-part-I

https://blog.indoorvivants.com/2021-02-08-scala3-video-part-II

### Scala Native
Scala Native is an ahead of time compiler and standalone runtime allowing to compile Scala code to machine language without the need for the JVM. 

https://medium.com/virtuslab/revisiting-scala-native-performance-67029089f241


### Scala Collections

https://medium.com/wix-engineering/the-little-gems-of-scala-standard-library-32ef298bf0df

https://blog.redelastic.com/a-guide-to-scala-collections-exploring-monads-in-scala-collections-ef810ef3aec3


https://data-flair.training/blogs/scala-tutorial/

 https://www.zeolearn.com/interview-questions/scala
 
 https://data-flair.training/blogs/scala-interview-questions/
 
 https://www.journaldev.com/8958/scala-interview-questions-answers

### The Scala book:

https://www.handsonscala.com/

<https://earthly.dev/blog/top-5-scala-blogs/>

https://bszwej.medium.com/domain-driven-design-with-fp-in-scala-21b557f94aa5

<https://leanpub.com/jvm-scala-book> JVM for Scala

<https://geirsson.com/2019.html> Scala tooling in 2019

<https://ammonite.io/> .   REPL ammonite

<https://www.youtube.com/watch?v=nD-p-cEKjHE> . SBT

<https://blog.softwaremill.com/bootzooka-2019-functional-scala-and-react-3cf8c1a0f1c2>

<https://github.com/ashwinbhaskar/functional-way>

<https://blog.softwaremill.com/how-to-structure-your-scala-application-658168fbb827>

## API 

<https://blog.softwaremill.com/an-open-source-scala-library-for-describing-http-api-endpoints-2955dfc929ac>

<https://www.youtube.com/watch?v=I3loMuHnYqw>


### Integral types

 Integral types: Byte, Short, Int, Long, and Char 

Numerical types: Integral types + Float and Double


### What is _*

### Unary operators

(2.0)unary_-    it is -2.0

 only four prefixes are allowed to use. These are: +, -, !, and ~.

### Var vs Val

Val the reference cannot be changed to point to another reference
Val keyword in Scala can be related to the functionality of java final keyword. To simplify it, Val refers to immutable declaration of a variable whereas var refers to mutable declaration of a variable in Scala.

```
val welcomeStrings = new Array[String](3) 
welcomeStrings(0) = "Welcome" 
welcomeStrings(1) = "to "
welcomeStrings(2) = "ProjectPro"

```

 variable can’t be reassigned a new value if one defines that variable using “val”. However, it is possible to make changes to the object the variable refers to.
 
### String

```
- String trim(): Returns a copy of the string, with leading and trailing whitespace omitted.
- String toUpperCase: Converts all of the characters in this String to upper case using the rules of the given Locale.
- Char[] to CharArray(): Converts this string to a new character array.
- String[] split(String regex): Splits this string around matches of the given regular expression.
- Int length(): returns the length of this string.

Val formatted= “%s %i”.format (mystring.myInt)
```

### Object is a singleton

An object is a singleton, an instance of a class which is unique.
An anonymous class is created for every object in the code, 
it inherits from whatever classes you declared object to implement.

### Companion objects

Companion objects provide a clear separation between static and non-static methods in a class 
because everything that is located inside a companion object is not a part of the class’s runtime objects 
but is available from a static context and vice versa.

According to the private access specifier, private members can be accessed only within that class but Scala’s companion object and class provide special access to private members. A companion object can access all the private members of a companion class. Similarly, a companion class can access all the private members of companion objects.

### Unit means void

Unit is a subtype of scala.anyval and is nothing but Scala equivalent of Java void that provides the Scala with an abstraction of the java platform. 
Empty tuple i.e. () in Scala is a term that represents unit value

###  Function

```
def functionName ([list of parameters]) : [return type] = {
   function body
   return [expression]
}
```

### Seq has many subclasses including Queue, Range, List, Stack, and LinkedList.

A Seq is an Iterable that has a defined order of elements. 

Sequences provide a method apply() for indexing, ranging from 0 up to the length of the sequence. 

 
```
import scala.collection.immutable._  
object MainObject{  
   def main(args:Array[String]){  
       var seq:Seq[Int] = Seq(52,85,1,8,3,2,7)  
       seq.foreach((element:Int) => print(element+" "))  
       println("\nAccessing element by using index")  
       println(seq(2))  
   }
}
```

### List 
A List is a Seq that is implemented as an immutable linked list. 

It's best used in cases with last-in first-out (LIFO) access patterns.
```
import scala.collection.immutable._  
object MainObject{  
   def main(args:Array[String]){  
      var list = List(1,8,5,6,9,58,23,15,4)  
       var list2:List[Int] = List(1,8,5,6,9,58,23,15,4)  
       println(list)  
       println(list2)  
   }
}
```

last element in the list:

```
import scala.collection.immutable._
object HelloWorld {
   def main(args: Array[String]) {
      val temp_list: List[String] = List("Hello", "World", "SCALA", "is", "awesome")
      println("Elements of temp_list: " + temp_list.last)
   }
}
```

### Arrays

```
var z = new Array[Int](5)
 
use Range() method to generate an array containing a sequence of increasing integers in a given range.

def range( start: Int, end: Int, step: Int ): Array[Int]
 
range (10, 20, 2)
```


### Multidimentional array ofDim

``` 
import Array.ofDim
var a=ofDim[Int](3,3)

a: Array[Array[Int]] = Array(Array(0, 0, 0), Array(0, 0, 0), Array(0, 0, 0))

 var k=1
 
 for(i<-0 to 2){
    | for(j<-0 to 2){
    | a(i)(j)={i+k}
    | k+=1
    | }
    | k-=1
    | }
    
scala> a
res12: Array[Array[Int]] = Array(Array(1, 2, 3), Array(4, 5, 6), Array(7, 8, 9)).
```

###  Append data in a List and ListBuffer

Class List in Scala not offer the append function but offers to prepend function?

Ans: This is because of the time it takes to perform both operations. For appending an element to a list in Scala, the time taken grows linearly with the size of the list whereas, prepending an element using the “::” operator takes constant time. 

However, if one wants to use the append function, they can use ListBuffer.



append 1 element using :+
```

var myList = List.empty[String]
myList :+= "a"
myList :+= "b"
myList :+= "c"
```

use ++ for appending a list to list
```
var myList = List.empty[String]
myList ++= List("a", "b", "c")
```

### Differentiate between Array and List  

List is an immutable recursive data structure whilst array is a sequential mutable data structure.
Lists are covariant whilst array are invariants.
The size of a list automatically increases or decreases based on the operations that are performed on it 
i.e. a list in Scala is a variable-sized data structure whilst an array is fixed size data structure.

List and Tuple are immutable, whereas arrays are mutable in Scala.

### Tuple
Unlike an Array or List, a tuple is Immutable and can hold objects with different Datatypes.
Scala tuples combine a fixed number of items together so that they can be passed around as whole. A tuple is immutable and can hold objects with different types, unlike an array or list.

 Capacity of tuples in Scala of the length two to twenty-two.
 
### Set

head: returns the head (first element) of the set
tail: returns entire set except the head element
isEmpty: checks if the set is empty, returns Boolean

### BitSet

 BitSet is a collection of smaller integers represented as bits of the larger integer. 
 We can add multiple items in a bitset using the ‘++’ operator similar to list. 
 Bitsets can be mutable and immutable and are sets of non-negative integers.
 
### Map

val colors = Map("red" -> "#FF0000", "azure" -> "#F0FFFF")



### What is the difference between flatMap() and map() operations?

FlatMap is a transformation operation in Apache Spark to create an RDD from existing RDD. It takes one element from an RDD and can produce 0, 1 or many outputs based on business logic. It is similar to Map operation, but Map produces one to one output. If we perform Map operation on an RDD of length N, output RDD will also be of length N. But for FlatMap operation output RDD can be of different length based on business logic

```
val array1d = Array(“Hello,World”, “This,is,an,example”)
//array1d is an array of strings
val maped_array = array1d.map(x => x.split(“,”))
//maped_array will be: Array(Array(Hello, World), Array(This, is, an, example))
val flatMap_array = array1d.flatMap(x => x.split(“,”))
//flatMap_array will be: Array(Hello, World, This, is, an, example)

```


#### Write a lambda function  using map(), which takes a sequence of salaries as input and outputs double of every element from input.

```
val salaries = Seq(20000, 70000, 40000)
val doubleSalary = (x : Int) => x*2
val newSalary = salaries.map(doubleSalary)

>List(40000, 140000, 80000)
Or

val salaries = Seq(20000, 70000, 40000)
val newSalary = salaries.map(x => x*2)

//List(40000, 140000, 80000)
```


### Exception

```
import java.io.FileReader
import java.io.FileNotFoundException
import java.io.IOException
object Demo {
   def main(args: Array[String]) {
      try {
         val f = new FileReader("input.txt")
      } catch {
         case ex: FileNotFoundException ={
            println("Missing file exception")
         }  
         case ex: IOException = {
            println("IO Exception")
         }
      }
      finally {
         println("Exiting the code...")
      }
   }
}
```

### Recursion
```
def factorial_loop(i: BigInt): BigInt = {
  var result = BigInt(1)
  for (j- 2 to i.intValue)
     result *= j
     result
}

for (i - 1 to 10)
  format("%s: %sn", i, factorial_loop(i))
```  

### Extractor

https://medium.com/wix-engineering/scala-pattern-matching-apply-the-unapply-7237f8c30b41

Extractor in Scala is an object that has a method called unapply as one of its members. 
The purpose of that unapply method is to match the value and take it apart.
apply and unapply methods in Scala are used for mapping and unmapping data between form and model data.

Apply method – Used to assemble an object from its components. For example, if we want to create an Employee object  then use the two components  firstName and lastName and compose the Employee object using the apply method.

Unapply method – Used to decompose an object from its components. It follows the reverse process of apply method. So if you have an employee object, it can be decomposed into two components- firstName and lastName.


### Queue

import scala.collection.mutable.Queue
val empty = new Queue[Int]

### Pattern matching
```
object Demo {
   def main(args: Array[String]) {
      println(matchTest(3))
   } 
   def matchTest(x: Int): String = x match {
      case 1 = "one"
      case 2 = "two"
      case _ = "other"
   }
}
```
Example 2

```
def personDescription(name: String, db: Map[String, Int]): String =
  db.get(name) match {
                      case Some(age) => s"$name is $age years old"
                      case None => s"$name is not present in db"
  }

val db = Map("John" -> 25, "Rob" -> 40)
personDescription("John", db)
// res4: String = John is 25 years old
personDescription("Michael", db)
// res5: String = Michael is not present in db

```

The get(key) method in Map returns Option, containing the value associated with the key. If the key does not exist in Map, it returns None. 
When you start using Option, pattern matching is the most natural way of triggering different behaviors depending on the content of Option.

Another way is to use map and getOrElse, as shown in the following code:

```
def personDesc(name: String, db: Map[String, Int]): String = {
  val optString: Option[String] = db.get(name).map(age => s"$name is  $age years old")
  optString.getOrElse(s"$name is not present in db")
}
```



### Case Classes

Case classes provides a recursive decomposition mechanism via pattern matching, it is a regular classes which export their constructor parameter. 
The constructor parameters of case classes can be accessed directly and are treated as public values.

Case classes are standard classes declared with a special modifier case. Case classes export their constructor parameters and provide a recursive decomposition mechanism through pattern matching. The constructor parameters of case classes are treated as public values and can be accessed directly. For a case class, companion objects and its associated method also get generated automatically. All the methods in the class, as well, methods in the companion objects are generated based on the parameter list. The only advantage of Case class is that it automatically generates the methods from the parameter list.

Features of Case Class in Scala
Case objects and Case class are serializable by default.
Case classes can be used for pattern matching.

### App
App is a helper class that holds the main method and its Members together. 
The App trait can be used to quickly turn Objects into Executable programs. 
We can have our classes extend App to render the executable code.
App is a trait defined in scala package as "scala.App" which defines the main method. 
If an object or class extends this trait then they will become Scala executable programs automatically as they inherit the main method from application.
Developers need not write main method when using App 
but the only drawback of using App is that developers have to use same name args to refer command line arguments because scala.App's main() method uses this name.

```
object Edureka extends App{
     println("Hello World")
   }
```

### Higher-order function  does at least one of the following

- takes one or more Functions as Arguments
- returns a Function as its result.

```
object Test {
   def main(args: Array[String]) {
       println( apply( layout, 10) 
   )
}

def apply(f: Int => String, v: Int) = f(v)

def layout[A](x: A) = "[" + x.toString() + "]"
```

   
### Closure   
Closure is considered as a Function whose return value is dependent upon the value of one or more variables declared outside the closure function.

val multiplier = (i:Int) => i * 10

### Trait va AbstractClasses
```
No| Key                 |	Trait	                                        |     Abstract Class
1	Multiple inheritance  | Trait supports multiple inheritance           | Abstract Class supports single inheritance only.
2	Instance	            | Trait can be added to an object instance.	    | Abstract class cannot be added to an object instance.
3	Constructor parameters|	Trait cannot have parameters in its constructors | Abstract class can have parameterised constructor.
4	Interoperability	    | Traits are interoperable with java if they don't have any implementation.	| Abstract classes are interoperable with java without any restriction.
5	Stackability	        |Traits are stackable and are dynamically bound . |Abstract classes are not stacable and are statically bound.
```

```
trait SampleTrait {
   // Abstract method
   def test

   // Non-Abstract method
   def tutorials() {
      println("Traits tutorials")
   }
}

abstract class SampleAbstractClass {
   // Abstract method
   def test

   // Non-abstract meythod
   def tutorials() {
      println("Abstract Class tutorial")
   }
}

class Tester extends SampleAbstractClass {
   def test() {
      println("Welcome to Tutorialspoint")
   }
}

class TraitTester extends SampleTrait {
   def test() {
      println("Welcome to Tutorialspoint")
   }
}

object HelloWorld {
   // Main method
   def main(args: Array[String]) {
      var obj = new Tester()
      obj.tutorials()
      obj.test()
      var obj1 = new TraitTester()
      obj1.tutorials()
      obj1.test()
   }
}
```

Trait denotes a particular unit of Class that facilitates the use of multiple inheritances. 
It encapsulates a method along with its variables and fields. While a Trait can extend only one Class, a Class can have multiple traits.
Traits are primarily used for dependency injection. Contrary to Java where dependency injection is accomplished through annotations, Scala has no annotations or no special package that needs to be imported — you only need to initialize the Class with the Trait to trigger the dependency injection.

A trait is a special kind of Class that enables the use of multiple inheritance. Although a trait can extend only one class, but a class can have multiple traits. However, unlike classes, traits cannot be instantiated.

A Trait can be defined as a unit which Encapsulates the method and its variables or fields. 
The following example will help us understand in a better way.

‘Traits’ are used to define object types specified by the signature of the supported methods. 
Scala allows to be partially implemented but traits may not have constructor parameters. 
A trait consists of method and field definition, by mixing them into classes it can be reused.
 

If the behaviour will not be reused, then make it a concrete class. Anyhow it is not a reusable behaviour.
In order to inherit from it in Java code, an abstract class can be used.

If efficiency is a priority then lean towards using a class
Make it a trait if it might be reused in multiple and unrelated classes. 
In different parts of the class hierarchy only traits can be mixed into different parts.
You can use abstract class, if you want to distribute it in compiled form and expects outside groups to write classes inheriting from it.

Scala resolves diamond problem through the concept of Traits and class linearization rules.

```
trait Printable{
   def print()
}
class A4 extends Printable{
   def print(){
      println("Hello")
  }
}
object MainObject{
   def main(args:Array[String]){
      var a = new A4()
      a.print()
  }
}
```


### Implicit 
Implicit classes allow Implicit conversations with the class’s Primary constructor when the class is in scope. 
Implicit class is a class marked with the “implicit” keyword. This feature was introduced in with Scala 2.10 version.

```
  object {
      implicit class Data type) {
          def Unit = xyz
       }
  }
``` 

### Explain the access Modifiers available in Scala

 There are mainly three access Modifiers available in Scala: private, protected and public

#### Private

The Accessibility of a private member is restricted to the Class or the Object in which it declared.
The following program will explain this in detail.
```
class Outer {
   class Inner {
      private def f() { println("f") }
       class InnerMost {
         f() // OK
      }
   }
   (new Inner).f() // Error: f is not accessible
}
```
#### Protected:

A protected member is only Accessible from Subclasses of the class in which the member is defined.
The following program will explain this in detail.

```
package p 
  class Super {
      protected def f() { println("f") }
   }
  class Sub extends Super {
      f()
   }
  class Other {
      (new Super).f() // Error: f is not accessible
   }
}
```

#### Public:

Unlike Private and Protected members, it is not required to specify Public keyword for Public members. 
There is no explicit modifier for public members. Such members can be accessed from Anywhere.
Following is the example code snippet to explain Public member

 
class Outer {
   class Inner {
      def f() { println("f") }
       class InnerMost {
         f() // OK
      }
   }
   (new Inner).f() // OK because now f() is public
}
 
 
### Option, some, none

‘Option’ is a Scala generic type that can either be ‘some’ generic value or none. 
‘Queue’ often uses it to represent primitives that may be null.

### Null	Nil	None	Nothing

#### Null represents the absence of a value. 
 It’s a sub-type of AnyRef type in Scala Types hierarchy.
 As Scala runs on JVM, it uses NULL to provide the compatibility with Java null keyword, or in Scala terms, 
 to provide type for null keyword, Null type exists. 
 It represents the absence of type information for complex types that are inherited from AnyRef.



#### Nil denotes the end a List	
It’s a handy way of initializing an empty list since, Nil, is an object, which extends List 

#### None is the value of an Option with no value.	

 In cases, where you don’t know, if you would be able to return a value as expected, we can use Option [T]. 
 It is an abstract class, with just two sub-classes,
 Some [T] and none. 
 With this, we can tell users that, the method might return a T of type Some [T] or it might return none.

#### Nothing is lowest type in type System
  It’s a sub-type of all the types exists in Scala Types hierarchy. It helps in providing the return type for the operations that can affect a normal program’s flow. It can only be used as a type, as instantiation of nothing cannot be done. It incorporates all types under AnyRef and AnyVal. Nothing is usually used as a return type for methods that have abnormal termination and result in an exception.

###  if else
```
object Demo {
   def main(args: Array[String]) {
      var x = 30;
      if( x == 10 ){
         println("Value of X is 10")
      } else if( x == 20 ){
         println("Value of X is 20");
      } else if( x == 30 ){
         println("Value of X is 30");
      } else{
         println("This is else statement");
      }
   }
}
```
###  Monad in Scala

A Monad is an object that wraps another object. You pass the Monad mini-programs,
i.e functions, to perform the data manipulation of the underlying object, instead of manipulating the object directly.  
Monad chooses how to apply the program to the underlying object.


### Yield 
is used with a loop, Yield produces a value for each iteration. Another way to do is to use map/flatMap and filter with nomads.

 
for (i <- 1 to 5) yield i
 

### Scala Anonymous Function.

Ans: In the Source code, Anonymous functions are called ‘Function literals’ and at run time, 
function literals are instantiated into objects called Function values. 
Scala provides a relatively easy Syntax for defining Anonymous functions:
 
 
(z:Int, y:Int)=> z*y
Or
(_:Int)*(_Int)
 

### Packages

- Java.lang._: It is a package that provides classes that are fundamental for the design of the Java programming language.
- Java.io._: It is a package that imports every class in Scala for input-output resources.
- PreDef: It offers type aliases for types that are used regularly used in Scala. These include Safe, Map, and the List constructors.
 

### Future

Scala Future is a monadic collection, which starts a background task. 
It is an object which holds the potential value or future value, which would be available after the task is completed. 
It also provides various operations to further chain the operations or to extract the value. 
Future also provide various call-back functions like 
  onComplete, 
  OnFailure, 
  onSuccess 
to name a few, which makes Future a complete concurrent task class. 
The main and foremost difference between Scala’s Future and Java’s Future class is that the later does not provide promises/callbacks operations. 

### Streams


Streams in Scala are a type of lazy collection, which are created using starting element and then recursively generated using those elements. Streams are like a List, except that, elements are added only when they are accessed, hence “lazy”. Since streams are lazy in terms of adding elements, they can be unbounded also, and once the elements are added, they are cached. Since Streams can be unbounded, and all the values are computed at the time of access, programmers need to be careful on using methods which are not transformers, as it may result in java.lang.OutOfMemoryErrors.

stream.max

stream.size

stream.sum


### Invalid code no j++ in Scala:

```
var i = 0 
while (j < args.length) { 
    println(args(i)) 
    j++
} 
```
