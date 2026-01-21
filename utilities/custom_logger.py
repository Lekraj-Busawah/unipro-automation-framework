import logging

class LogGen:
    @staticmethod
    def loggen():
        # Define specific logger name to isolate from Selenium internal logs
        logger = logging.getLogger("Unipro_Automation")
        
        # Only add handlers if they haven't been added yet
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            
            # File Handler
            file_handler = logging.FileHandler("automation.log")
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', 
                                          datefmt='%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            
        return logger