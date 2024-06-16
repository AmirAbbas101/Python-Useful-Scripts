import tkinter as tk
from tkinter import ttk
import winsound
import threading

class AlarmApp:
    def __init__(self, master):
        self.master = master
        master.title("Alarm App")
        master.configure(bg='#f0f0f0')  # Set background color

        # Custom Fonts
        title_font = ('Helvetica', 16, 'bold')
        button_font = ('Helvetica', 12)

        # Title Label
        self.label = ttk.Label(master, text="Alarm will beep every 20 minutes.", background='#f0f0f0', font=title_font)
        self.label.pack(pady=20)

        # Start Button
        self.start_button = ttk.Button(master, text="Start Alarm", command=self.start_alarm, style='Start.TButton')
        self.start_button.pack(pady=10)

        # Stop Button
        self.stop_button = ttk.Button(master, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED, style='Stop.TButton')
        self.stop_button.pack(pady=5)

        self.is_running = False
        self.alarm_thread = None

    def start_alarm(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.alarm_thread = threading.Thread(target=self.alarm_loop)
            self.alarm_thread.start()

    def stop_alarm(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def alarm_loop(self):
        while self.is_running:
            winsound.Beep(1000, 1000)  # Beep sound
            self.master.after(20 * 60 * 1000)  # Wait for 20 minutes

root = tk.Tk()

# Custom Styles
style = ttk.Style(root)
style.configure('Start.TButton', background='#008000', foreground='white', font=('Helvetica', 12), padding=10)
style.map('Start.TButton', background=[('active', '#004d00')])  # Change color on button press
style.configure('Stop.TButton', background='#FF5733', foreground='white', font=('Helvetica', 12), padding=10)
style.map('Stop.TButton', background=[('active', '#cc4125')])  # Change color on button press

app = AlarmApp(root)
root.mainloop()
