from abc import ABC, abstractmethod

class Presentation:
    def __init__(self,title,author,createdTime,slides ):
        self.title = title
        self.author = author
        self.createdTime = createdTime
        self.slides = slides 
    
    def addSlide(self,slide):
        self.slides.append(slide)

    def removeSlide(self,slide):
        self.slides.remove(slide)
        
    def displaySlides(self):
        for slide in self.slides:
            slide.displayElements()
            

class Element(ABC):
    def __init__(self,positionX,positionY,size,color):
        self.positionX = positionX
        self.positionY = positionY
        self.size = size 
        self.color = color
       
    @abstractmethod
    def display(self):
        pass
    
class Text(Element):
    def __init__(self,positionX,positionY,size,color,textContent):
        super (Text, self).__init__(positionX, positionY, size, color) 
        self.textContent = textContent

    def display(self):
        print(f"Text: {self.textContent}")
        print(f"Position: ({self.positionX}, {self.positionY})")
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")
            
#we can add any type like img or any type of data 
class Slide:
    def __init__(self,title,ListofElments):
        self.title = title
        self.ListofElments = ListofElments 
    def addElement(self,element):
        self.ListofElments.append(element) 

    def removeElement(self,element): 
        self.ListofElments.remove(element) 
        
    def displayElements(self):
        for element in self.ListofElments: 
            element.display()
            
if __name__ == "__main__":
    presentation = Presentation("My Presentation", "Nour", "02-08-2023", [])
    
    slide1 = Slide("Introduction", [])
    text1 = Text(10, 20, 12, "black", "Hello World!")
    slide1.addElement(text1) 
    presentation.addSlide(slide1)
    presentation.displaySlides()
