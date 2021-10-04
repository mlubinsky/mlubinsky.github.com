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


### Pattern matching

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


### App
App is a helper class that holds the main method and its Members together. 
The App trait can be used to quickly turn Objects into Executable programs. We can have our classes extend App to render the executable code.

```
object Edureka extends App{
     println("Hello World")
   }
```

A Higher-order function is a function that does at least one of the following: 
- takes one or more Functions as Arguments
- returns a Function as its result.
   
### Closure   
Closure is considered as a Function whose return value is dependent upon the value of one or more variables declared outside the closure function.

val multiplier = (i:Int) => i * 10

### Trait
A Trait can be defined as a unit which Encapsulates the method and its variables or fields. 
The following example will help us understand in a better way.

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

#### Private:

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
 

### a Monad in Scala?

A Monad is an object that wraps another object. You pass the Monad mini-programs,
i.e functions, to perform the data manipulation of the underlying object, instead of manipulating the object directly.  
Monad chooses how to apply the program to the underlying object.



 

### Scala Anonymous Function.

Ans: In the Source code, Anonymous functions are called ‘Function literals’ and at run time, 
function literals are instantiated into objects called Function values. 
Scala provides a relatively easy Syntax for defining Anonymous functions:
 
 
(z:Int, y:Int)=> z*y
Or
(_:Int)*(_Int)
 

###  How do I Append data in a list?

Ans: In Scala to Append into a List, We have the following methods:
```
use “:+” single value
var myList = List.empty[String]
myList :+= "a"
```
 
