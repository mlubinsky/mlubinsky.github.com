//https://bradcollins.com/tag/scala/
// scala>   :load examples.scala
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