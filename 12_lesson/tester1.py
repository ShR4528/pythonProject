from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

print(config.sections())
print(config['EMAIL']['pass'])

config.add_section('NEWLOGIN')
config.set('NEWLOGIN', 'login', 'new_login')
config.set('NEWLOGIN', 'pass', 'new_pass')

with open('config.ini', 'w') as config_file:
    config.write(config_file)


#config['DEFAULT'] = {
#    'login': 'mylogin',
#    'pass': 'mypass'
#}
#config['DATABASE'] = {
#    'host': 'localhost',
#    'login': 'root',
#    'pass': '12345'
#}
#config['EMAIL'] = {
#    'login': 'roman@example',
#    'pass': '123456'
#}
#with open('config.ini', 'w') as config_file:
#    config.write(config_file)

