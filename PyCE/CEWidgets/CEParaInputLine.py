from http.client import UNSUPPORTED_MEDIA_TYPE
from typing import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from Base.UnitTrans import *

class CEParaInputLine(QFrame):
    __i1 = 1
    __i2 = 2
    __i3 = 3
    UnitType:Unit
    TargetUnit:None
    LastData:Any = ""
    def __init__(this, parent:QWidget = None):
        super().__init__(parent)
        this.setParent(parent)
        this.setObjectName("CEParaInputLine")
        this.TextLabel = QLabel(this)
        this.InputEdit = QLineEdit(this)
        this.UnitBox = QComboBox(this)
        this.TextLabel.setObjectName("TextLabel")
        this.InputEdit.setObjectName("InputEdit")
        this.UnitBox.setObjectName("UnitBox")
        this.UnitBox.currentIndexChanged.connect(this.unitTrans)
        
    def setUnitType(this, Type:Unit):
        this.UnitType = Type
    
    def unitType(this):
        return this.UnitType

    def setTargetUnit(this, unit):
        this.TargetUnit = unit

    def targetUnit(this):
        return this.TargetUnit

    def getTargetValue(this):
        return UnitTrans.trans(this.UnitType, float(this.value()), this.currentData(), this.TargetUnit)
        
    def setText(this, text:str):
        this.TextLabel.setText(text)

    def setTextStyleSheet(this, style:str):
        this.TextLabel.setStyleSheet(style)
    
    def setInputEditStyleSheet(this, style:str):
        this.InputEdit.setStyleSheet(style)

    def setUnitBoxStyleSheet(this, style:str):
        this.UnitBox.setStyleSheet(style)

    def addItems(this, unit:list):
        this.UnitBox.addItems(unit)

    def addItem(this, text:str, data:Any):
        this.UnitBox.addItem(text, data)

    def setInitIndex(this, index:int):
        this.UnitBox.setCurrentIndex(index)
        this.LastData = this.UnitBox.currentData()

    def setCurrentIndex(this, index:int):
        this.UnitBox.setCurrentIndex(index)
    
    def setValue(this, text:str):
        this.InputEdit.setText(text)

    def value(this)->str:
        return this.InputEdit.text()

    def setInterval(this, i1:int, i2:int, i3:int):
        this.__i1 = i1
        this.__i2 = i2
        this.__i3 = i3
        this.resizeEvent()

    def resizeEvent(this, event:QResizeEvent = None):
        this.TextLabel.setGeometry(QRect(0, 0, this.width()*(this.__i1/(this.__i1+this.__i2+this.__i3)), this.height()))
        this.InputEdit.setGeometry(QRect(this.width()*(this.__i1/(this.__i1+this.__i2+this.__i3))+1, 0, this.width()*(this.__i2/(this.__i1+this.__i2+this.__i3)), this.height()))
        this.UnitBox.setGeometry(QRect(this.width()*((this.__i1+this.__i2)/(this.__i1+this.__i2+this.__i3))+1, 0, this.width()*(this.__i3/(this.__i1+this.__i2+this.__i3)), this.height()))

    def text(this):
        return this.TextLabel.text()

    def currentIndex(this):
        return this.UnitBox.currentIndex()

    def currentData(this):
        return this.UnitBox.currentData()

    def unitTrans(this):
        if (this.InputEdit.text() != "") and (this.UnitType != Unit.Dimensionless):
            this.InputEdit.setText(str(UnitTrans.trans(this.UnitType,float(this.InputEdit.text()), this.LastData, this.UnitBox.currentData())))
            this.LastData=this.UnitBox.currentData()

    