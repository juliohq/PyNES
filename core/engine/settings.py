import configparser, os

PATH = 'config.cfg'
skip_file = False

config = configparser.ConfigParser()

if os.path.isfile(PATH) and not skip_file:
    config.read_file(open('config.cfg'))
else:
    config.read_dict({
        'main': {
            'debug': True
        },
        'graphics': {
            'hwaccel': True
        }
    })