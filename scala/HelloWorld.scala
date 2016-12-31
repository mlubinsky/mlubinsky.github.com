// https://madusudanan.com/tags/#Scala
/*
Scala does not have the static keyword as part of the language at all, 
but Scala has  companion objects. Everything inside an object is the static
There are two ways to create a runnable application in Scala. 
1)  using the main method inside of an object 
2)  by extending the App trait :  object RunExample extends App{
*/
object HelloWorld {
  def factorial(a:Int): Int = {
    if(a <=1) 1 else a * factorial(a-1)
  }

  //Stubbed method 
  def not_implemented(): String = ??? 

  def main(args: Array[String]): Unit = {
      println("Hello, world!")
      val fac3  =factorial(3) 
      println("3!="+fac3)

  }
}