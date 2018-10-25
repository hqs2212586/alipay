from django.shortcuts import render, redirect, HttpResponse
from utils.pay import AliPay
# Create your views here.
import time
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def aliPay():
    obj = AliPay(  # 生成Alipay对象
        appid=settings.APPID,  # 沙箱APPID
        # 服务器异步通知页面路径
        # 如果支付成功，支付宝会向这个地址发送POST请求（因此这个地址必须是公网地址）。 并在这里做校验，是否支付完成。
        app_notify_url=settings.NOTIFY_URL,
        # 页面跳转同步通知页面路径
        # 如果支付成功，支付成功后重定向回到你网站的地址（也可以只内网地址）。
        return_url=settings.RETURN_URL,
        app_private_key_path=settings.PRI_KEY_PATH,  # 应用私钥
        alipay_public_key_path=settings.PUB_KEY_PATH,  # 支付宝公钥
        debug=True,  # True：向沙箱环境提交，False:向正式环境提交。默认是False。
    )
    return obj


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')

    alipay = aliPay()   # 实例化

    # 对购买的数据进行加密
    money = float(request.POST.get('price'))   # 将钱转为float类型
    query_params = alipay.direct_pay(   # 利用Alipay对象将买的数据加密，变为一个参数
        subject="充气式韩红",   # 商品简单描述
        out_trade_no="x2" + str(time.time()),   # 生成随机字符串作为商户订单号
        total_amount=money,    # 交易金额(单位：元 保留两位小数)
    )

    # 利用参数拼接支付宝网关，得到支付地址
    pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)

    return redirect(pay_url)


def pay_result(request):
    """
    支付完成后跳转回的地址
    :param request:
    :return:
    """
    # 跳转回商户页面时，携带了大量参数
    params = request.GET.dict()
    sign = params.pop('sign', None)

    alipay = aliPay()  # 实例化

    status = alipay.verify(params, sign)
    if status:
        return HttpResponse("支付成功")

    return HttpResponse("支付失败")


@csrf_exempt    # 取消csrf认证装饰器
def update_order(request):
    """
    支付成功后，支付宝向该地址发送的POST请求（用于修改订单状态）
    :param request:
    :return:
    """
    if request.method == "POST":
        from urllib.parse import parse_qs

        # 请求体的数据
        body_str = request.body.decode("utf-8")
        post_data = parse_qs(body_str)

        post_dict = {}
        for k,v in post_data.items():
            post_dict[k] = v[0]
        print(post_dict)

        sign = post_dict.pop('sogn', None)

        alipay = aliPay()  # 实例化

        # 对传过来的数据进行校验
        status = alipay.verify(post_dict, sign)
        if status:
            # 校验成功，修改订单状态
            out_trade_no = post_dict.get("out_trade_no")   # 拿到订单号
            print(out_trade_no)
            return HttpResponse("支付成功")
        else:
            return HttpResponse("支付失败")
    return HttpResponse("")