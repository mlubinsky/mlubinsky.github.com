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
def matchMonth(month: String) = month match {
case "March" | "April" | "May" => "It's spring"
case "June" | "July" | "August" => "It's summer"
case "September" | "October" | "November" => "It's autumn"
case "December" | "January" | "February" => "It's winter"
  }
  //Stubbed method 
  def not_implemented(): String = ??? 
  
abstract class Shape
case class Circle(radius: Int) extends Shape
case class Square(length: Int) extends Shape
case class Rectangle(length: Int, width: Int) extends Shape

def perimeter(shape: Shape): Double = shape match {
case Circle(radius) => 2 * Math.PI * radius
case Square(length) => 4 * length
case Rectangle(length, width) => 2 * length + 2 * width
case _ => 0.0
}

//****************************************/
  def main(args: Array[String]): Unit = {
      println("Hello, world!")
      val fac3  =factorial(3) 
      println("3!="+fac3)
      println("Which season November belongs to ? Answer:"+ matchMonth("November")) // will print "It's autumn"
      println("Perimeter of rectangle with sides 10 and 20 ="+perimeter(Rectangle(10, 20))) 

  }
}