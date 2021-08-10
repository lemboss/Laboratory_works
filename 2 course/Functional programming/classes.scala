abstract class Animal {
  println("появилось животное")
  def sayHello() : Unit ={
    println("Привет, я животное")
  }
}
class Mammal(name: String, age : Int) extends Animal {
  println("Я млекопитнулся")
  var Name : String = name
  var Age : Int = age
  override def sayHello() : Unit = {
    println("Привет! Я млекопитающее")
  }
  def feedMilk() : Unit = println("Накормила")
  def upAge(): Unit = {
    Age += 1
    println("Возраст увеличили, теперь он равен " + Age)
  }
}

class Horse(name:String, age:Int, breed : String = "", speed: Int = 0) extends Mammal(name, age) {
  println("игогого")
  var Breed: String = breed
  var Speed: Int = speed
  override def sayHello(): Unit = {
    println("Привет! Я лошадь, меня зовут " + Name + ", Мне " + Age + " лет.")
  }

}

class Dog(name:String, age:Int, breed : String = "", power: Int = 0) extends Mammal(name, age){
  println("тяв пес родился")
  var Breed: String = breed
  var Power: Int = power
  override def sayHello(): Unit = {
    println("Привет! Я пес, меня зовут " + Name + ", Мне " + Age + " лет.")
  }
  def doGav() : Unit = println("гав гав")
  def letPaw() : Unit = println("дал лапу")
}

class Fish(name: String, age : Int) extends Animal {
  println("вылупился из икры")
  override def sayHello(): Unit = {
    println("Привет! Я рыба")
  }
}
class Insect(name: String, age : Int) extends Animal {
  override def sayHello(): Unit = {
    println("Привет! Я насекомое")
  }
}

class Spider(name: String, age : Int, anger: Int = 0, color : String = "", flufinness : Boolean = false, poison : Boolean = false) extends Insect(name, age) {
  println("родился паук")
  var Anger: Int = anger
  var Color: String = color
  var Flufinness: Boolean = flufinness
  var Poison : Boolean = poison
  if (Flufinness == true && Color.length > 2)
    Poison  = true

  override def sayHello(): Unit = {
    println("Привет! Я павук")
  }
}

class Croc(name: String, age : Int = 0, length: Int = 0, grenness: Int = 0) extends Animal{
  println("Я крокодился")
  var Name : String = name
  var Age : Int = age
  var Length : Int = length
  var Grenness : Int = grenness

  override def sayHello() : Unit = {
    println("Привет! Я крокодил")
  }
  def goSleep() : Unit = println("Сплю с открытой пастью на солнышке")

}
object laba2_2 extends App {
  var dog1 = new Dog("Шарик", 18)
  var croc = new Croc("Гена")
}
