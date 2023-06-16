import keyboard
from config_window import ConfigWindow
from input_window import InputWindow

def register_shortcut(shortcut, callback):
    keyboard.add_hotkey(shortcut, callback)

def shortcut_triggered(config_window):
    input_window = InputWindow(config_window.target_file)
    input_window.mainloop()

def main():
    config_window = ConfigWindow()
    config_window.load_config()
    register_shortcut(config_window.shortcut_entry.get(), lambda: shortcut_triggered(config_window))
    config_window.mainloop()

if __name__ == "__main__":
    main()
