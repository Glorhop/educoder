import  sys,os;from typing  import   List,  Dict
def  add_numbers(  a:int  ,  b:int  )->int:return a+b
class   Person:
 def   __init__(   self  ,  name:str  ,  age:int  ):self.name=name;self.age=age
 def  greet(  self  )  ->  None:print(  f"Hello, {  self.name  }!"  )
def  filter_data(  data:List[  int  ],  threshold:int  =0  )->List[  int  ]:
 return [  x  for x in  data  if  x>  threshold  ]
def  main(  )->None:
 data=  [  1,  2,  3,  4,  5  ]
 filtered=filter_data(  data  ,  3  )
 person=Person(  "Alice"  ,  30  )
 person.greet(  )
 print(  f"Sum: {  add_numbers(  3  ,  5  )  }"  )
 print(  f"Filtered: {  filtered  }"  )
if  __name__  ==  "__main__"  :main(  )