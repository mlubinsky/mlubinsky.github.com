/*
Currying – decomposition of function with multiple arguments into a chain of single-argument functions.
Notice, that Scala allows to pass a function as an argument to another function.

Partial application of function – pass to function less arguments than it has in its declaration. Scala does not throw an exception when you provide less arguments to function, it simply applies them and return a new function with rest of arguments which need to be passed.
*/

def sum(a: Int, b: Int): Int = a + b
//(Int, Int) => Int

def curriedSum = (sum _).curried
//Int => (Int => Int)

curriedSum(5)
//Int => Int


def isInRange(left: Int, n: Int, right: Int): Boolean = {
    if (left < n && n < right) true else false
}

(isInRange _).curried
//Int => (Int => (Int => Boolean))
//**********
// Partial
//**********
def is5InRange = isInRange(_: Int, 5, _: Int)
//(Int, Int) => Boolean

is5InRange(0, 8)
//true

def between0and10 = isInRange(0, _: Int, 10)
//Int => Boolean

between0and10(5)
//true

between0and10(100)
//false

case class DemoState(number: Int)
type PFRule = PartialFunction[DemoState, Option[String]]

def numberRule(f: Int => Boolean, result: String): PFRule = {
  case DemoState(n) if f(n) => Option(result)
}

val GreaterThanFiveRule = numberRule(_ > 5, "Greater than five")
val LessThanFiveRule    = numberRule(_ < 5, "Less than five")
val EqualsFiveRule      = numberRule(_ == 5, "Equals five")

val NumberRules = GreaterThanFiveRule orElse LessThanFiveRule orElse EqualsFiveRule

NumberRules(5) // It will return "Equals five"
NumberRules(1) // It will return "Less than five"
NumberRules(7) // It will return "Greater than five"
