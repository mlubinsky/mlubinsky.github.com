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

  //Find 2 elements in sorted array where pair of elements = target
  def one_pair(a: Array[Int], target: Int): Option[(Int, Int)] = {

    var left = 0
    var right = a.length - 1
    var result: Option[(Int, Int)] = None
    while (left < right && result.isEmpty) {
      (a(left), a(right)) match {
        case (x, y) if x + y == target => result = Some(x, y)
        case (x, y) if x + y < target => left = left + 1
        case (x, y) if x + y > target => right = right - 1
      }
    }
    result
  }

  def all_pairs(a: Array[Int], target: Int): List[(Int, Int)] = {

    var left = 0
    var right = a.length - 1
    var result: List[(Int, Int)] = List()
    while (left < right) {
      (a(left), a(right)) match {
        case (x, y) if x + y == target => result = result :+ (x, y); left = left + 1
        case (x, y) if x + y < target => left = left + 1
        case (x, y) if x + y > target => right = right - 1
      }
    }
    result
  }

  //Сначала мы сформируем ленивый список (stream) всех "кандидатов":
  def streamOfPairs(a: Array[Int], target: Int): Stream[(Int, Int)] =
    Stream.iterate(a) { xs => if (xs.head + xs.last > target) xs.init else xs.tail }
      .take(a.length - 1)
      .map { xs => (xs.head, xs.last) }

  //А теперь из полученного "стрима" легко получим как одну, так и все искомые пары:
  def pair(a: Array[Int], target: Int): Option[(Int, Int)] =
    streamOfPairs(a, target) find { case (x, y) => x + y == target }

  def pairs(a: Array[Int], target: Int): List[(Int, Int)] =
    (streamOfPairs(a, target) filter { case (x, y) => x + y == target }).toList

//****************************************/
  def main(args: Array[String]): Unit = {
      println("Hello, world!")
      val fac3  =factorial(3)
      println("3!="+fac3)
      println("Which season November belongs to ? Answer:"+ matchMonth("November")) // will print "It's autumn"
      println("Perimeter of rectangle with sides 10 and 20 ="+perimeter(Rectangle(10, 20)))
      println("Find 2 elements in sorted array where sum of elements=5  "+one_pair(Array(0,1,2,3,4,5), 5))
      println("Find all pair elements in sorted array where sum of elements=5  "+all_pairs(Array(0,1,2,3,4,5), 5))
      println("Find 2 elements in sorted array where sum of elements=5 using stream "+one_pair(Array(0,1,2,3,4,5), 5))
      println("Find all pair elements in sorted array where sum of elements=5 using stream "+all_pairs(Array(0,1,2,3,4,5), 5))

  }


}