/*
Case classes are special because Scala automatically creates a companion object for them:
a singleton object that contains not only an apply method for creating new instances of the case class,
but also an unapply method – the method that needs to be implemented by an object in order for it to be an extractor.

http://danielwestheide.com/blog/2012/11/21/the-neophytes-guide-to-scala-part-1-extractors.html
*/
val xs = 3 :: 6 :: 12 :: Nil
xs match {
  case List(a, b) => a * b
  case List(a, b, c) => a + b + c
  case _ => 0
}

case class Player(name: String, score: Int)

def printMessage(player: Player) = player match {
  case Player(_, score) if score > 100000 => println("Get a job, dude!")
  case Player(name, _) => println("Hey " + name + ", nice to see you again!")
}

val xs = 3 :: 6 :: 12 :: 24 :: Nil
xs match {
  case List(a, b, _*) => a * b
  case _ => 0
}

object GivenNames {
  def unapplySeq(name: String): Option[Seq[String]] = {
    val names = name.trim.split(" ")
    if (names.forall(_.isEmpty)) None else Some(names)
  }
}
def greetWithFirstName(name: String) = name match {
  case GivenNames(firstName, _*) => "Good morning, " + firstName + "!"
  case _ => "Welcome! Please make sure to fill in your name!"
}
// http://danielwestheide.com/blog/2012/11/28/the-neophytes-guide-to-scala-part-2-extracting-sequences.html
def gameResults(): Seq[(String, Int)] =
  ("Daniel", 3500) :: ("Melissa", 13000) :: ("John", 7000) :: Nil

def hallOfFame = for {
  result <- gameResults()
  (name, score) = result
  if (score > 5000)
} yield name

def hallOfFameBetter = for {
  (name, score) <- gameResults()
  if (score > 5000)
} yield name

val lists = List(1, 2, 3) :: List.empty :: List(5, 3) :: Nil

for {
  list @ head :: _ <- lists
} yield list.size


val wordFrequencies = ("habitual", 6) :: ("and", 56) :: ("consuetudinary", 2) ::
  ("additionally", 27) :: ("homely", 5) :: ("society", 13) :: Nil
def wordsWithoutOutliers(wordFrequencies: Seq[(String, Int)]): Seq[String] =
  wordFrequencies.filter(wf => wf._2 > 3 && wf._2 < 25).map(_._1)
wordsWithoutOutliers(wordFrequencies) // List("habitual", "homely", "society")
/*
alternative way of writing anonymous functions: A pattern matching anonymous function
is an anonymous function that is defined as a block consisting of a sequence of cases,
surrounded as usual by curly braces, but without a match keyword
*/
def wordsWithoutOutliers(wordFrequencies: Seq[(String, Int)]): Seq[String] =
  wordFrequencies.filter { case (_, f) => f > 3 && f < 25 } map { case (w, _) => w }
//-----------
 boo: Boolean = 5 < 10
boo match {
  case true => 1
  case false => 0
}

def matchFunction(v: Int) = v match {
  case 1 => "one"
  case 2 => "two"
  case _ => "unknown number"
}
matchFunction(2) //two
matchFunction(5) //unknown number

trait Payment {
  def pay(amount: Double): Unit
}
class Cash extends Payment {
  def pay(amount: Double): Unit = println(s"Pay with cash $amount")
}
class CreditCard extends Payment {
  def pay(amount: Double): Unit = println(s"Pay with credit card $amount")
  def verify(): Unit = println("Verification...")
}

// matching on class
def processPayment(amount: Double, method: Payment) = method match {
  case c: Cash => c.pay(amount)
  case cc: CreditCard => cc.verify(); cc.pay(amount)
  case _ => println("Unknown payment method")
}
val paymentA = new Cash
val paymentB = new CreditCard
processPayment(10, paymentA)
//Pay with cash 10.0
processPayment(50, paymentB)

//Collection pattern matching
val commonList = List(1, 2, 3, 4, 5)
val emptyList = Nil
val oneElement = 'a' :: Nil
def checkList[T](list: List[T]): String = list match {
  case Nil => "Empty list"
  case list :: Nil => "One element"
  case _ => "More than one element"
}
checkList(emptyList) //Empty list
checkList(oneElement) //One element
checkList(commonList) //More than one element

val commonList = List(1, 2, 3, 4, 5)
def sum(list: List[Int]): Int = {
  def recursion(sum: Int, list: List[Int]): Int = list match {
    case Nil => sum
    case el :: tail => (recursion(sum + el, tail))
  }
  recursion(0, list)
}
sum(commonList) //15

/*
Usually, implementing your own extractors is only necessary if you want to extract something from a type
you have no control over, or if you need additional ways of pattern matching against certain data.
For example, a common usage of extractors is to extract meaningful values from some string.
*/
trait User {
  def name: String
}
class FreeUser(val name: String) extends User
class PremiumUser(val name: String) extends User

object FreeUser {
  def unapply(user: FreeUser): Option[String] = Some(user.name)
}
object PremiumUser {
  def unapply(user: PremiumUser): Option[String] = Some(user.name)
}

val user: User = new PremiumUser("Daniel")
user match {
  case FreeUser(name) => "Hello " + name
  case PremiumUser(name) => "Welcome back, dear " + name
}

trait User2 {
  def name: String
  def score: Int
}
class FreeUser2(val name: String, val score: Int, val upgradeProbability: Double)
  extends User
class PremiumUser(val name: String, val score: Int) extends User

object FreeUser2 {
  def unapply(user: FreeUser): Option[(String, Int, Double)] =
    Some((user.name, user.score, user.upgradeProbability))
}
object PremiumUser2 {
  def unapply(user: PremiumUser): Option[(String, Int)] = Some((user.name, user.score))
}

val user2: User2 = new FreeUser2("Daniel", 3000, 0.7d)
user2 match {
  case FreeUser2(name, _, p) =>
    if (p > 0.75) name + ", what can we do for you today?" else "Hello " + name
  case PremiumUser2(name, _) => "Welcome back, dear " + name
}

//-----------------
case class User3(
  id: Int,
  firstName: String,
  lastName: String,
  age: Int,
  gender: Option[String])

object UserRepository {
  private val users = Map(1 -> User(1, "John", "Doe", 32, Some("male")),
                          2 -> User(2, "Johanna", "Doe", 30, None))
  def findById(id: Int): Option[User] = users.get(id)
  def findAll = users.values
}

val user = User3(2, "Johanna", "Doe", 30, None)
user.gender match {
  case Some(gender) => println("Gender: " + gender)
  case None => println("Gender: not specified")
}

val user1 = UserRepository.findById(1)
if (user1.isDefined) {
  println(user1.get.firstName)
} // will print "John"

val user = User3(2, "Johanna", "Doe", 30, None)
println("Gender: " + user.gender.getOrElse("not specified")) // will print "not specified"
/*
Scala’s pattern matching allows to bind the value that is matched to a variable,
too, using the type that the used extractor expects. This is done using the @ operator.
*/
val user = User3(2, "Johanna", "Doe", 30, None)
user.gender match {
  case Some(gender) => println("Gender: " + gender)
  case None => println("Gender: not specified")
}
//-----------------------
val user = User(2, "Johanna", "Doe", 30, None)
val gender = user.gender match {
  case Some(gender) => gender
  case None => "not specified"
}
println("Gender: " + gender)
