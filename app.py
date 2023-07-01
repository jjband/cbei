import flet as ft
from supabase import create_client,Client
URL = "https://rdnuwsnvckpunrmmlrbn.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJkbnV3c252Y2twdW5ybW1scmJuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4ODE3NjA4NiwiZXhwIjoyMDAzNzUyMDg2fQ.aUywzTT5mcVY6tThzKgdIeL5tjDrefIGHi0I86kbzzY"

def supa():
    return create_client(URL,KEY)





def main(page:ft.Page):
    page.title = "flet"
    supabase = supa()

    def 버튼클릭(e):
        print("클릭", field.value)
        supabase.table("name_table").insert({"name":field.value}).execute()
        name_render()
        #n = ft.Text(field.value)
        #col.controls.append(n)
        field.value=""
        page.update()

    txt = ft.Text("안녕 What's your name")
    field = ft.TextField(hint_text="이름을 써주세요")
    btn = ft.TextButton("버튼", on_click=버튼클릭)

    row = ft.Row()
    col = ft.Column()
    supabase = supa()
    def name_render():
        r = supabase.table("name_table").select("*").execute()
        for i in range(len(col.controls)):
            col.controls.pop()
        for info in r.data:
            t = ft.Text(info["name"]+"님 안녕하세요!")
            col.controls.append(t)

    
    name_render
    page.add(col)
    page.add(txt)
    page.add(field)
    page.add(btn)
    page.update()
    
ft.app(target = main)