
object laba2_2 extends App {
  trait Main1
  {
    var obj = Array[Int]()
  }


  trait ToAppend extends Main1{
    def append(elem : Int): Unit = {
      //нахожу длину массива
      var lenList = 0
      for (i <- obj)
        lenList += 1
      //создаю новый массив, чтобы перенести эл-ты из исходного
      val tmp = new Array[Int](lenList)
      for (i <- 0 to lenList-1)
        tmp(i) = obj(i)
      //определяю новый размер исходного массива
      obj = new Array[Int](lenList + 1)
      for (i <- 0 to lenList-1)
        obj(i) = tmp(i)
      //добавляю элемент в конец массива
      obj(lenList) = elem
    }
  }

  trait ToRemove extends Main1
  {
    def remove(elem : Int): Unit =
    {
      //нахожу длину массива
      var lenList = 0
      for (i <- obj)
        lenList += 1
      //создаю новый массив, чтобы перенести эл-ты из исходного
      val tmp = new Array[Int](lenList)
      for (i <- 0 to lenList-1)
        tmp(i) = obj(i)
      //определяю новый размер исходного массива
      obj = new Array[Int](lenList-1)
      //заполняю исходный массива без удаляемого элемента
      var i = 0
      while (tmp(i) != elem){
        obj(i) = tmp(i)
        i+=1
      }
      while (i != lenList-1){
        obj(i) = tmp(i+1)
        i+=1
      }
    }
  }

  trait ToInsert extends Main1
  {
    def insert(elem:Int, index:Int):Unit =
    {
      //нахожу длину массива
      var lenList = 0
      for (i <- obj)
        lenList += 1
      //создаю новый массив, чтобы перенести эл-ты из исходного
      val tmp = new Array[Int](lenList)
      for (i <- 0 to lenList-1)
        tmp(i) = obj(i)
      //определяю новый размер исходного массива
      obj = new Array[Int](lenList+1)
      //заполняю исходный массив и в нужную позицию фиксирую нужный элемент
      var i = 0
      while (i != index){
        obj(i) = tmp(i)
        i+=1
      }
      obj(index) = elem
      while (i != lenList){
        obj(i+1) = tmp(i)
        i+=1
      }
    }
  }

  trait ToPrint extends Main1
  {
    def toprint: Unit =
    {
      for (item <- obj)
        println(item)
    }
  }
  class list extends ToAppend with ToInsert with ToRemove with ToPrint

  trait InsertionSort extends Main1
  {
    def insertion_sort: Unit =
    {
      //нахожу длину массива
      var lenList = 0
      for (i <- obj)
        lenList += 1
      var x = 0
      var j = 0
      var i = 1
      while (i != lenList){
        x = obj(i)
        j = i
        while (j > 0 && x < obj(j-1) == true) {
          obj(j) = obj(j-1)
          j-=1
        }
        obj(j) = x
        i+=1
      }
    }
  }

  trait BubbleSort extends Main1
  {
    def bubble_sort : Unit =
    {
      //нахожу длину массива
      var lenList = 0
      for (i <- obj)
        lenList += 1
      var i = 0
      var tmp = 0
      while (i != lenList)
      {
        var j = lenList-1
        while (j != i)
        {
          if (obj(j-1) > obj(j))
          {
            tmp = obj(j-1)
            obj(j-1) = obj(j)
            obj(j) = tmp
          }
          j-=1
        }
        i+=1
      }
    }
  }

  class ArraySort extends ToAppend with ToPrint with InsertionSort with BubbleSort

  trait value
  {
    var num : Double = 342
  }


  trait sqrt2 extends value
  {
    def sqrt2 : Unit = {
      num = Math.pow(num, 0.5)
    }
  }


  trait sqrt3 extends value
  {
    def sqrt3 : Unit = {
      num = Math.pow(num, 0.33)
    }
  }


  trait sqrt4 extends value
  {
    def sqrt4 : Unit = {
      num = Math.pow(num, 0.25)
    }
  }


  trait sqrt5 extends value
  {
    def sqrt5 : Unit = {
      num = Math.pow(num, 0.2)
    }
  }


  class Sqrt extends sqrt2 with sqrt3 with sqrt4 with sqrt5

  trait dosmt extends value
  {
    def print : Unit = println(num)
  }

  println("Задание 1")
  var list = new list
  list.append(3)
  list.append(2)
  list.append(4)
  list.append(7)
  list.insert(1,2)
  list.remove(3)
  list.toprint

  println("Задание 2")
  var arraySort = new ArraySort
  arraySort.append(3)
  arraySort.append(-2)
  arraySort.append(0)
  arraySort.append(5)
  arraySort.append(1)
  arraySort.append(9)
  arraySort.bubble_sort
  arraySort.toprint

  println("Задание 3")
  var number = new Sqrt with dosmt
  number.sqrt2
  number.print
}
