import customtkinter as ctk
import application_runner as app_r

app = ctk.CTk()
app.title("My Modern App")
app.geometry("1080x720")

label = ctk.CTkLabel(app, text="Enter application name below:")
label.pack(pady=10)

entry = ctk.CTkEntry(app, placeholder_text="Type here...")
entry.pack(pady=10)


def get_app_name():
    """Gets the app name from the text entry box"""
    app_name = entry.get()
    if app_name != "":
        return app_name
    else:
        return "  "  # Returns an app_name that can't close to prevent errors


text_history = []  # Stores the previous text entries


def add_entry():
    text = entry.get()
    if text and not text_history.__contains__(text):
        text_history.append(text)
        update_history_list()


def update_history_list():
    # Clear current history buttons
    for widget in history_frame.winfo_children():
        widget.destroy()

    # Add new buttons for each history item
    for idx, item in enumerate(reversed(text_history)):
        btn = ctk.CTkButton(
            history_frame,
            text=item,
            command=lambda t=item:
                entry.delete(0, ctk.END) or entry.insert(0, t),
            width=350
        )
        btn.pack(pady=2)


def launch_app(app):
    app_r.launch_app(app)
    add_entry()


button = ctk.CTkButton(app, text="Open App",
                       command=lambda: launch_app(get_app_name()))
button.pack(pady=10)


def close_app(app):
    app_r.close_app(app)
    add_entry()


close_button = ctk.CTkButton(app, text="Close App",
                             command=lambda: app_r.close_app(get_app_name()))
close_button.pack(pady=10)

history_label = ctk.CTkLabel(app, text="Text History")
history_label.pack(pady=15)

history_frame_container = ctk.CTkScrollableFrame(app, width=370, height=300)
history_frame_container.pack(pady=5)
history_frame = ctk.CTkFrame(history_frame_container, width=350)
history_frame.pack(pady=5)

app.mainloop()
