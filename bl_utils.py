import tkinter as tk
from tkinter import filedialog, messagebox
import threading

class BLFileManager:
    def __init__(self):
        self.current_file_path = None
        self.file_type_filters = [("PDF Files", "*.pdf")]
    
    def select_file(self, parent_window):
        file_path = filedialog.askopenfilename(
            title="Select PDF File",
            filetypes=self.file_type_filters,
            parent=parent_window
        )
        if file_path:
            self.current_file_path = file_path
            return True
        return False
    
    def get_file_path(self):
        return self.current_file_path
    
    def validate_file(self):
        if not self.current_file_path:
            return False
        if not self.current_file_path.lower().endswith('.pdf'):
            return False
        return True

def bl_run_in_thread(func, *args, **kwargs):
    thread = threading.Thread(target=func, args=args, kwargs=kwargs)
    thread.daemon = True
    thread.start()
    return thread

def bl_show_notification(title, message, notification_type="info"):
    if notification_type == "error":
        messagebox.showerror(title, message)
    elif notification_type == "warning":
        messagebox.showwarning(title, message)
    else:
        messagebox.showinfo(title, message)
