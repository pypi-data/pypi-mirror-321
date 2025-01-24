import tkinter
import tkinter.messagebox
import traceback
import typing


class _ErrorBox(tkinter.Toplevel):
    def __init__(self, message: str, master: tkinter.Tk | tkinter.Frame | None = None) -> None:
        super().__init__(master=master)

        self.minsize(width=200, height=40)
        self.resizable(width=False, height=False)
        self.protocol(name="WM_DELETE_WINDOW", func=self.destroy)
        self.title(string="Error")

        # Calculate the needed width/height
        width = max(map(len, message.split("\n")))
        height = message.count("\n") + 1
        # Create the text widget
        self.text = tkinter.Text(
            master=self,
            # bg="#f0f0ed",
            height=height,
            width=width,
            highlightthickness=0,
            bd=0,
            foreground="red",
            selectbackground="blue",
        )
        self.text.insert(index="end", chars=message)
        self.text.config(state="disabled")

        self.button = tkinter.Button(master=self, text="Ok", command=self.destroy)

        # Organize
        padx = 5
        pady = 2.5

        self.text.pack(padx=padx, pady=pady)
        self.button.pack(padx=padx, pady=pady)

        # Required to get accurate size information for centering
        self.update_idletasks()

        # Center the popup
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = self.winfo_width()
        window_height = self.winfo_height()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(newGeometry=f"+{x}+{y}")

        # Make sure the user isn't able to spawn new popups while this is still alive
        self.grab_set()
        self.mainloop()


def _raise_as_tkinter_error_message_box(function: typing.Callable) -> typing.Callable:
    def wrapper(*args: tuple[typing.Any, ...], **kwargs: dict[typing.Any, typing.Any]) -> typing.Any:
        try:
            return function(*args, **kwargs)
        except Exception as exception:  # noqa: BLE001, rerouting all exceptions is the point
            # Due to the asynchronous nature of the error, the full stacktrace can accumulate multiple issues
            # over the runtime of the _app.
            # All attempts to clear the stacktrace of past errors failed, so manual string parsing is performed.
            stacktrace_lines = traceback.format_exception(exception)
            latest_stacktrace_start_index = -stacktrace_lines[::-1].index("Traceback (most recent call last):\n") - 1
            latest_stacktrace_lines = stacktrace_lines[latest_stacktrace_start_index:]
            latest_stacktrace = "".join(latest_stacktrace_lines)

            message = f"Exception in {function.__name__}\n\n{type(exception)}: {exception!s}\n\n{latest_stacktrace}"
            _ErrorBox(message=message)

    return wrapper


class ErrorBoxMetaClass(type):
    """
    A generic metaclass for rerouting exceptions.

    Specifically causes all Pythonic errors which occur during the execution of any bound method of the main class
    (which is expected to be a Tkinter application) to be displayed in an error message box.
    """

    def __new__(cls, name: typing.Any, bases: typing.Any, dct: dict[typing.Any, typing.Any]) -> type:
        for attribute, value in dct.items():
            if callable(value):
                dct[attribute] = _raise_as_tkinter_error_message_box(function=value)
        return super().__new__(cls, name, bases, dct)
