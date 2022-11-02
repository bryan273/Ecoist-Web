from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from donate.models import Donasi
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from django.core import serializers
from donate.forms import DonateForm
from django.urls import reverse

# Create your views here.
# @login_required(login_url='ecoist/login/')
def show_donate(request):
    context = {'form':DonateForm()}
    return render(request, "donate.html", context)

# @login_required(login_url='/ecoist/login/')
# def donate_ajax(request):
#     if request.method == "POST":
#         nominal = request.POST.get("nominal")
#         namaPohon = request.POST.get("namaPohon")
#         jumlahPohon = request.POST.get("jumlahPohon")
#         pesan = request.POST.get("pesan")
#         donasi = Donasi(user=request.user,nominal=nominal,namaPohon=namaPohon,jumlahPohon=jumlahPohon,pesan=pesan)
#         donasi.save()

#         return HttpResponse(b"CREATED", status=201)
            
#     return HttpResponseNotFound()

def donate_ajax(request):
    if request.method == 'POST':
        nominal = request.POST.get('nominal')
        namaPohon = request.POST.get('namaPohon')
        jumlahPohon = request.POST.get('jumlahPohon')
        pesan = request.POST.get('pesan')
        todo = Donasi.objects.create(nominal=nominal,namaPohon=namaPohon,jumlahPohon=jumlahPohon,pesan=pesan,user=request.user)
        hasil = {
            'fields':{
                'nominal':todo.nominal,
                'namaPohon':todo.namaPohon,
                'jumlahPohon':todo.jumlahPohon,
                'pesan':todo.pesan,
            },
            'pk':todo.pk
        }
        return JsonResponse({"instance":hasil}, status=200)

# @login_required(login_url='/ecoist/login/')
def show_json(request):
    data = Donasi.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")