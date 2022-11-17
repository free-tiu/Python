from django.shortcuts import render


def chart_default(request):
    """ 数据统计图表 """

    return render(request, 'echart.html')

