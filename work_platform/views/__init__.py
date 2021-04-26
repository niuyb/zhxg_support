from .views import *
from ._wechat import (wechat_group_message_list_api, 
        Wechat, WechatResult, wechat_test, wechat_result_test,
        wechat_group_list, wechat_group_members_api, push_wechat_group_message)
from ._ding_talk import (index, get_modules, login, index2)
from ._customer import (customer_list, customer_list_api, 
        search_customer)

from.task import (task,task_oppapi,task_modifyapi,task_api,add_task_api)
from.task import (person_task,team_department_api,team_pei_api)


from.work_count import (work_count,work_count_api,work_depart_api,work_per_api,count_detail_api)