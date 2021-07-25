import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\SKYNETT DRONES\\workspce_python\\Odoo_CRM_Automation\\Configuration\\config.ini")


class ReadConfig:

    @staticmethod
    def getapplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'userName')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
