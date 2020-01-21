from proxmoxer import ProxmoxAPI
from django.shortcuts import render


def login(host, password):
    return ProxmoxAPI(host, user='root@pam', password=password, verify_ssl=False)


def proxmox(request):
    if request.method == 'POST':
        log_in = login(host=request.POST.get('host'), password=request.POST.get('password'))
        if log_in is not None:
            machines = log_in.nodes.get()
            return render(request, 'proxymox_web_ui/virtual_machines_list.html', {'machines': machines})
    return render(request, 'proxymox_web_ui/login.html')

