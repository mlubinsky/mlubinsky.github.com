
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
