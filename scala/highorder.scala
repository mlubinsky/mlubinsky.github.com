//https://github.com/nadimbahadoor/allaboutscala

println("Step 1: Review how to define function with curried parameter groups")
def totalCost(donutType: String)(quantity: Int)(discount: Double): Double = {
  println(s"Calculating total cost for $quantity $donutType with ${discount * 100}% discount")
  val totalCost = 2.50 * quantity
  totalCost - (totalCost * discount)
}

println("\nStep 2: How to define a higher order function which takes another function as parameter")
def totalCostWithDiscountFunctionParameter(donutType: String)(quantity: Int)(f: Double => Double): Double = {
  println(s"Calculating total cost for $quantity $donutType")
  val totalCost = 2.50 * quantity
  f(totalCost)
}

println("\nStep 3: How to call higher order function and pass an anonymous function as parameter")
  val totalCostOf5Donuts = totalCostWithDiscountFunctionParameter("Glazed Donut")(5){totalCost =>
  val discount = 2 // assume you fetch discount from database
  totalCost - discount
}
println(s"Total cost of 5 Glazed Donuts with anonymous discount function = $totalCostOf5Donuts")

println("\nStep 4: How to define and pass a function to a higher order function")
def applyDiscount(totalCost: Double): Double = {
  val discount = 2 // assume you fetch discount from database
  totalCost - discount
}

println(s"Total cost of 5 Glazed Donuts with discount function = ${totalCostWithDiscountFunctionParameter("Glazed Donut")(5)(applyDiscount(_))}")


println("Step 1: How to define a List with Tuple3 elements")
val listOrders = List(("Glazed Donut", 5, 2.50), ("Vanilla Donut", 10, 3.50))

println("\nStep 2: How to define a function to loop through each Tuple3 of the List and calculate total cost")
def placeOrder(orders: List[(String, Int, Double)])(exchangeRate: Double): Double = {
  var totalCost: Double = 0.0
  orders.foreach {order =>
    val costOfItem = order._2 * order._3 * exchangeRate
    println(s"Cost of ${order._2} ${order._1} = £$costOfItem")
    totalCost += costOfItem
  }
  totalCost
}

println("\nStep 3: How to call function with curried group parameter for List of Tuple3 elements")
println(s"Total cost of order = £${placeOrder(listOrders)(0.5)}")

println("\nStep 4: How to define a call-by-name function")
def placeOrderWithByNameParameter(orders: List[(String, Int, Double)])(exchangeRate: => Double): Double = {
  var totalCost: Double = 0.0
  orders.foreach {order =>
    val costOfItem = order._2 * order._3 * exchangeRate
    println(s"Cost of ${order._2} ${order._1} = £$costOfItem")
    totalCost += costOfItem
  }
  totalCost
}

println("\nStep 5: How to define a simple USD to GBP function")
val randomExchangeRate = new Random(10)
def usdToGbp: Double = {
  val rate = randomExchangeRate.nextDouble()
  println(s"Fetching USD to GBP exchange rate = $rate")
  rate
}

println("\nStep 6: How to call function with call-by-name parameter")
println(s"Total cost of order = £${placeOrderWithByNameParameter(listOrders)(usdToGbp)}")


println("Step 1: How to define a function with a callback parameter")
def printReport(sendEmailCallback: () => Unit) {
  println("Printing report ... started")
  // look up some data in database and create a report
  println("Printing report ... finished")
  sendEmailCallback()
}

println("\nStep 2: How to call a function which has a callback parameter")
printReport(() =>
println("Sending email ... finished")
)

println("\nStep 4: How to define a function Function with an Option callback")
def printReportWithOptionCallback(sendEmailCallback: Option[() => Unit] = None) {
  println("Printing report ... started")
  // look up some data in database and create a report
  println("Printing report ... finished")
  sendEmailCallback.map(callback => callback())
}

println("\nStep 5: How to call a function without providing its callback parameter")
printReportWithOptionCallback() // more elegant

println("\nStep 6: How to call a function with Option callback parameter")
printReportWithOptionCallback(Some(() =>
  println("Sending email wrapped in Some() ... finished")
))

