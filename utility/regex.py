import re

def is_email(string):
	p = re.compile('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$')
	if p.match(string):
		return True
	else:	
		return False 