from lawyer.parsers import singlet, singlets

a = singlets('W', helptext='this is some W grp', auto_help=True, help_notations=('--help', '-h'), application_name='Wapp', application_description='some desc here')
a.__singlet__('create', '--create', '-c', base=True, capture='single', helptext='create something with this', required=False, default='23')
a.__singlet__('create34', '--create34', '-c34', base=False, capture='single', helptext='create something with this', required=False, default='23')
a.__singlets__('W2', helptext='this is W2 group that is under W grp', auto_help=True, help_notations=('--help', '-h'))

a.__register_singlet_for_this_singlets_object__('W2', 'create2', '--create2', '-c2', base=True, capture='single', helptext='this is create2', required=False, default='23')
a.__register_singlets_for_this_singlets_object__('W2', 'W3', 'this is W3', auto_help=True, help_notations=('--help', '-h'))

# print(a.__object__('W3').helptext)
print(a.__parse__('create', 'create34', ('W2', 'create2')))