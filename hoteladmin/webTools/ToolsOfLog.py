class LogTools:

    @staticmethod
    def checkin(request, *args):
        """
        判断登录状态, 逻辑与的关系
        :param request: 请求对象
        :param args: 判断需要判断对象是否在session中
        :return: 登录返回True, 否则返回False
        """
        ses_dic = request.session
        for arg in args:
            if arg in ses_dic:
                continue
            else:
                return False
        return True

    @staticmethod
    def get_infos(request, *args):
        """
        获取POST/GET信息
        :param request: 请求对象
        :param args: 输入需要获取的数据名称
        :return: 返回列表, 可以用拆包形式获取
        """
        info_list = []
        if request.method == "GET":
            for arg in args:
                info_list.append(request.GET.get(arg))
            return info_list
        if request.method == "POST":
            for arg in args:
                info_list.append(request.POST.get(arg))
            return info_list