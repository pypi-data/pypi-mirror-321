import tkinter
import tkinter.messagebox

from ._error_box import ErrorBoxMetaClass


class BaseApp(tkinter.Tk, metaclass=ErrorBoxMetaClass):
    """A generic framework for construction complicated Tkinter applications piece-by-piece."""

    def __init__(self) -> None:
        """A relatively simple GUI implementation for the CoMo Recipes Installer based on Tkinter."""
        super().__init__()

        self.setup_attributes()
        self.setup_window()
        self.setup_frame()
        self._center_window()  # Must be done after components are organized

    def setup_attributes(self) -> None:
        """
        Define all internal attributes of the application.

        Leave verbose comments describing the usage of any that have broad effects.
        """
        message = "This method must be overridden in a subclass."
        raise NotImplementedError(message)

    def setup_window(self) -> None:
        """
        Perform the actual setup of the main window of the outermost level of the application.

        Typically, this will involve setting the title, icon, and size of the window.
        It can also involve window configuration settings like resizing or exit conditions.
        """
        message = "This method must be overridden in a subclass."
        raise NotImplementedError(message)

    def setup_frame(self) -> None:
        """
        Perform the actual setup of the main frame contents of the application.

        This is the container that will hold all the widgets and other sub frames.
        """
        message = "This method must be overridden in a subclass."
        raise NotImplementedError(message)

    def _center_window(self) -> None:
        """
        Make initial spawn location the center of any screen.

        Must be performed after all organization via `.pack` or `.grid` calls.
        """
        self.update_idletasks()  # Required to get accurate size information

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = self.winfo_width()
        window_height = self.winfo_height()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(newGeometry=f"+{x}+{y}")
