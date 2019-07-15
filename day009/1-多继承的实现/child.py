from father import Father
from mother import Mother

class Child(Mother,Father):
    def __init__(self,money,facevalue):
        #写法,多继承
        Father.__init__(self,money)
        Mother.__init__(self,facevalue)
