import flet
from flet import ButtonStyle, Column, FilledButton, Page, Row, Text, TextField, colors
from flet.buttons import RoundedRectangleBorder
from flet.ref import Ref
from calculator import simple_interest


def main(page: Page):
    page.title = "Welcome to my Simple Interest Calculator!"
    page.padding = 75
    principal = Ref[TextField]()
    rate = Ref[TextField]()
    time = Ref[TextField]()
    result = Ref[Column]()

    def get_interest(e):
        p = int(principal.current.value)
        r = float(rate.current.value)/100
        t = int(time.current.value)
        result.current.controls.append(Text(f"Congratulation, your simple interest is Ksh{simple_interest(p,r,t)}", size = 20, weight="w600"))
        principal.current.value = ""
        rate.current.value = ""
        time.current.value = ""
        page.update()
        result.current.controls.pop()

    page.add(
    Row(
        [
            Text("Welcome to my Simple Interest Calculator!", size = 50, color = "orange", weight = "bold"),
        ],
    ),
    Column(
        [
                TextField(ref=principal, label = "What is your principal?", width=700),
                TextField(ref=rate, label = "What is your rate?", width=700),
                TextField(ref=time, label = "What is your time in years?", width=700),
                    FilledButton(
                        "Calculate Simple Interest Here",

style = ButtonStyle(shape=RoundedRectangleBorder(radius=5), padding=14),
                        on_click=get_interest,
              ),
              Column(ref=result),
        ]
    ),
)


flet.app(target=main)




    
        
