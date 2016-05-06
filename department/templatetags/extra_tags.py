from django import template
register = template.Library()

@register.filter(addstr='addstr')
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)


@register.filter(vallue='get_attendence')
def get_attendence(employee, day):
	try:			
		return getattr(employee, day)
	except:
		return '-'


@register.filter(save_attendence='save_attendence')
def save_attendence(arg1, arg2):
    print("===============saving attendence for  for the day ===================")
    return str(arg1) + str(arg2)
