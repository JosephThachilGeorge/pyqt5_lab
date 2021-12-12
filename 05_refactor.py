# Import stuff
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtWidgets import QBoxLayout, QWidget

# Use a __main__ guard, you never know.
if __name__ == '__main__':
    # Create our application -- MUST be done first.
    app = QApplication(sys.argv)

    # BUILD THE INTERFACE...

    app.exec_()

#
# Laboratory exercises:
#
# 1. In this exercise you should implement a simple application that
# displays one or more buttons with the text "Clicks: N", where 'N' is
# the number of times *that* button has been clicked.
#
# You should think carefully about the design of this
# application. Where should the click counter be? Where should the
# increment functionality for button press be located? Think in terms
# of inversion of control, separation of concerns, and customization
# via inheritance.
#
# Another hint: the 'text()' method of a button gives the text of the
# label displayed, and to format a string with a number in it you can
# use something like:
#
#  'Clicks: {}'.format(num_clicks)
#
# or (since Python 3):
#
#  f'Clicks{num_clicks}'
#
