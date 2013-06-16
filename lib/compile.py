from driveler import Driveler

d = Driveler()
d.site_title = 'wabbo'
d.include_dir = 'includes/'
d.css_file = '/css/style.css'


d.copy_folder('css/')
d.convert_folder('', bl=['readme'])
d.convert_folder('blov/')
d.convert_folder('notes/', wl=['linalg'])
