https://scastie.scala-lang.org/ Online Scala compiler

<https://riiswa.github.io/Scala-CheatSheet/>

 

The Scala book:

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


### Var vs Val

Val the reference cannot be changed to point to another reference
Val keyword in Scala can be related to the functionality of java final keyword. To simplify it, Val refers to immutable declaration of a variable whereas var refers to mutable declaration of a variable in Scala.

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

### Arrays

```
var z = new Array[Int](5)
var myMatrix = ofDim[Int](3,3)  -- We use ofDim to declare multidimensional arrays.

We use Range() method to generate an array containing a sequence of increasing integers in a given range.


def range( start: Int, end: Int, step: Int ): Array[Int]
 
range (10, 20, 2)
```


###  Append data in a list

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

### Tuple
Unlike an Array or List, a tuple is Immutable and can hold objects with different Datatypes.
Scala tuples combine a fixed number of items together so that they can be passed around as whole. A tuple is immutable and can hold objects with different types, unlike an array or list.

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

### Trait

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

 There are mainly three access Modifiers available in Scala. Namely,

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
