from colorama import Fore,Style
import os
import sys
from time import sleep
from services.quary_service import QuaryService

__quary_service = QuaryService()

while True:
    os.system("cls")
    print(Fore.LIGHTGREEN_EX,"\n\t=======================")
    print(Fore.LIGHTGREEN_EX,"\n\t上海生活垃圾分类查询")
    print(Fore.LIGHTGREEN_EX,"\n\t=======================")
    result_list = __quary_service.quary_list()
    for index in range(len(result_list)):
        print(Fore.LIGHTBLUE_EX,"\n\t%d.%s" % (index + 1, result_list[index][1]))
    #print(Fore.LIGHTBLUE_EX,"\n\tm.分类管理")
    print(Fore.LIGHTRED_EX,"\n\texit.退出")
    print(Style.RESET_ALL)
    opt = input("\n\t选择指令查询详情或输入查询的垃圾名称：")
    if opt.isdigit():
        try:
            page=1
            while True:
                os.system("cls")
                print(Fore.LIGHTBLUE_EX,"\n\t%s是指：" % result_list[int(opt) - 1][1])
                print(Fore.LIGHTRED_EX,"\n\t%s" % (result_list[int(opt) - 1][2]))
                print(Fore.LIGHTBLUE_EX,"\n\t%s投放要求：" % result_list[int(opt) - 1][1])
                result_desc = __quary_service.quary_desc(result_list[int(opt) - 1][0])
                for index in range(len(result_desc)):
                    print(Fore.LIGHTRED_EX,"\n\t· %s"%result_desc[index][0])
                print(Fore.LIGHTBLUE_EX, "\n\t%s清单：" % result_list[int(opt) - 1][1])
                result_search = __quary_service.search_list(result_list[int(opt) - 1][1], page)
                for index in range(len(result_search)):
                    print(Fore.LIGHTRED_EX,"\n\t%s\t%s" % (index + 1, result_search[index][1]))
                count = __quary_service.search_count(result_list[int(opt) - 1][0])
                print(Fore.LIGHTGREEN_EX, "\n\t%d\%d" % (page, count))
                print(Fore.LIGHTGREEN_EX,"\n\t------------------------------------------")
                print(Fore.LIGHTRED_EX, "\n\tprev.上一页\t\tnext.下一页")
                print(Fore.LIGHTRED_EX,"\n\tb.返回上一层\t\t\texit.退出")
                print(Style.RESET_ALL)
                opt_page = input("\n\t请输入操作指令：")
                if opt_page == "prev" and page > 1:
                    page -= 1
                elif opt_page == "next" and page < count:
                    page += 1
                if opt_page.lower() == "b":
                    break
                elif opt_page.lower() == "exit":
                    sys.exit()
        except Exception as e:
            print(e)
            print(Fore.LIGHTRED_EX,"\n\t输入的%s指令有误,请重新输入"%opt)
            print(Style.RESET_ALL)
            sleep(3)
    elif opt.lower() == "exit":
        sys.exit()
    else:
        while True:
            os.system("cls")
            result_list = __quary_service.quary_sort(opt)
            if result_list:
                print(Fore.LIGHTGREEN_EX, "\n\t%s\t%s\t%s" % ("编号","名称","分类"))
                for one in range(len(result_list)):
                    print(Fore.LIGHTBLUE_EX,"\n\t%s\t%s\t%s" % (one + 1, result_list[one][0], result_list[one][1]))
                print(Fore.LIGHTGREEN_EX,"\n\t------------------------------------------")
                print(Fore.LIGHTRED_EX, "\n\tb.返回上一层")
                print(Fore.LIGHTRED_EX, "\n\texit.退出")
                print(Style.RESET_ALL)
                opt = input("\n\t选择指令查询详情或输入查询的垃圾名称：")
                if opt.lower() == "b":
                    break
                elif opt.lower() == "exit":
                    sys.exit()
                else:
                    continue
            else:
                print(Fore.LIGHTRED_EX, "\n\t抱歉，无法查询到%s的分类信息（3s后自动返回上一层）" % opt)
                print(Style.RESET_ALL)
                sleep(3)
                break