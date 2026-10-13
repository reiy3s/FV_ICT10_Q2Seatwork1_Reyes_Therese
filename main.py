from pyscript import display, document

def get_IN(e):
    document.getElementById("output").innerHTML = ""
    name1 = document.getElementById("fn").value
    name2 = document.getElementById("ln").value