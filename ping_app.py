import tkinter as tk
import csv
import threading
from ping3 import ping, verbose_ping

def check_servers():
    with open('servers.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for widget in frame.winfo_children():
            widget.destroy()  # Clear existing labels
            
        for row in reader:
            server_name = row['Server Name']
            ip_address = row['IP Address']
            result = ping(ip_address)
            
            if result is not None:
                status = "Online"
                bg_color = "green"
            else:
                status = "Offline"
                bg_color = "red"
            
            server_label = tk.Label(frame, text=f"{server_name}: {status}", bg=bg_color, font=("Helvetica", 24))
            server_label.pack(fill=tk.BOTH, expand=True)

def periodic_check():
    check_servers()
    app.after(30000, periodic_check)  # Schedule the next check after 30 seconds (30000 milliseconds)

def close_app(event):
    app.destroy()

app = tk.Tk()
app.title("Server Status Checker")
app.attributes('-fullscreen', True)  # Make the application full-screen

frame = tk.Frame(app, bg="white")  # Set the background color of the frame to white
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Start periodic server checks
periodic_check()

# Bind the Escape key to the close_app function
app.bind("<Escape>", close_app)

app.mainloop()
