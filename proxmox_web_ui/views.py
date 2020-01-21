from proxmoxer import ProxmoxAPI
from django.shortcuts import render
from django.http import JsonResponse


def login(host, password):
    return ProxmoxAPI(host, user='root@pam', password=password, verify_ssl=False)


def proxmox(request):
    if request.method == 'POST':
        log_in = login(host=request.POST.get('host'), password=request.POST.get('password'))
        if log_in is not None:
            machines = log_in.nodes.get()
            return JsonResponse(machines, safe=False)
    return render(request, 'proxymox_web_ui/login.html')

