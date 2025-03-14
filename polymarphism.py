class shape:
  def aera(self):
     pass
class rectangle(shape):
  def_init_(self,length,width):
      self.length=length
      self.width=width
  def aera(self):
      return self.length*self.width
  class circle(shape):
  def_init_(self,radius):
      self.radius=radius
  def aera(self):
          return 3.14*self.radius*self.radius
  shape_rectangle=rectangle(5,3)
  shape_circle=circle(4)
          print("rectangle aera:",shape_rectangle.aera())
          print("circle aera:",shape_circle.aera())
