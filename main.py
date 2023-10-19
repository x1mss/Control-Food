import PySimpleGUI as sg
import time

sg.set_global_icon('eat.ico')
sg.theme("LightBrown3")

shedule_file = open("eat.txt", "r" , encoding="utf-8")

todo_list = shedule_file.readlines()

clock = sg.Text('',key = 'clock')
imput_eat = sg.InputText(key = 'eat')
combo_time = sg.Combo(values =['00:00','01:00',"02:00", "03:00",'04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00'], key='time')
label_time = sg.Text("Время приёма пищи.")
label_eat = sg.Text("Каллории еды.")
add = sg.Button("Добавить")
shedule_list = sg.Listbox(values=todo_list,key='todos_f', size=[40,10], enable_events=True)
edit = sg.Button("Изменить")
del_ = sg.Button("Удалить")
exit = sg.Button("Выход")

window = sg.Window("Контроль калорий", layout=[
    [clock],
    [shedule_list],
    [label_time],
    [combo_time],
    [label_eat],
    [imput_eat],
    [add],
    [exit]],
    font=("Impact", 15),
)

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%d.%m.%y  %H:%M:%S"))
    if event == sg.WIN_CLOSED or event == "Выход":
            break
    elif event == "Добавить":
        file = open('eat.txt','a', encoding="utf-8")
        file.write(values['time'] + ' - ' + values['eat'] + ' Ккал' + '\n')
        file.close()
        file = open('eat.txt','r', encoding="utf-8")
        a = file.readlines()
        window['todos_f'].update(values=a)
        file.close()
window.close()