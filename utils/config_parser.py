import configparser
import os

class ConfigReader:
    _config = None
    
    @staticmethod
    def get_config(context):
        
        if ConfigReader._config is None:     
            env = context.config.userdata.get('env', 'dev')  # Default to 'dev' if not provided
        
            ConfigReader._config = configparser.ConfigParser()
            #get root path of the project
            root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            config_path = os.path.join(root_path, f'config\\{env}.ini')
            
            if not os.path.exists(config_path):
                raise FileNotFoundError(f"Config file not found: {config_path}")
            
            
            ConfigReader._config.read(config_path)
            print(f"✅ Running tests with {env.upper()} config")
            
        return ConfigReader._config
    
    @staticmethod
    def get_base_url(context):
        config = ConfigReader.get_config(context)
        return config.get('default', 'BASE_URL', fallback='https://www.saucedemo.com/')
    
    @staticmethod
    def get_browser(context):
        config = ConfigReader.get_config(context)
        return config.get('default', 'BROWSER', fallback='chrome')

    @staticmethod
    def is_headless(context):
        return ConfigReader.get_config(context)['default'].getboolean('HEADLESS', fallback=False)
    
    @staticmethod
    def get_implicit_wait(context):
        config = ConfigReader.get_config(context)
        return config.getint('default', 'IMPLICIT_WAIT', fallback=10)
    
    @staticmethod
    def get_explicit_wait(context):
        config = ConfigReader.get_config(context)
        return config.getint('default', 'EXPLICIT_WAIT', fallback=15)
    