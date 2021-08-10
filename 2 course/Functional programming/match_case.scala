
object laba2_2 extends App {
  var y = 0
  for (i <- 0 to 4)
  {
    i match
    {
      case 0 => y=2
      case 1 => y=0
      case 2 => y=0
      case 3 => y=1
    }
  }

  class Numbers(num:Int)
  {
    val Num = num
    def fib(n : Int = Num):Int =
    {
      n match
      {
        case 1 => 1
        case 2 => 1
        case _ => fib(n-1)+fib(n-2)
      }
    }
  }

  val number = new Numbers(13)
  number.fib()

}
