#假设你获取了用户输入的日期和时间如2015-1-21 9：01：30，以及一个时区信息如UTC+5：
#均是str,请编写一个函数将其转换为timestamp:

import re
from datetime import datatime,timezone,timedelta

