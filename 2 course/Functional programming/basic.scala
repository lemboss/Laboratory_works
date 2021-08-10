import scala.collection.mutable.ArrayBuffer

object lab2 extends App {
  // number 1
  var List = Array(1, 1, 2, 3, 5, 8)

  def nth(k: Int, array: Array[Int]): Int = {
    // cycle 1
    var i = 0
    for (index <- array) {
      if (i == k)
        return index
      i += 1
    }
    return -1
  }

  println("Zadanie1Cycle")
  println(nth(2, List))

  // recursion 1
  def nth1(k: Int, array: Array[Int], i: Int = 0): Int = {
    if (i == k)
      return array(i)
    nth1(k: Int, array: Array[Int], i + 1)
  }

  println("Zadanie1recursion")
  println(nth1(2, List))


  // number 2
  def reverse(array: Array[Int]): Array[Int] = {
    // cycle 2
    val len = array.length - 1
    var new_array: Array[Int] = new Array[Int](len + 1)
    for (i <- 0 to len) {
      new_array(i) = (array(len - i))
    }
    new_array
  }

  println("Zadanie2Cycle")
  println(reverse(List).mkString(", "))

  // recursion 2
  def reverse1(array: Array[Int], i: Int = 0): Array[Int] = {
    var len = array.length - i - 1
    if (len <= i)
      return array
    var tmp = array(i)
    array(i) = array(len)
    array(len) = tmp
    reverse1(array, i = i + 1)
  }

  println("Zadanie2recursion")
  println(reverse1(List).mkString(", "))

  // number 3
  var list: Array[Char] = Array('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k')

  def slice(start: Int, end: Int, array: Array[Char]): Array[Char] = {
    var new_array = new Array[Char](end - start)
    var i = 0
    for (j <- start to end - 1) {
      new_array(i) = array(j)
      i += 1
    }
    new_array
  }

  // recursion 3
  def slice1(start: Int, end: Int, array: Array[Char], array1: ArrayBuffer[Char] = new ArrayBuffer[Char], i: Int = 0): ArrayBuffer[Char] = {
    var item = array(start + i)
    if (start + i == end)
      return array1
    array1.append(item)
    slice1(start, end, array, array1, i = i + 1)
  }

  println("Zadanie3Cycle")
  println(slice(3, 7, list).mkString(", "))

  println("Zadanie3Recursion")
  println(slice1(3, 7, list).mkString(", "))


  // cycle 4
  def range(start: Int, end: Int) = {
    for (num <- start to end) yield (num)
  }

  // recursion 4
  def range1(start: Int, end: Int, array: ArrayBuffer[Int] = new ArrayBuffer[Int](), i: Int = 0): ArrayBuffer[Int] = {
    if ((start + i) == end + 1)
      return array
    array += (start + i)
    range1(start, end, array, i = i + 1)
  }

  println("Zadanie4Cycle")
  println(range(4, 9))

  println("Zadanie4Recursion")
  println(range1(4, 9))

  // cycle 5
  def gcd(num1: Int, num2: Int): Int = {
    var i = num1
    while (true) {
      i -= 1
      if ((num1 % i == 0) && (num2 % i == 0))
        return i
    }
    i
  }

  // recursion 5
  def gcd1(num1: Int, num2: Int, i: Int = 0): Int = {
    if ((num1 % (num1 - i) == 0) && (num2 % (num1 - i) == 0))
      return i
    gcd1(num1: Int, num2: Int, i + 1)
  }

  println("Zadanie5Cycle")
  println(gcd(36, 63))

  println("Zadanie5Recursion")
  println(gcd(36, 63))


  // cycle 6
  def rotate(num: Int, array: Array[Int]) = {
    val len = array.length - 1
    var newarray = new Array[Int](len + 1)
    for (i <- num to len) {
      newarray(i - num) = array(i)
    }
    for (i <- 0 to num - 1) {
      newarray(i + len - num + 1) = array(i)
    }
    newarray
  }

  List = Array(1, 1, 2, 3, 5, 8)

  println("Zadanie6Cycle")
  println(rotate(2, List).mkString(", "))


  // recursion 6
  def rotate1(num: Int, array: Array[Int], array1: ArrayBuffer[Int] = new ArrayBuffer[Int], i: Int = 0, flag: Boolean = true): ArrayBuffer[Int] = {
    var flag1 = flag
    var index = i
    if (array1.length == array.length)
      return array1
    if ((num + i) >= (array.length)) {
      index = 0
      flag1 = false
    }
    if (flag1 == true)
      array1.append(array(num + i))
    else
      array1.append(array(index))
    rotate1(num, array, array1, i = i + 1)

  }

  println("Zadanie6Recursion")
  println(rotate1(2, List).mkString(", "))


  def f(x: Double) = x * x * x + 18 * x - 83

  def fi(x: Double) = x - f(x) / 66

  def msi(x: Double, e: Double = 0.0001): (Double, Double) = {
    var x0: Double = 0
    var tempX = x
    while (math.abs(tempX - x0) > e) {
      x0 = tempX
      tempX = fi(x0)
    }
    (tempX, f(tempX))
  }

  def msi1(x: Double, e: Double = 0.0001, x0: Double = 0): (Double, Double) = {
    var tempx0 = x
    var tempx = fi(tempx0)
    if (math.abs(tempx - tempx0) <= e)
      return (tempx, f(tempx))
    msi1(x = tempx, e)
  }

  println("Zadanie7Cycle")
  println(msi(3))

  println("Zadanie7Recursion")
  println(msi1(3))


  //на вход массив и элемент и индексыв которых этот элмент был
  def func(array: Array[Int], num: Int) = {
    for (i <- 0 to array.length - 1 if (array(i) == num)) yield (i)
  }
  println(func(Array(3,4,2,5,2,3,0,1,3), 3))
}