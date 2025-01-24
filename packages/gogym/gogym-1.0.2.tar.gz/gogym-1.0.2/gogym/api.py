# api.py文件可以调用本项目的任何包
# 用户也只允许调用api.py的包
from multiprocessing import Process

from gogym.control import get_safe_shared_list, rewrite_print, is_user_exist, generate_log
from gogym.core import get_available_slot_list, User, go_user, get_reservation_info
from gogym.underlying import get_date_next_week


def go(date=get_date_next_week()) -> None:
    """
    用户可以调用此函数让 users 目录下的所有账户都抢 date 那天的健身房。
    :param date: "20xx-xx-xx"
    :return: None
    """

    # 日志记录：生成一个安全列表，并重写print
    backup = get_safe_shared_list()
    rewrite_print(backup)

    # 如果 users 目录里没有用户的 json 则提示需要保存并退出
    if not is_user_exist():
        print(f"data/users目录中没有用户，请调用User.save()函数保存新用户。")
        generate_log(backup)
        return None

    # 打印下周当天的预信息
    print(f"-----------------------------------当天预约信息-----------------------------------")
    available_slot_list = get_available_slot_list(date, show=True)

    # 如果列表为空，表示当天已经没有可以预约的时间段，退出
    if not available_slot_list:
        print(f"------------------------{date} 当天已经没有时间段可以预约-----------------------")
        generate_log(backup)
        return None

    # 将每个用户的go_user进程都添加到进程池 pool 里
    pool = []
    for user in [each[0] for each in User.get_info()]:
        each = Process(target=go_user, args=(user, date, available_slot_list, backup), name=f"Process-{user}")
        pool.append(each)

    # 启动所有进程
    for each in pool:
        each.start()
    print(f"----------------------------------所有进程已启动----------------------------------")

    # 等待所有进程结束
    for each in pool:
        each.join()
    print(f"----------------------------------所有进程已完成----------------------------------")

    # 打印所有用户今天所抢的健身房
    get_reservation_info(user="all", date=date, is_print=True)

    # 日志记录：生成日志文件
    generate_log(backup)
    return None


def save(initial, name, account, password, phone, slot_preference) -> None:
    """
    用户可以调用此函数来保存一个新的账户。
    其中的 slot_preference 表示你的场地偏好，
    [4, 5, 6, 7] 表示先抢第4个时间段的场地，抢不到就抢5，再是6，再是7，如果7还抢不到今天就不抢了。
    :param initial: "hxt"
    :param name: "黄啸天"
    :param account: "24820231162341"
    :param password: "Hxt20010623."
    :param phone: "13871234567"
    :param slot_preference: [4, 5, 6, 7]
    :return:
    """
    # 开始记录日志
    backup = get_safe_shared_list()
    rewrite_print(backup)

    # main
    User.save(initial, name, account, password, phone, slot_preference)

    # 生成日志文件
    generate_log(backup)
    return None


def check(user="all", date="now") -> None:
    """
    用户可以调用此函数来检查若干个用户的预约情况。
    user 可以选择"all", "xxx". 其中 xxx 是用户的 initial。
    all 表示查询 users 里的所有用户，xxx 表示查询某一个用户。
    date 可以选择"all", "now", "new", "this_week", "20xx-xx-xx".
    all 表示查询用户的所有预约，now 表示查询今天的预约，new 和 this_week 表示查询最新一天预约，
    20xx-xx-xx 表示查询某一天的预约（超过三十天的查询不到）。
    :param user: "all", "xxx"
    :param date: "all", "now", "new", "this_week", "20xx-xx-xx"
    :return: None
    """
    # 开始记录日志
    backup = get_safe_shared_list()
    rewrite_print(backup)

    # 打印输出
    get_reservation_info(user=user, date=date, is_print=True)

    # 生成日志文件
    generate_log(backup)
    return None



