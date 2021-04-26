import json
import logging
import traceback

from django.db.models import Q
from django.http import JsonResponse
import pymysql

from customer.models import SurverySubject, CrmIndustryL2, Questionaire, Answer, Question, Account
from customer.service.questionnaireService import encryption, deciphering, industry_id_mapping, sync_subject
from public.utils import parse_kwargs_for_pymysql
from django.conf import settings

logger = logging.getLogger("customer")

#生成uuid
def get_uuid(request):
    if request.method == "GET":
        result = {"code": 200, "msg": "", "data": None}
        account_id = request.GET.get("account_id")
        if account_id:
            queuuid = encryption(account_id)
            result["data"] = queuuid
            print(result)
            return JsonResponse(result)
        result["code"] = 400
        result["msg"] = "account Parameter missing"
        return JsonResponse()



#存储调研表数据
# def save_questionnalre(request):
#     if request.method == "POST":
#
#         result = {"code": 200, "msg":"success", "data":None}
#         if request.body:
#             req_data = json.loads(request.body, encoding="utf-8")
#         else:
#             req_data = {}
#         try:
#             queuuid = req_data.get("queuuid")
#             data = req_data.get("data")
#             name = req_data.get("name")
#
#             account_id = deciphering(queuuid)
#
#             account = Account.objects.filter(id=account_id).first()
#             industry_id = account.dbcselect9
#
#
#
#             # #存储 调研表记录
#             questionaire = Questionaire.objects.filter(id=queuuid)
#             if questionaire:
#                 result["msg"] = '已存在 不能在创建'
#                 result["code"] = 201
#                 return JsonResponse(result)
#
#             questionaire = Questionaire()
#             questionaire.id = queuuid
#             questionaire.name = name
#             questionaire.account_id = account_id
#             questionaire.industry_id = industry_id
#             questionaire.save()
#
#             # data = {
#             #   "1001" : ""
#             #   "1002" : False
#             # }
#             for catalog_id, content in data.items():
#         #         answer = Answer()
#         #         #调研表id
#         #         answer.questionaire_id = queuuid
#         #         #主题id
#         #         answer.catalog_id = catalog_id
#         #         #使用主题id 查询 他的类型
#         #         srs = SurverySubject.objects.filter(catalog_id=str(catalog_id)).first()
#         #         # question = Question.objects.filter(id=srs.question_id).first()
#         #
#         #         #填空题
#         #         if srs.type == '1':
#         #             answer.content = content
#         #         #多选题
#         #         elif srs.type == '2':
#         #             pass
#         #         #多选题的其他
#         #         elif srs.type == '3':
#         #             answer.content = content
#         #         answer.question_id = srs.question_id
#         #         answer.save()
#         except Exception as e:
#             print(traceback.print_exc())
#             result["msg"] = str(e)
#             result["code"] = 500
#         return JsonResponse(result)


#存储调研表数据
def save_questionnalre(request):
    if request.method == "POST":

        result = {"code": 200, "msg":"success", "data":None}
        if request.body:
            req_data = json.loads(request.body, encoding="utf-8")
        else:
            req_data = {}
        try:
            queuuid = req_data.get("queuuid")
            data = req_data.get("data")
            name = req_data.get("name")


            account_id = deciphering(queuuid)


            #获取 客户 行业
            account = Account.objects.filter(id=account_id).first()
            industry_id_cc = account.dbcselect9
            # 转行业id
            industry_id = industry_id_mapping.get(industry_id_cc, 0)

            #存储的时候也 同步在存储
            sync_subject(industry_id)

            # #存储 调研表记录
            questionaire = Questionaire.objects.filter(id=queuuid)
            if questionaire:
                result["msg"] = '已存在 不能在创建'
                result["code"] = 201
                return JsonResponse(result)
            questionaire = Questionaire()
            questionaire.id = queuuid
            ci = CrmIndustryL2.objects.filter(id=industry_id_cc).first()
            name = ci.name if ci else ""
            questionaire.name = name + "行业舆情监测调研表"
            questionaire.account_id = account_id
            # 存放的是 cc 里的
            questionaire.industry_id = industry_id_cc
            questionaire.save()

            # data = {
            #   "1001" : ""
            #   "1002" : False
            # }
            for subject_id, content in data.items():
                answer = Answer()
                #调研表id
                answer.questionaire_id = queuuid
                #主题id
                answer.subject_id = subject_id

                #使用主题id 查询 他的类型
                srs = SurverySubject.objects.filter(catalog_id=int(subject_id)).first()
                # question = Question.objects.filter(id=srs.question_id).first()
                answer.subject_name = srs.catalogname
                answer.account_id = account_id
                answer.region_tag_type = srs.region_tag_type
                #填空题
                if srs.type == '1':
                    if srs.question_id == 1:
                        answer.customre_abbreviation = content
                    answer.content = content

                #多选题
                elif srs.type == '2':
                    pass
                #多选题的其他
                elif srs.type == '3':
                    answer.content = content
                answer.question_id = srs.question_id
                answer.industry_id = industry_id
                answer.save()
        except Exception as e:
            print(traceback.print_exc())
            result["msg"] = str(e)
            result["code"] = 201
        return JsonResponse(result)

#获取调研表数据

def get_questionnalre(request):
    if request.method == 'GET':
        result = {"code": 200, "msg":"", "data":None}

        queuuid = request.GET.get("queuuid")

        try:
            # 用 uuid 获取 调研表记录数据
            questionaire = Questionaire.objects.filter(id=queuuid).first()

            #如果有 获取
            if questionaire:
                #6
                industry_id_acc = questionaire.industry_id
            else:
                try:
                    account_id = deciphering(queuuid)
                except Exception as e:
                    result["code"] = 201
                    result["msg"] = "url地址错误"
                    return JsonResponse(result)
                account = Account.objects.filter(id=account_id).first()
                #6
                industry_id_acc = account.dbcselect9


            #同步 数据
            #8
            print(industry_id_acc)
            #这里是  不同行业id 转
            if int(industry_id_acc) in industry_id_mapping:
                industry_id = industry_id_mapping.get(int(industry_id_acc), 0)

            else:
                result["msg"] = "没有客户行业对应的模板"
                result["code"] = 201
                return JsonResponse(result)


            #同步数据
            sql = "select id, subject_name, describtion, is_must, region_tag_type from system_recommend_subject where industry_id= '{}' and (describtion != null or describtion != '' or catalog_id != 0)".format(
                industry_id)

            if settings.MODE == 'develop' or settings.MODE == 'beta':
                kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
            else:
                kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
            # kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
            conn = pymysql.connect(**kws)
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            oppinfo = cursor.fetchall()

            SurverySubject.objects.filter(industry_id=industry_id).delete()

            lst = []
            for o in oppinfo:
                ss = SurverySubject()
                ss.catalog_id = o["id"]
                ss.type = "2"
                ss.catalogname = o["subject_name"]
                ss.tip = o["describtion"]
                ss.question_id = 2
                ss.industry_id = industry_id
                ss.is_default = o["is_must"]
                ss.region_tag_type = o["region_tag_type"]
                # ss.save()
                lst.append(ss)

            SurverySubject.objects.bulk_create(lst)

            #同步 答案id
            answers = Answer.objects.filter(questionaire_id=queuuid)
            answers_list = []
            for answer in answers:
                for opp in oppinfo:
                    if answer.subject_name == opp["subject_name"] or answer.subject_id == opp["id"]:
                        answer.subject_name = opp["subject_name"]
                        answer.subject_id = opp["id"]
                        answer.region_tag_type = opp["region_tag_type"]
                        answers_list.append(answer)
                        break

            Answer.objects.bulk_update(answers, ["subject_name", "subject_id", "region_tag_type"])


            questions = Question.objects.all()
            data = []
            for question in questions:
                dict1 = {}
                dict1["describe"] = question.describe
                dict1["necessary"] = True if question.is_must == 1 else False
                question_id = question.id
                #专题 获取 行业 专题 和  type3
                srss = SurverySubject.objects.filter(Q(question_id=question_id) , Q(Q(industry_id=industry_id ) | Q(type='3'))).order_by('catalog_id')
                # print(srss)
                # for index,srs in enumerate(list(srss)):
                #     if srs.catalog_id == 6666:
                #         srss.append(srs)
                #         srss.remove(srs)
                #
                # print(srss)

                # 其他题
                type2_srss = SurverySubject.objects.exclude(type='2').filter(question_id=question_id)

                questions_list = []
                for type2_srs in type2_srss:
                    dict2 = {}
                    if questionaire:
                        answer = Answer.objects.filter(questionaire_id=questionaire.id, subject_id=type2_srs.catalog_id,
                                                       question_id=question_id).first()
                    else:
                        answer = None
                    dict2["key"] = type2_srs.catalog_id
                    dict2["type"] = type2_srs.type
                    dict2["name"] = ""
                    dict2["tip"] = type2_srs.tip
                    if answer:
                        dict2["answer"] = answer.content
                    else:
                        dict2["answer"] = ""
                    # if answer:
                    #     if question_id == 1:
                    #         dict2["listType"] = answer.content.split(',')
                    #     dict2["answer"] = answer.content
                    # else:
                    #     if question_id == 1:
                    #         dict2["listType"] = ["","",""]
                    #     dict2["answer"] = ""

                    if type2_srs.type == "3":
                        break
                    questions_list.append(dict2)

                for srs in srss:
                    dict2 = {}
                    if questionaire:
                        answer = Answer.objects.filter(questionaire_id=questionaire.id, subject_id=srs.catalog_id,
                                                   question_id=question_id).first()
                    else:
                        answer = None
                    dict2["key"] = srs.catalog_id
                    dict2["type"] = srs.type
                    dict2["name"] = srs.catalogname
                    dict2["tip"] = srs.tip

                    if questionaire:
                        dict2["answer"] = True if answer else False
                    else:
                        dict2["answer"] = True if srs.is_default == 1 else False


                    if srs.type == '3':
                        dict2["answerSup"] = ''
                        if answer:
                            dict2["answer"] = True
                            dict2["answerSup"] = answer.content
                        else:
                            dict2["answer"] = False
                    questions_list.append(dict2)
                #第二道题（其他）专题调换顺序到最后
                if question.id == 2:
                    for index, srs in enumerate(questions_list):
                        if srs.get('key') == 6666:
                            questions_list.append(questions_list[index])
                            questions_list.remove(questions_list[index])
                            break

                dict1["questions"] = questions_list
                data.append(dict1)


        except Exception as e:
            print(traceback.print_exc())
            result["msg"] = "获取数据失败"
            result["code"] = 201
            return JsonResponse(result)


        result["data"] = data
        industry = CrmIndustryL2.objects.filter(id=industry_id_acc).first()
        result["industry"] = industry.name
        return JsonResponse(result)



