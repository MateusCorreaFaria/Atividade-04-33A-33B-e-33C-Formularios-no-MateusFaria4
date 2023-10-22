from django.shortcuts import render, redirect
from .models import carros, videogames

# Create your views here.
def home(request):
    carrosL = carros.objects.all()
    videogamesL = videogames.objects.all()

    return render(request, "review.html", context={ 
        "Carros": carrosL,
        "videogames": videogamesL
    })

def create_carros(request):
    if request.method == 'POST':
        carros.objects.create(
            nome=request.POST['nome'],
            fabricante=request.POST['fabricante'],
            automatico_manual=request.POST['automatico_manual'],
            data_fabricação=request.POST['data_fabricação']
        )
        return redirect('review') 
    return render(request, 'forms.html', context={"action": "Adicionar"})

def update_carros(request, id):
    carro = carros.objects.get(id=id)
    if request.method == "POST":
        carro.nome = request.POST["nome"]
        carro.fabricante = request.POST["fabricante"]
        carro.automatico_manual = request.POST["automatico_manual"]
        carro.data_fabricação = request.POST["data_fabricação"]
        carro.save()

        return redirect("review")
    return render(request, "forms.html", context={"action": "Atualizar", "carros": carros})

def delete_carros(request, id):
    carro = carros.objects.get(id=id)
    if request.method == "POST":
        if "confirm" in request.POST:
            carro.delete()
        return redirect("review")
    return render(request, "are_you_sure.html", context={"carros": carros})

def create_videogames(request):
    if request.method == 'POST':
        videogames.objects.create(
            nome=request.POST['nome'],
            empresa=request.POST['empresa'],
            estilo=request.POST['estilo'],
            data_lançamento=request.POST['data_lançamento']
        )
        return redirect('review') 
    return render(request, 'formsVideogames.html', context={"action": "Adicionar"})

def update_videogames(request, id):
    videogame = videogames.objects.get(id=id)
    if request.method == "POST":
        videogame.nome = request.POST["nome"]
        videogame.empresa = request.POST["empresa"]
        videogame.estilo = request.POST["estilo"]
        videogame.data_lançamento = request.POST["data_lançamento"]
        videogame.save()

        return redirect("review")
    return render(request, "formsVideogames.html", context={"action": "Atualizar", "videogames": videogames})

def delete_videogames(request, id):
    Videogame = videogames.objects.get(id=id)
    if request.method == "POST":
        if "confirm" in request.POST:
            Videogame.delete()
        return redirect("review")
    return render(request, "are_you_Videogames.html", context={"Videogames": Videogame})
