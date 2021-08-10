sealed abstract class Figure

case class Circle(radius: Double) extends Figure

case class Square(side: Double) extends Figure

case class Rectangle(height: Double, width: Double) extends Figure

object laba2_2 extends App
{
  def ToCalculate(figure: Figure): String =
  {
    figure match
    {
      case Circle(radius) => s"Круг\nПлощадь: ${Math.PI*radius*radius}\nПериметр: ${2*Math.PI*radius}\n"
      case Square(side) => s"Квадрат\nПлощадь: ${side*side}\nПериметр: ${4*side}\n"
      case Rectangle(height, width) => s"Прямоугольник\nПлощадь: ${height*width}\nПериметр: ${(height+width)*2}\n"
    }
  }
  val circle = Circle(4.3)
  val square = Square(3)
  val rectangle = Rectangle(4,5)
  println(ToCalculate(square))
  println(ToCalculate(circle))
  println(ToCalculate(rectangle))
}
