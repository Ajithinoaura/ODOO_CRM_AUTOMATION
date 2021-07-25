import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger('sgd_svrg')
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        fh = logging.FileHandler('C:\\Users\\SKYNETT DRONES\\workspce_python\\Odoo_CRM_Automation\\Logs\\experiments.log')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
