"""
vw602- Gabriel Sanchez
1-9-2025

"""
import tkinter as tk
import time

# Constants for Pomodoro timings
WORK_TIME = 25 * 60  # 25 minutes of work
SHORT_BREAK = 5 * 60  # 5-minute short break
LONG_BREAK = 15 * 60  # 15-minute long break
CYCLE = 4  # Number of work sessions before a long break


class PomodoroApp:
    def __init__(self):
        # Create the main application window
        self.window = tk.Tk()
        self.window.title("Pomodoro Timer")
        self.window.geometry("300x200")

        # Timer label for countdown
        self.timer_label = tk.Label(self.window, text="Timer", font=("Arial", 24))
        self.timer_label.pack(pady=20)

        # Start button
        self.start_button = tk.Button(self.window, text="Start", command=self.start_timer)
        self.start_button.pack()

        # Reset button
        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset_timer)
        self.reset_button.pack()

        # Timer state
        self.timer_running = False
        self.current_time = WORK_TIME
        self.work_sessions = 0

        # Update the timer display
        self.update_timer()
        self.window.mainloop()

    def update_timer(self):
        """
        Updates the timer display every second.
        """
        minutes = self.current_time // 60  # Get minutes
        seconds = self.current_time % 60  # Get seconds
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")  # Format time as MM:SS

        # Countdown if timer is running
        if self.timer_running and self.current_time > 0:
            self.current_time -= 1
            self.window.after(1000, self.update_timer)  # Update every second
        elif self.timer_running and self.current_time == 0:
            self.handle_timer_end()  # Handle the end of the timer

    def start_timer(self):
        """
        Starts the timer.
        """
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def reset_timer(self):
        """
        Resets the timer to the initial work session.
        """
        self.timer_running = False
        self.current_time = WORK_TIME
        self.update_timer()

    def handle_timer_end(self):
        """
        Handles the transition between work and break sessions.
        """
        self.timer_running = False
        self.work_sessions += 1

        # Determine next session type (work, short break, or long break)
        if self.work_sessions % CYCLE == 0:  # Long break after 4 work sessions
            self.current_time = LONG_BREAK
        elif self.work_sessions % 2 == 0:  # Short break after each work session
            self.current_time = SHORT_BREAK
        else:  # Regular work session
            self.current_time = WORK_TIME

        # Automatically start the next session
        self.timer_running = True
        self.update_timer()


if __name__ == "__main__":
    PomodoroApp()