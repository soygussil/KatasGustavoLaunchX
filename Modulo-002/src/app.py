from datetime import *
from dateutil.relativedelta import * 
now = datetime.now()
print(now)

noew = now + relativedelta(months=1, weeks=1, hour=10)
print (now)
