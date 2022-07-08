class RFID:
    def __init__(self):
        import RPi.GPIO as GPIO
        from mfrc522 import SimpleMFRC522
        self.reader = SimpleMFRC522()
    
    def Read(self):
        """Description:
            Requests MFRC522 to read a tapped card
        
        Args:
            n/a
        """
        print("\nPlace card to read")
        return(self.reader.read())

    def Write(self, newData:str): #To be created 
        """Description:
            Requests MFRC522 to write new data to a tapped card

        Args:
            newData (str): The new data to be written to the card

        Example:
            ```newData("Write this text")```
        """
        self.reader.write(newData)
        return()