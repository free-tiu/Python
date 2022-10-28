from django.shortcuts import render, redirect

from app01.models import Department


def depart_list(request):
    """ 部门列表 """
    # 获取部门表中所有部门信息
    depart_list = Department.objects.all()

    context = {
        'depart_list': depart_list
    }

    return render(request, 'depart_list.html', context)


def depart_add(request):
    """ 添加部门 """
    if request.method == 'POST':
        depart_name = request.POST.get('title')
        # 测试输出
        # print(depart_name)
        Department.objects.create(title=depart_name)

        # 部门添加成功后，重定向到部门列表页面
        return redirect('/depart/list/')

    return render(request, 'depart_add.html')


def depart_del(request):
    """ 删除部门 """
    # 获取部门ID
    nid = request.GET.get('nid')
    # 删除操作
    Department.objects.filter(id=nid).delete()

    return redirect('/depart/list')


def depart_edit(request, nid):
    """ 编辑部门 """
    if request.method == 'GET':
        # 根据nid获取部门信息，并获取Queryset对象中的第一条数据
        depart = Department.objects.filter(id=nid).first()
        # 测试输出
        # print(depart.title)
        # 将获取到的部门信息传到前端
        context = {
            'depart': depart
        }

        return render(request, 'depart_edit.html', context)

    elif request.method == 'POST':
        depart_name = request.POST.get('title')
        # 测试输出
        # print(depart_name)

        Department.objects.filter(id=nid).update(title=depart_name)

        return redirect('/depart/list/')

















