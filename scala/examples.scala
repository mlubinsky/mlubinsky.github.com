//https://bradcollins.com/tag/scala/
//https://pavelfatin.com/scala-collections-tips-and-tricks/
//https://habrahabr.ru/post/323706/
//https://twitter.github.io/effectivescala/

// scala>   :load examples.scala
// function as parameter
def halfMaker(value: Int): Double = value.toDouble/2

def processRange(start: Int, finish: Int, processor: Int => AnyVal): Unit = {
 for (i <- start to finish)
 println(processor(i))
}

processRange(1,3,halfMaker)

// Anonymous func (lambda)
def moneyTransfer(amount: Double, providerFee: Double => Double): Double = {
 amount + 10 + providerFee(amount)
}
val money=50.0
println(moneyTransfer(val, val => val / 10.0)

//Function as Return Value
def getStrategy(enoughEnergy: Boolean) = {
 if (enoughEnergy)
 (energy: Double) => "We are going to attack with damage "+energy
 else
 (energy: Double) => "We are going to reflect damage "+energy/2
}
val returnedFunction = getStrategy(true)
returnedFunction(15.0)
//We are going to attack with damage 15.0

//*******************
// Scala collections
//*******************
 val numbers = Seq(11, 2, 5, 1, 6, 3, 9)
 println(  numbers.max ) //11
 println(  numbers.min ) //1

case class Book(title: String, pages: Int)
   val books = Seq( Book("Future of Scala developers", 85),
                   Book("Parallel algorithms", 240),
                   Book("Object Oriented Programming", 130),
                   Book("Mobile Development", 495) )
   //Book(Mobile Development,495)
   books.maxBy(book => book.pages)
   //Book(Future of Scala developers,85)
   books.minBy(book => book.pages)

//  Filtering
val numbers = Seq(1,2,3,4,5,6,7,8,9,10)
println (numbers.filter(n => n % 2 == 0))
books.filter(book => book.pages >= 120)

// Flatten

   val abcd = Seq('a', 'b', 'c', 'd')
   val efgj = Seq('e', 'f', 'g', 'h')
   val ijkl = Seq('i', 'j', 'k', 'l')
   val mnop = Seq('m', 'n', 'o', 'p')
   val qrst = Seq('q', 'r', 's', 't')
   val uvwx = Seq('u', 'v', 'w', 'x')
   val yz = Seq('y', 'z')
   val alphabet = Seq(abcd, efgj, ijkl, mnop, qrst, uvwx, yz)
   //  alphabet: Seq[Seq[Char]] = List(List(a, b, c, d), List(e, f, g, h), List(i, j, k, l), List(m, n, o, p), List(q, r, s, t), List(u, v, w, x), List(y, z))

   alphabet.flatten
  // List(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)

// *****************************
//  diff union intersect distinct
// *****************************
val num1 = Seq(1, 2, 3, 4, 5, 6)
   val num2 = Seq(4, 5, 6, 7, 8, 9)
   //List(1, 2, 3)
   num1.diff(num2)
   //List(4, 5, 6)
   num1.intersect(num2)
   //List(1, 2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 9)
   num1.union(num2)
//
//List(1, 2, 3, 4, 5, 6, 7, 8, 9)
num1.union(num2).distinct

// flatMap
// flatMap[B](f: A => Container[B]): Container[B]

// find all permutation of chars: solution #1
val chars = 'a' to 'd'
val perms = chars flatMap { a =>
  chars flatMap { b =>
    if (a != b) Seq("%c%c".format(a, b))
    else Seq()
  }
}

// find all permutation of chars: solution #2
val perms = for {
  a <- chars
  b <- chars
  if a != b
} yield "%c%c".format(a, b)



val xs = Vector(1,2,3,4,5,6)
val mid = xs.length / 2 // 3
val (left, right) = xs splitAt mid

val xs2 = Vector(10,20,30,40,50)
val (left, right) = xs2 splitAt 1

def bisect[A](xs: Vector[A]) = {
  val mid = xs.length / 2
  xs splitAt mid
}

def merge(left: Vector[Int], right: Vector[Int]) = {
  //@tailrec
  def mergeWith(l: Vector[Int], r: Vector[Int], acc: Vector[Int]): Vector[Int] = {
    (l.isEmpty, r.isEmpty) match {
      // If either side is empty, just add
      // the non-empty side to the accumulator.
      case (true, _) => acc ++ r
      case (_, true) => acc ++ l

      // Compare the head elements, and add
      // the lesser head value to the
      // accumulator. Then call recursively.
      case _ =>
        val lh = l.head
        val rh = r.head
        val (next, l2, r2) =
          if (lh < rh) (lh, l.tail, r)
          else (rh, l, r.tail)
        mergeWith(l2, r2, acc :+ next)
    }
  }

  mergeWith(left, right, Vector[Int]())
}

def mergeSort(as: Vector[Int]): Vector[Int] =
  as match {
    case Vector() => as
    case Vector(a) => as
    case _ =>
      val (l, r) = bisect(as)
      merge(mergeSort(l), mergeSort(r))
  }

val xs3 = Vector(43,48,3,23,28,6,25,43,16)
val sorted: Vector[Int] = mergeSort(xs3)


val names = Stream(
  "Rehoboam",
  "Abijah",
  "Asa",
  "Jehoshaphat",
  "Jehoram",
  "Ahaziah")

val groupedByInitial = names.groupBy(_.head)

val groupedByInitialAndSorted =  groupedByInitial.toStream.sortBy(_._1)

case class TestScore(name: String, score: Int)

val grades = Stream(
  TestScore("Anna", 74),
  TestScore("Andy", 76),
  TestScore("Brenda", 70),
  TestScore("Bobby", 90),
  TestScore("Charlotte", 98),
  TestScore("Chuck", 83),
  TestScore("Deborah", 88),
  TestScore("Dan", 66),
  TestScore("Ellie", 80),
  TestScore("Ed", 61),
  TestScore("Frannie", 89),
  TestScore("Frank", 96) )

val grouped = grades.groupBy(_.score / 10 * 10)

val histogram = grouped.map {
  case (grade, scores) => grade -> scores.length
}.toStream.sortBy(_._1).reverse

val anagrams = Stream(
  "tar", "rat", "bar",
  "rob", "art", "orb"
).groupBy(_.sorted)


case class Salesman(name: String, sales: BigDecimal)

def findTopSalesman (salesmen : List[Salesman]) = {
  salesmen.filter { _.sales >= 10000 }
          .sortBy { -_.sales } // descending
          .headOption
}

val sales = List(
  Salesman("Joe Bob", 9500),
  Salesman("Sally Jane", 18500),
  Salesman("Betty Lou", 11800),
  Salesman("Sammy Joe", 6500)
)

val top = findTopSalesman(sales)

val empty = List[Int]()
val nonempty = (9 to 17).toList

val nuthin = empty.headOption
val sumthin = nonempty.headOption
// sumthin: Option[Int] = Some(9)

val empty = List[Int]()
val nonempty = (9 to 17).toList
val head = nonempty.headOption getOrElse -1
val fallback = empty.headOption getOrElse -1

val monday = List(
  Salesman("Joe Bob", 9500),
  Salesman("Sally Jane", 8500),
  Salesman("Betty Lou", 9800),
  Salesman("Sammy Joe", 6500)
)

val mondayTop = findTopSalesman(monday)
// mondayTop: Option[Salesman] = None

val tuesday = List(
  Salesman("Joe Bob", 9500),
  Salesman("Sally Jane", 18500),
  Salesman("Betty Lou", 11800),
  Salesman("Sammy Joe", 6500)
)

val tuesdayTop = findTopSalesman(tuesday)

//generators
var ref0: List[Int] =
  for {
  	 k <- List(0,1,2)
  	 p <- List(3,4,5)
  } yield k * p

var ref1: List[Int] =
  for {
  	 k <- List(0,1,2) if k > 0;
  	 p <- List(3,4,5)
  } yield k * p

 var ref3: List[Int] = List(0,1).filter(_ > 0)
 var ref4: List[Int] = List(0,1).withFilter(_ >0).map(x=>x)

 def fibonacci(term: Int) : Int = {
  //@annotations.tailrec
  def calculate(counter: Int, previous: Int, acc: Int) : Int =
    if (counter == term) acc
    else calculate(counter + 1, acc, acc + previous)

  calculate(0, 1, 0)
}


val votes = Seq(("scala", 1), ("java", 4), ("scala", 10), ("scala", 1), ("python", 10))
val orderedVotes = votes
  .groupBy(_._1)
  .map { case (which, counts) =>
    (which, counts.foldLeft(0)(_ + _._2))
  }.toSeq
  .sortBy(_._2)
  .reverse

val votesByLang = votes groupBy { case (lang, _) => lang }
val sumByLang = votesByLang map { case (lang, counts) =>
  val countsOnly = counts map { case (_, count) => count }
  (lang, countsOnly.sum)
}
val orderedVotes = sumByLang.toSeq
  .sortBy { case (_, count) => count }
  .reverse

