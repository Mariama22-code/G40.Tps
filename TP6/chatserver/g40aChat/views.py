from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("""<!DOCTYPE html>
<html>
<body>

<h2>Connexion au chat</h2>

<form method="post" action="/chat/">
    <label>Login :</label><br>
    <input type="text" name="login"><br><br>
    <label>Mot de passe :</label><br>
    <input type="password" name="password"><br><br>
    <button type="submit">Se connecter</button>
    <button type="reset">Annuler</button>
</form>

</body>
</html>""")

def page_404(request, exception):
    return HttpResponseNotFound("""<html>
<body>
<h1>404 Not Found</h1>
</body>
</html>""")