def readCommandArgs(
    args: List[String],
    argsSoFar: List[(String, List[String])]
  ): List[(String, List[String])] = {
    def isSwitch(s: String) = { s.length > 0 && s.charAt(0) == '-' }

    args match {
      case opt :: tail if isSwitch(opt) =>
        readCommandArgs(tail, (opt, List.empty) :: argsSoFar)
      case value :: tail =>
        if (argsSoFar.length == 0) {
          readCommandArgs(tail, ("", List(value)) :: Nil)
        } else {
          readCommandArgs(tail, (argsSoFar.head._1, value :: argsSoFar.head._2) :: argsSoFar.tail)
        }
      case Nil => argsSoFar.map { case (k, vs) => k -> vs.reverse }.reverse
    }
  }

readCommandArgs(List("--groups", "aa", "bb", "--rankType", "comment"), List.empty)
// return List(("--groups" -> List("aa", "bb")), ("--rankType" -> List("comment"))

readCommandArgs(List("a", "b", "c"), List.empty)
// return List(("" -> List("a", "b", "c"))

