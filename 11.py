import datetime

now_date = datetime.datetime.now()
str(now_date)

print('[aria-label*="%s' % now_date.strftime("%B ") + '%d' % now_date.day + '"]')