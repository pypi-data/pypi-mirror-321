#!/usr/bin/env python3

import subprocess
import tempfile
import os
from dotenv import load_dotenv
import base64
import json
import requests
import threading
import shutil

# Load environment variables from .env file
load_dotenv()


class ScreenshotAssistant:
    def __init__(self):
        # Load configuration from environment variables with defaults
        self.ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
        self.model = os.getenv("OLLAMA_MODEL", "llava")
        self.window_title = os.getenv("WINDOW_TITLE", "Screenshot Assistant")
        self.screenshot_mode = os.getenv("SCREENSHOT_MODE", "active")
        self.screenshot = None
        self.temp_dir = tempfile.mkdtemp()

    def get_active_window_geometry(self):
        """Get the geometry of the active window using various Wayland tools"""
        try:
            # Try swaymsg for Sway
            if shutil.which("swaymsg"):
                result = subprocess.run(
                    ["swaymsg", "-t", "get_outputs", "--raw"],
                    capture_output=True,
                    text=True,
                )

                if result.returncode == 0:
                    import json

                    outputs = json.loads(result.stdout)
                    focused_output = next(
                        (output for output in outputs if output["focused"]), None
                    )

                    if focused_output:
                        return focused_output["name"]

            # Try hyprctl for Hyprland
            elif shutil.which("hyprctl"):
                result = subprocess.run(
                    ["hyprctl", "monitors", "-j"], capture_output=True, text=True
                )

                if result.returncode == 0:
                    import json

                    monitors = json.loads(result.stdout)
                    focused_monitor = next(
                        (mon for mon in monitors if mon["focused"]), None
                    )

                    if focused_monitor:
                        return focused_monitor["name"]

            # Try getting active monitor with wlr-randr
            elif shutil.which("wlr-randr"):
                result = subprocess.run(
                    ["wlr-randr", "--json"], capture_output=True, text=True
                )

                if result.returncode == 0:
                    import json

                    outputs = json.loads(result.stdout)
                    focused_output = next(
                        (output for output in outputs if output["focused"]), None
                    )

                    if focused_output:
                        return focused_output["name"]

            return None
        except Exception as e:
            print(f"Failed to get active window: {e}")
            return None

    def preview_screenshot(self, is_terminal=False):
        """Preview the screenshot using appropriate viewer"""
        if not self.screenshot:
            return

        if is_terminal:
            # Try kitty's icat if available
            if shutil.which("kitty") and "KITTY_WINDOW_ID" in os.environ:
                subprocess.run(["kitty", "+kitten", "icat", self.screenshot])
            else:
                print("Terminal image preview requires Kitty terminal emulator")
        else:
            # Use imv for Wayland display
            try:
                # Start imv in background
                subprocess.Popen(["imv", self.screenshot])
            except FileNotFoundError:
                print("Please install 'imv' for screenshot preview")

    def capture_screenshot(self):
        """Capture screenshot using grim (Wayland)"""
        try:
            screenshot_path = os.path.join(self.temp_dir, "screenshot.png")

            if self.screenshot_mode == "all":
                # Capture all screens
                cmd = ["grim", screenshot_path]
            elif self.screenshot_mode == "select":
                # Let user select an area
                cmd = ["grim", "-g", "$(slurp)", screenshot_path]
            else:  # 'active' mode
                # Get active screen
                active_output = self.get_active_window_geometry()
                if active_output:
                    cmd = ["grim", "-o", active_output, screenshot_path]
                else:
                    print(
                        "Couldn't determine active screen, falling back to full screenshot"
                    )
                    cmd = ["grim", screenshot_path]

            # Join the command for shell execution if using slurp
            if self.screenshot_mode == "select":
                result = subprocess.run(
                    " ".join(cmd), shell=True, executable="/bin/bash"
                )
            else:
                result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                self.screenshot = screenshot_path
                return self.screenshot
            else:
                print(
                    f"Screenshot capture failed: {result.stderr if hasattr(result, 'stderr') else 'Unknown error'}"
                )
                return None
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")
            return None

    def encode_image(self, image_path):
        """Convert image to base64 string for API transmission"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def ask_ollama(self, prompt, image_path):
        """Send prompt and image to Ollama API and get response"""
        base64_image = self.encode_image(image_path)

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "images": [base64_image],
        }

        try:
            response = requests.post(self.ollama_url, json=payload)
            response.raise_for_status()
            return response.json()["response"]
        except requests.exceptions.RequestException as e:
            return f"Error communicating with Ollama: {str(e)}"

    def show_terminal_prompt(self):
        """Show terminal-based interface"""
        print("\nScreenshot captured! Showing preview...")
        self.preview_screenshot(is_terminal=True)

        print("\nWhat would you like to know about it?")
        while True:
            try:
                prompt = input("\nEnter your question (or 'quit' to exit): ")
                if prompt.lower() in ["quit", "exit", "q"]:
                    break

                print("\nProcessing...")
                response = self.ask_ollama(prompt, self.screenshot)
                print("\nResponse:", response)

            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")
                break

    def show_gui_prompt(self):
        """Try to show GUI interface, fall back to terminal if not available"""
        try:
            import tkinter as tk
            from tkinter import ttk

            # Show the screenshot preview
            self.preview_screenshot()

            def submit_prompt():
                prompt = prompt_entry.get()
                result_text.config(state="normal")
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, "Processing...")
                result_text.config(state="disabled")

                def process():
                    response = self.ask_ollama(prompt, self.screenshot)
                    result_text.config(state="normal")
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, response)
                    result_text.config(state="disabled")

                threading.Thread(target=process, daemon=True).start()

            window = tk.Tk()
            window.title(self.window_title)
            window.geometry("600x400")

            frame = ttk.Frame(window, padding="10")
            frame.pack(fill=tk.BOTH, expand=True)

            prompt_label = ttk.Label(frame, text="Ask about the screenshot:")
            prompt_label.pack(pady=5)

            prompt_entry = ttk.Entry(frame, width=50)
            prompt_entry.pack(pady=5)
            prompt_entry.focus()

            submit_button = ttk.Button(frame, text="Submit", command=submit_prompt)
            submit_button.pack(pady=5)

            result_text = tk.Text(frame, height=10, wrap=tk.WORD)
            result_text.pack(fill=tk.BOTH, expand=True, pady=5)
            result_text.config(state="disabled")

            def on_enter(event):
                submit_prompt()

            def on_escape(event):
                window.destroy()

            prompt_entry.bind("<Return>", on_enter)
            window.bind("<Escape>", on_escape)

            window.mainloop()

        except Exception as e:
            print(f"Could not initialize GUI: {e}")
            print("Falling back to terminal interface...")
            self.show_terminal_prompt()

    def run(self):
        """Main entry point to start the application"""
        if self.capture_screenshot():
            self.show_gui_prompt()
        else:
            print("Could not start application due to screenshot capture failure")
