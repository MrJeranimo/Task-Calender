import customtkinter as ctk
import application_runner as app_r

app = ctk.CTk()
app.title("My Modern App")
app.geometry("1080x720")

label = ctk.CTkLabel(app, text="Hello, world!", font=("Arial", 20))
label.pack(pady=20)

button = ctk.CTkButton(app, text="Open Discord",
                       command=app_r.launch_discord)
button.pack(pady=10)

close_button = ctk.CTkButton(app, text="Close Discord",
                             command=app_r.close_discord)
close_button.pack(pady=10)

app.mainloop()
