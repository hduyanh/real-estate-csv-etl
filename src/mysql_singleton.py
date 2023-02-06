import mysql.connector
import sys
sys.path.append(r'D:\Git\real-estate-csv-etl')
from config import logger

# manage when the instance needs to be created
class Singeleton_DB:
    # variable associated with the class, keeps track if the instance has been created yet or not and instance itself
    # Equals to None mean, when program first start running the instance has not yet been created
    __instance = None 

    @staticmethod
    def getInstance():
    # this method associated with the singleton class, not associated with particular instance of singleton class, particular object
    # it is gonna check do we need the instance, if yes we create it.
    # return the instance itself, does not matter if need to be created or not
        if Singeleton_DB.__instance == None: # if None the we need to create the singleton object
            Singeleton_DB() # instantiate the singleton object 
        return Singeleton_DB.__instance # return something that is not None
    
    # init method to set instance it self the instance class variable
    # called when we created a singleton object
    # also called constructor
    def __init__(self): #given a reference to the acttuan singleton object itself that is being created when we call Singleton()
        if Singeleton_DB.__instance != None:
            raise Exception("Singleton exits already!")
        else:
            Singeleton_DB.__instance = mysql.connector.connect( host='localhost', user='root', password='123456')

    def script_executer(scripts):
        cursor = Singeleton_DB.__instance.cursor()
        for script in scripts:
            cursor.execute(script)
        Singeleton_DB.__instance.commit()
