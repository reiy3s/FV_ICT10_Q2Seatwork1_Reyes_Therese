from pyscript import display, document

members = ["Zoey Ledres", "Cheree Mendoza", "Princess Schwab", "Therese Reyes", "Elise Ramos"]

def get_IN(e):
    document.getElementById("output").innerHTML = ""
    name1 = document.getElementById("fn").value
    name2 = document.getElementById("ln").value

    print(f'{name1} {name2}', target = "output")