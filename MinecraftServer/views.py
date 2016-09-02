from django.shortcuts import render
from mcstatus import MinecraftServer
from MinecraftServer.models import MCServer, Admin
# Create your views here.

def index(request):
    server = []
    status = []
    servers = MCServer.objects.all()
    for srv in servers:
        server.append(srv)
        try:
            if srv.IPaddress:
                mcsrv = MinecraftServer("%s" % srv.IPaddress, int(srv.port))
                status.append(mcsrv.status())
            elif srv.domain:
                mcsrv = MinecraftServer("%s" % srv.domain, int(srv.port))
                status.append(mcsrv.status())
            else:
                status = "Server doesnt contain any addresses. Where am I meant to look? Please contact the admin: " + str(e)
                admin = Admin.objects.first()
                return render(request, 'MinecraftServer/index.html', {'status': status, 'admin': admin})

        except Exception, e:
            status = "Cant reach the server. Please contact the admin: " + str(e)
            admin = Admin.objects.first()
            return render(request, 'MinecraftServer/index.html', {'status': status, 'admin': admin})

    return render(request, 'MinecraftServer/index.html', {'status': status})