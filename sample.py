from tkinter import * 


def get_quote():
    # response = requests.get("http://127.0.0.1:8000")
    # response.raise_for_status()
    # data = response.json()
    # print(data)
    # lyric = data["quote"]
    # canvas.itemconfig(quote_text, text=lyric)
    pass


window = Tk()
window.title("TS Once Said...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
quote_text = canvas.create_text(150, 207, text="TS Said...", width=250)
canvas.grid(row=0, column=0)

t_button = Button(text="Hello", command=get_quote)
t_button.grid(row=1, column=0)
