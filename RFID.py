def Read():
    ### Import Libraries ###
    import RPi.GPIO as GPIO
    from mfrc522 import SimpleMFRC522

    ### Reader Setup ###
    reader = SimpleMFRC522()

    ### Read & Return ###
    return(reader.read())

def Write(newData): #To be created 
    ### Import Libraries ###
    import RPi.GPIO as GPIO
    from mfrc522 import SimpleMFRC522

    ### Reader Setup ###
    reader = SimpleMFRC522()
    
    ### Write & Return ###
    reader.write(newData)
    return()

