import tkinter as tk
from tkinter import ttk
from reader_utils import PDFReader
from speaker_utils import Speaker
from bl_utils import BLFileManager, bl_run_in_thread, bl_show_notification

class PDFTTSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("root")
        self.root.geometry("500x300")
        self.root.resizable(True, True)
        
        self.file_manager = BLFileManager()
        self.setup_ui()
        
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = ttk.Label(
            main_frame, 
            text="PDF Text-to-Speech Converter",
            font=("Arial", 16)
        )
        title_label.pack(pady=(0, 20))
        
        self.file_path_var = tk.StringVar()
        self.file_path_var.set("No file selected")
        
        file_frame = ttk.Frame(main_frame)
        file_frame.pack(fill=tk.X, pady=10)
        
        file_path_label = ttk.Label(
            file_frame,
            textvariable=self.file_path_var,
            width=40,
            anchor="w",
            background="#f0f0f0",
            padding=5
        )
        file_path_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        select_file_btn = ttk.Button(
            file_frame,
            text="Select PDF",
            command=self.select_pdf_file
        )
        select_file_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
        voice_frame = ttk.Frame(main_frame)
        voice_frame.pack(fill=tk.X, pady=10)
        
        voice_label = ttk.Label(voice_frame, text="Select Voice:")
        voice_label.pack(side=tk.LEFT)
        
        self.voices = {
            "Dávid": "M336tBVZHWWiWb4R54ui",
            "Alexandra": "kdmDKE6EkgrWrrykO9Qt",
            "Grandpa Spuds Oxley": "NOpBlnGInO9m6vDvFkFC"
        }
        
        self.selected_voice = tk.StringVar()
        self.selected_voice.set("Dávid")
        
        voice_dropdown = ttk.Combobox(
            voice_frame,
            textvariable=self.selected_voice,
            values=list(self.voices.keys()),
            state="readonly",
            width=25
        )
        voice_dropdown.pack(side=tk.RIGHT, padx=(10, 0))
        
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        self.play_btn = ttk.Button(
            button_frame,
            text="Play",
            command=self.play_pdf_text,
            width=15,
            state=tk.DISABLED
        )
        self.play_btn.pack()
        
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=10)
        
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        
        status_label = ttk.Label(
            status_frame,
            textvariable=self.status_var,
            anchor="w"
        )
        status_label.pack(fill=tk.X)
    
    def select_pdf_file(self):
        if self.file_manager.select_file(self.root):
            file_path = self.file_manager.get_file_path()
            self.file_path_var.set(file_path)
            self.play_btn.config(state=tk.NORMAL)
            self.status_var.set("PDF file selected")
        else:
            self.status_var.set("No file selected")
    
    def play_pdf_text(self):
        if not self.file_manager.validate_file():
            bl_show_notification("Error", "Please select a valid PDF file", "error")
            return
        
        self.status_var.set("Processing PDF...")
        self.play_btn.config(state=tk.DISABLED)
        
        bl_run_in_thread(self.process_pdf_to_speech)
    
    def process_pdf_to_speech(self):
        try:
            file_path = self.file_manager.get_file_path()
            pdf_reader = PDFReader(file_path)
            
            pdf_text = pdf_reader.read_pdf()
            if pdf_text:
                self.root.after(0, lambda: self.status_var.set("Converting text to speech..."))
                
                selected_voice_name = self.selected_voice.get()
                voice_id = self.voices[selected_voice_name]
                speaker = Speaker(text=pdf_text, voice_id=voice_id)
                speaker.text_to_speech()
                
                self.root.after(0, lambda: self.status_var.set("Playback complete"))
                self.root.after(0, lambda: self.play_btn.config(state=tk.NORMAL))
            else:
                self.root.after(0, lambda: self.status_var.set("No text extracted from PDF"))
                self.root.after(0, lambda: self.play_btn.config(state=tk.NORMAL))
                bl_show_notification("Error", "No text could be extracted from the PDF file", "error")
        except Exception as e:
            self.root.after(0, lambda: self.status_var.set(f"Error: {str(e)}"))
            self.root.after(0, lambda: self.play_btn.config(state=tk.NORMAL))
            bl_show_notification("Error", f"An error occurred: {str(e)}", "error")

def main():
    root = tk.Tk()
    app = PDFTTSApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()