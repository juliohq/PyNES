import configparser, os

PATH = 'config.cfg'
DEFAULTS = {
    'main': {
        'debug': True,
        'interpreter': False,
    },
        'graphics': {
            'hwaccel': True,
    }
}
skip_file = False

config = configparser.ConfigParser()

if os.path.isfile(PATH) and not skip_file:
    config.read_file(open('config.cfg'))
else:
    config.read_dict(DEFAULTS)