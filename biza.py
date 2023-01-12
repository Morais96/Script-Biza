from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
import webbrowser as wb
from datetime import date

main = Tk()
main.title("Cover Letter Generator")

projects = ['Biza', "mete","aqui","os","projetos","que","queres"]

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

window_width = 510
window_height = 280

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

main.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
main.resizable(False, False)
frame = Frame(main, borderwidth = 5)
frame.grid()

ManagerName = Label(frame, width = 25,  borderwidth = 5, relief = SUNKEN, text = "Nome do recrutador")
ManagerNameEntry = Entry(frame, width = 50, borderwidth = 5)

CompanyName = Label(frame, width = 25,  borderwidth = 5, relief = SUNKEN, text = "Empresa")
CompanyNameEntry = Entry(frame, width = 50, borderwidth = 5)

CompanyPurpose = Label(frame, width = 25,  borderwidth = 5, relief = SUNKEN, text = "Propósito da empresa")
CompanyPurposeEntry = Entry(frame, width = 50, borderwidth = 5)

Position = Label(frame, width = 25,  borderwidth = 5, relief = SUNKEN, text = "Posição")
PositionEntry = Entry(frame, width = 50, borderwidth = 5)

options = StringVar(frame)
options.set(projects[0])
Project = Label(frame, width = 25,  borderwidth = 5, relief = SUNKEN, text = "Projeto")
ProjectEntry = OptionMenu(frame, options, *projects)

Interests = Label(frame, width = 25,  borderwidth = 5, relief = SUNKEN, text = "Os meus interesses")
InterestsEntry = Entry(frame, width = 50, borderwidth = 5)

def Create_PDF():
  CL = FPDF()
  CL.add_page()
  CL.set_font('Helvetica', size = 11)
  CL.set_author('Diogo Gomes')
  CL.cell(h = 5, txt = f'{CL.author}', ln = True)
  CL.cell(h = 5, txt = "Engenharia Eletrtécnica e de Computadores", ln = True)
  CL.cell(h = 5, txt = "diogo9191@gmail.com", ln = True)
  CL.cell(h = 5, txt = "(+351) 963 949 407", ln = True)
  CL.cell(h = 5, txt = "Rua da Cova do Ladrão 327, Carreço", ln = True)
  CL.cell(h = 5, txt = f'{date.today().strftime("%d/%m/%Y")}', ln = True)
  CL.ln(20) 
  CL.cell(h = 5, txt = f'Caro {ManagerNameEntry.get()},')
  CL.ln(10)
  CL.multi_cell(w = 190, h = 5, txt = f'Eu estou bastante interessado na vaga de {PositionEntry.get()} na {CompanyNameEntry.get()}, uma vez, que a empresa opera na minha' 
    f' área e se foca em {CompanyPurposeEntry.get()}.', align = 'J', ln = True)
  CL.multi_cell(w = 190, h = 5, txt = f'Considero que sou uma pessoa unicamente proativa e focada. Tenho uma excelente capacidade de cooperação em equipa que é enfatizada pela minha ótima'
    f'organização e pontualidade. Atributos e capacidades que foram desenviolvidos e aprimorados, não só pela minha experiência prática em projetos na universidade,'
    f' como também em projectos de provação, onde testei e validei aplicações de reconhecimento de voz.', align = 'J', ln = True)
  CL.multi_cell(w = 190, h = 5, txt = f'A minha licenciatua em Engenharia Eletrotécnica e de Computadores permitu-me estudar uma plétora de disciplinas tais como cálculo, '
    f'ciências computacionais, robótica, design de circuitos elétricos, automação, eletromecânica, sistemas de comunicação, e física aplicada. A minha educação concedeu-me'
    f'todas as capacidades e skills que necessito para me tornar um engenheiro de sucesso. Ao longo do meu trajeto académico, o projeto que me mais motivou e cativou, '
    f' foi {options.get()}. Este projeto foi o que despertou em mim o meu interesse pela área de {InterestsEntry.get()}.', align = 'J', ln = True)
  CL.multi_cell(w = 190, h = 5, txt = f'Com um enorme interesse em {InterestsEntry.get()}, esta oportunidade de trabalhar para uma empresa como a {CompanyNameEntry.get()} é '
    f'muito estimulante para mim. Os meus feitos tantos corporaticos como académicos demonstram que detenho o conhecimento e capacidade para alcançar a excelência. '
    f'Eu posso dizer com confiança que seria uma excelente adição à empresa e que no ambiente de trabalho certo, a minha forte ética de trabalho e paixão pela área o demonstrariam.', align = 'J', ln = True)
  CL.multi_cell(w = 190, h = 5, txt = f'Por favor não exite em entrar em contacto comigo para agendar uma entrevista ou discutir qualquer questão que possam ter sobre mim'
    f', ou as minhas habilidades que beneficiariam a firma, {CompanyNameEntry.get()}.', align = 'J')
  CL.ln(20)
  CL.cell(h = 5, txt = "Atenciosamente,", ln = True)
  CL.cell(h = 5, txt = f'{CL.author}')
  
  CL.output(f'C:/Users/Luís Morais/desktop/Cover Letter {CompanyNameEntry.get()}.pdf')

  wb.open_new(f'C:/Users/Luís Morais/desktop/Cover Letter {CompanyNameEntry.get()}.pdf')

def condition():
  while ManagerNameEntry.get() == '' or ManagerNameEntry.get().isspace():
    messagebox.showerror("Error", "Por favor indica o nome do recrutador!")
    Generator.wait_variable(ManagerNameEntry.get())

  while CompanyNameEntry.get() == '' or CompanyNameEntry.get().isspace():
    messagebox.showerror("Error", "Por favor preenche o nome da empresa!")
    Generator.wait_variable(CompanyNameEntry.get())

  while CompanyPurposeEntry.get() == '' or CompanyPurposeEntry.get().isspace():
    messagebox.showerror("Error", "Por favor indica o propósito da empresa!")
    Generator.wait_variable(CompanyPurposeEntry.get())

  while PositionEntry.get() == '' or PositionEntry.get().isspace():
    messagebox.showerror("Error", "Por favor indica a posição para a qual te estás a candidatar!")
    Generator.wait_variable(PositionEntry.get())

  while InterestsEntry.get() == '' or InterestsEntry.get().isspace():
    messagebox.showerror("Error", "Por favor indica os teus interesses!")
    Generator.wait_variable(InterestsEntry.get())

def CL_Generator():
  condition()
  Create_PDF()

Generator = Button(main, text = "Criar Carta", relief = RAISED, borderwidth = 5, bg = "black", fg = "white", command = CL_Generator)

ManagerName.grid()
ManagerNameEntry.grid(row = 0, column = 1, columnspan = 2, padx = 0, pady = 5)
CompanyName.grid()
CompanyNameEntry.grid(row = 1, column = 1, columnspan = 2, padx = 0, pady = 5)
CompanyPurpose.grid()
CompanyPurposeEntry.grid(row = 2, column = 1, columnspan = 2, padx = 0, pady = 5)
Position.grid()
PositionEntry.grid(row = 3, column = 1, columnspan = 2, padx = 0, pady = 5)
Project.grid()
ProjectEntry.grid(row = 4, column = 1, columnspan = 2, padx = 0, pady = 5)
Interests.grid()
InterestsEntry.grid(row = 5, column = 1, columnspan = 2, padx = 0, pady = 5)
Generator.grid()

main.mainloop()
