from pyscript import display, document #link to index...?

members = ["Zoey Ledres", "Cheree Mendoza", "Princess Schwab", "Therese Reyes", "Elise Ramos"] #im pretty sure this is the ganglang thats allowed

def get_IN(e):
    name1 = document.getElementById("fn").value
    name2 = document.getElementById("ln").value

    full_name = f"{name1.strip()} {name2.strip()}" #combines name
    is_member = full_name in members #true or false

    if is_member:
        display("Welcome to the Rainbow Catering Club!", target="output") #displays when a member
    else:
        display("Oops! Are you sure you're part of this club?", target="output") #displays when not a member (?)