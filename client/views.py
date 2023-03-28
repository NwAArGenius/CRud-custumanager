from django.shortcuts import render, redirect
from .models import  Client 
# Create your views here.

def listall(request):
    query = request.GET.get('q')
    if query:
        clients = Client.objects.filter(full_name__icontains=query)
    else:
        clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'list.html', context)

def createClient(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        status = request.POST.get('status')
        client = Client.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            status=status    
            )
        return redirect('list')
    return render(request, 'create.html')

def Update(request, id):
    client = Client.objects.get(id=id)
    if request.method == 'POST':
        client.full_name = request.POST.get('full_name')
        client.email = request.POST.get('email')
        client.phone = request.POST.get('phone')
        client.status = request.POST.get('status')
        client.save()
        return redirect('list')
    context = {'client':client}
    return render(request, 'update.html', context)


def delete(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect('list')    
    
        
    

        
