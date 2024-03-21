import inspect
import logging


class loggen:

     @staticmethod
     def log():
         name = inspect.stack()[1][3]
         logger = logging.getLogger(name)
         file = logging.FileHandler("E:\\software testing\\lectures\\pythonProject\\PRACTICE_PROJECT_1\\Logs\\automation_logs.log")
         format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
         file.setFormatter(format)
         logger.addHandler(file)
         logger.setLevel(logging.DEBUG)
         return logger




