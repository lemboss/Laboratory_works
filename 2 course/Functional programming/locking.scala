import scala.collection.mutable.ArrayBuffer
import scala.reflect.ClassManifestFactory.Any
import scala.util.Random

object lab2_2 extends App
{
  def randint(start: Int, finish: Int): ()=>Any = {
    val array = new ArrayBuffer[Int]
    var num:Int=0
    def inner(): Any =
    {
      if (array.length == finish)
        return null
      num = Random.between(start, finish+1)
      while (array.contains(num))
        num = Random.between(start, finish+1)

      array.append(num)
      num
    }
    inner
  }

  var z = randint(1, 10)
  var a=z()
  while (a!=null)
    {

      println(a)
      a=z()
    }



}
