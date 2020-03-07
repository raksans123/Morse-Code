from translator import MorseCodeTranslator
from tkinter import Tk, Label, Text, Frame, Button, Scrollbar, IntVar
import sys

if "win" in sys.platform:
    from winsound import Beep


class App(object):
    """
Main class
    """

    __button_width = 15
    __button_height = 1
    __button_bg = "snow4"
    __button_fg = "white"
    __button_font = ("Autumn", 27)
    __button_relief = "flat"

    __inputText_height = 5

    __label_fg = "#F5F5F5"
    __label_font = ("Impact", 20)

    __outputText_height = 7

    __text_width = 50
    __text_bg = "white"
    __text_fg = "black"
    __text_font = ("Arial", 14)

    frequency = 2000

    window_title = "Morse Code Translation App"
    window_geometry = [600, 500]
    window_bg = "SteelBlue3"

    def __init__(self):

        # Create an instance of Tk and configure the window.
        self.__root = Tk()
        self.__root.geometry("{}x{}".format(*self.window_geometry))
        self.__root["bg"] = self.window_bg
        self.__root.title(self.window_title)
        self.__root.resizable(False, False)
        self.__root.focus_force()
        self.__root.bind("<Return>", self.translate)

        self.__playing = False
        self.__waitVar = IntVar()

        # Call method to build program interface.
        self.build()

    def build(self):
        """
        Method for building program interface.
        """

        # Creates a title for the entry of the text to be translated.
        Label(
            self.__root,
            bg=self.window_bg,
            font=self.__label_font,
            fg=self.__label_fg,
            text="Text:",
            pady=10
        ).pack()

        # Creates a frame to place the input field.
        input_frame = Frame(self.__root, bg=self.window_bg)
        input_frame.pack()

        # Creates a field for the user to enter the text.
        self.__inputText = Text(
            input_frame,
            width=self.__text_width,
            height=self.__inputText_height,
            bg=self.__text_bg,
            fg=self.__text_fg,
            font=self.__text_font,
            wrap="word"
        )
        self.__inputText.insert(0.0, " Enter text here...")

        # Creates a scroll bar for the input field.
        scrollbar = Scrollbar(input_frame)
        scrollbar.pack(side="right", fill="y")
        self.__inputText.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.__inputText.yview)

        self.__inputText.pack()

        # Creates field title where the translated text will be placed.
        Label(
            self.__root,
            bg=self.window_bg,
            font=self.__label_font,
            fg=self.__label_fg,
            text="Morse Code:",
            pady=10
        ).pack()

        # Creates frame to place the output field.
        output_frame = Frame(self.__root, bg=self.window_bg)
        output_frame.pack()

        # Field to place the translated text.
        self.__outputText = Text(
            output_frame,
            width=self.__text_width,
            height=self.__outputText_height,
            bg=self.__text_bg,
            fg=self.__text_fg,
            font=self.__text_font,
            wrap="word"
        )
        self.__outputText.insert(0.0, " The morse code will appear here.")

        # Creates a scroll bar for the output field.
        scrollbar = Scrollbar(output_frame)
        scrollbar.pack(side="right", fill="y")
        self.__outputText.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.__outputText.yview)

        self.__outputText.pack()

        # Creates a frame to insert the buttons.
        buttons_frame = Frame(self.__root, bg=self.window_bg, pady=20)
        buttons_frame.pack()

        # Creates a "border" for the button.
        button1_frame = Frame(buttons_frame, bg="black", padx=2, pady=2)
        button1_frame.pack(side="left")

        # Creates a button to translate the text.
        self.__button1 = Button(
            button1_frame,
            width=self.__button_width,
            height=self.__button_height,
            relief=self.__button_relief,
            bg=self.__button_bg,
            fg=self.__button_fg,
            font=self.__button_font,
            text="Translate",
            command=self.translate
        )
        self.__button1.pack()

        # If the user's OS is Windows, a button will be created
        # to reproduce the sound of the Morse code.
        if "win" in sys.platform:
            Label(buttons_frame, bg=self.window_bg, padx=5).pack(side="left")

            # Creates a "border" for the button.
            button2_frame = Frame(buttons_frame, bg="black", padx=2, pady=2)
            button2_frame.pack(side="left")

            #Creates a button to reproduce Morse code sound.
            self.__button2 = Button(
                button2_frame,
                width=self.__button_width,
                height=self.__button_height,
                relief=self.__button_relief,
                bg=self.__button_bg,
                fg=self.__button_fg,
                font=self.__button_font,
                text="Play",
                command=self.play
            )
            self.__button2.pack()

        self.__root.mainloop()

    def play(self):
        """
        Method to reproduce the sound of the Morse code.
        """

        #For playback.
        if self.__playing:
            self.__playing = False
            return

        # Gets the text of the output and checks if it is a Morse code.
        text = self.__outputText.get(0.0, "end")
        if not text or text.isspace() or not MorseCodeTranslator.isMorse(text): return

        # Informs that the morse code sound is being played.
        self.__playing = True
        self.__button2.config(text="Stop")

        # Divide text into words.
        for char in text.split(" "):

            # Gets each letter of the word.
            for l in char:

                if not self.__playing:
                    break

                # Checks whether the character is an error.
                if l == MorseCodeTranslator.errorChar:
                    continue

                # It beeps for 0.4 seconds each time it is a dot.
                if l == ".":
                    Beep(self.frequency, 400)

                # Plays a beep for 0.8 seconds if it is a dash.
                elif l == "-":
                    Beep(self.frequency, 800)

                #Wait for 2 seconds if it is the beginning of a new word.
                elif l == "/":
                    self.wait(2000)

            if not self.__playing:
                break

            # Waits 1 second.
            self.wait(1000)

        # Informs you that playback has finished.
        self.__playing = False
        self.__button2.config(text="Play")

    def translate(self, event=None):
        """
        Button method for translating text.
        """

        #Gets user input.
        text = self.__inputText.get(0.0, "end")
        if not text: return

        # Delete the text from the output field and insert the translated user's input.
        self.__outputText.delete(0.0, "end")
        self.__outputText.insert(0.0, MorseCodeTranslator.translate(text))

    def wait(self, ms):
        """
        Method to wait a while on Ms.
        """

        self.__waitVar.set(0)
        self.__root.after(ms, self.__waitVar.set, 1)
        self.__root.wait_variable(self.__waitVar)
        self.__waitVar.set(0)


if __name__ == "__main__":
    App()