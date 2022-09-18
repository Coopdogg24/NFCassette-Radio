from Software import MongoDB

class RFID:
    def __init__(self):
        import RPi.GPIO as GPIO
        from mfrc522 import SimpleMFRC522
        from mfrc522 import MFRC522
        from Software import MongoDB
        self.reader = SimpleMFRC522()
        self.backupReader = MFRC522()
        self.MongoDB = MongoDB()
    
    def Read(self):
        """Description:
            Requests MFRC522 to read a tapped card
        
        Args:
            n/a
        """
        print("\nPlace card to read")
        cardData = self.reader.read()
        if cardData[1] == "":
            status, _ = self.backupReader.MFRC522_Request(self.backupReader.PICC_REQIDL)
            status, backData = self.backupReader.MFRC522_Anticoll()
            buf = self.backupReader.MFRC522_Read(0)
            self.backupReader.MFRC522_Request(self.backupReader.PICC_HALT)
            if buf:
                return(cardData[0], self.MongoDB.getTagData((':'.join([hex(x) for x in buf]))))
        #Note: Needs to return [ID, Data]
        return(cardData)

    def Write(self, newData:str):
        """Description:
            Requests MFRC522 to write new data to a tapped card

        Args:
            newData (str): The new data to be written to the card

        Example:
            ```newData("Write this text")```
        """
        print("\nPlace card to write '{}'".format(newData))       

        cardData = self.reader.read()
        if cardData[1] == "":
            status, _ = self.backupReader.MFRC522_Request(self.backupReader.PICC_REQIDL)
            status, backData = self.backupReader.MFRC522_Anticoll()
            buf = self.backupReader.MFRC522_Read(0)
            self.backupReader.MFRC522_Request(self.backupReader.PICC_HALT)
            if buf:
                cardHex = (':'.join([hex(x) for x in buf]))
                if self.MongoDB.checkIfExists(cardHex):
                    self.MongoDB.replaceTagData(cardHex, newData)
                else:
                    self.MongoDB.writeNewTag(cardHex, newData)
                return()
        self.reader.write(newData)
        return()