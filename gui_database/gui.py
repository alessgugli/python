import customtkinter as ctk
import sqlite3

def update():
    table.configure(state = "normal")
    table.delete("1.0", "end")
    table.insert("1.0","NOME\t\tCOGNOME\t\tEMAIL\n")
    table.insert("2.0","\n")
    c.execute("SELECT * FROM persone")
    righe = c.fetchall()
    i = 3
    for riga in righe:
        table.insert(f"{i}.0", f"{riga[0]} {riga[1]}\t\t{riga[2]}\t\t{riga[3]}\n")
        i += 1
    table.configure(state = "disabled")

def insert():
    input = entry.get().split()
    c.execute(f"INSERT INTO persone VALUES(NULL,'{input[0]}','{input[1]}','{input[2]}')")
    entry.delete(0, "end")
    update()
    conn.commit()

def delete_window():
    delete_window =  ctk.CTkToplevel(window)
    delete_window.geometry("300x300")
    delete_window.title("Elimina")
    label = ctk.CTkLabel(delete_window, text = "Inserisci email della persona da eliminare:")
    label.place(relx = 0.5, rely = 0.1, anchor="center")
    delete_entry = ctk.CTkEntry(delete_window, width=240)
    delete_entry.place(relx = 0.5, rely = 0.2, anchor="center")
    def delete():
        email = delete_entry.get()
        c.execute(f"DELETE FROM persone WHERE email = '{email}'")
        delete_entry.delete(0, "end")
        update()
    delete_btn = ctk.CTkButton(delete_window, command = delete, text = "elimina",width=115)
    delete_btn.place(relx = 0.71, rely = 0.33, anchor="center")
    close_btn = ctk.CTkButton(delete_window, text = "annulla", width=115, fg_color="#2B2B2B", hover_color="#969696" , border_width=1 , border_color="#969696", command = delete_window.destroy)
    close_btn.place(relx = 0.29, rely = 0.33, anchor="center")
    conn.commit()

def change():
    modify = entry_change.get().split()
    entry_change.delete(0, "end")
    c.execute(f"UPDATE persone SET email = '{modify[1]}' WHERE id = '{modify[0]}'")
    update()
    conn.commit()

conn = sqlite3.connect("persone.db")
c = conn.cursor()
window = ctk.CTk()
window.geometry("550x400")
window.resizable(False, False)
window.title("Database Manager")

entry = ctk.CTkEntry(window, width = 530, height = 35, placeholder_text="Inserisci nel seguente formato: Nome Cognome Email")
entry.place(x = 10, y = 10)

table = ctk.CTkTextbox(window, width = 410, height = 335)
table.place(x = 10, y = 55)

update()

btn_insert = ctk.CTkButton(window, command = insert, text = "aggiungi", width = 110, height = 40)
btn_insert.place(x = 430, y = 55)

btn_delete = ctk.CTkButton(window, command = delete_window, text = "elimina", width = 110, height = 40)
btn_delete.place(x = 430, y = 105)


entry_change = ctk.CTkEntry(window, width = 110, height  = 35, placeholder_text="id e email nuova")
entry_change.place(x = 430, y = 303)

btn_change = ctk.CTkButton(window, text = "modifica", command = change, width = 110, height = 40)
btn_change.place(x = 430, y = 348)

window.mainloop()
conn.commit()
conn.close()