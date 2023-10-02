import configparser
config=configparser.RawConfigParser()
path="E:\\software testing\\lectures\\pythonProject\\PRACTICE_PROJECT_1\\Configuration\\config.ini"
config.read(path)

class Readconfig:
    @staticmethod
    def Geturl():
        url=config.get('info', 'url')
        return url
