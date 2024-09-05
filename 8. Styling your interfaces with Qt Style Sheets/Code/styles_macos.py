# def styleDeleteButton():
#     return """
#         QPushButton {
#             background-color: qlineargradient(
#                 x1: 0, y1: 0, x2: 0, y2: 1,
#                 stop: 0 #FF6B6B, stop: 1 #FF3B30
#             ); /* Enhanced macOS red gradient */
#             color: white;
#             border-radius: 8px; /* Rounded corners */
#             border: 1px solid #D1D1D1;
#             padding: 7px 20px; /* Slightly more padding for a premium feel */
#             font-size: 14px;
#             min-height: 35px;
#         }
#         QPushButton:hover {
#             background-color: qlineargradient(
#                 x1: 0, y1: 0, x2: 0, y2: 1,
#                 stop: 0 #FF8787, stop: 1 #FF5A49
#             );
#         }
#         QPushButton:pressed {
#             background-color: qlineargradient(
#                 x1: 0, y1: 0, x2: 0, y2: 1,
#                 stop: 0 #E54444, stop: 1 #CC302F
#             );
#         }
#         """

# def styleSaveButton():
#     return """
#         QPushButton {
#             background-color: qlineargradient(
#                 x1: 0, y1: 0, x2: 0, y2: 1,
#                 stop: 0 #4CD964, stop: 1 #34C759
#             ); /* Enhanced macOS green gradient */
#             color: white;
#             border-radius: 8px;
#             border: 1px solid #D1D1D1;
#             padding: 7px 20px;
#             font-size: 14px;
#             min-height: 35px;
#         }
#         QPushButton:hover {
#             background-color: qlineargradient(
#                 x1: 0, y1: 0, x2: 0, y2: 1,
#                 stop: 0 #76E191, stop: 1 #5BD672
#             );
#         }
#         QPushButton:pressed {
#             background-color: qlineargradient(
#                 x1: 0, y1: 0, x2: 0, y2: 1,
#                 stop: 0 #389E46, stop: 1 #2E8940
#             );
#         }
#         """

def styleDeleteButton():
    return """
        QPushButton {
            background-color: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #FF6B6B, stop: 1 #FF3B30
            ); /* Enhanced macOS red gradient */
            color: white;
            border-radius: 8px; /* Rounded corners */
            border: 1px solid #D1D1D1;
            padding: 7px 20px; /* Slightly more padding for a premium feel */
            font-size: 14px;
            min-height: 35px;
            font-weight: normal;
        }
        QPushButton:hover {
            background-color: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #FF8787, stop: 1 #FF5A49
            );
            font-size: 15px; /* Increase font size on hover */
            font-weight: bold; /* Optionally make it bold for more emphasis */
        }
        QPushButton:pressed {
            background-color: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #E54444, stop: 1 #CC302F
            );
            font-size: 14px; /* Reset to original size when pressed */
            font-weight: normal;
        }
        """

def styleSaveButton():
    return """
        QPushButton {
            background-color: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #4CD964, stop: 1 #34C759
            ); /* Enhanced macOS green gradient */
            color: white;
            border-radius: 8px;
            border: 1px solid #D1D1D1;
            padding: 7px 20px;
            font-size: 14px;
            min-height: 35px;
            font-weight: normal;
        }
        QPushButton:hover {
            background-color: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #76E191, stop: 1 #5BD672
            );
            font-size: 15px; /* Increase font size on hover */
            font-weight: bold;
        }
        QPushButton:pressed {
            background-color: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #389E46, stop: 1 #2E8940
            );
            font-size: 14px; /* Reset to original size when pressed */
            font-weight: normal;
        }
        """



def styleRadioButtons(dark=False):
    if dark:
        return """
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border-radius: 8px;
                border: 2px solid #3A3A3A;
                background-color: #FF3B30;
            }
            QRadioButton::indicator:checked {
                background-color: #FF615D;
                border: 2px solid #FF3B30;
            }
            QRadioButton::indicator:unchecked {
                background-color: transparent;
                border: 2px solid #3A3A3A;
            }
            QRadioButton {
                color: #FFFFFF;
            }
        """
    else:
        return """
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border-radius: 8px;
                border: 2px solid #A9A9A9;
                background-color: #34C759;
            }
            QRadioButton::indicator:checked {
                background-color: #76E191;
                border: 2px solid #34C759;
            }
            QRadioButton::indicator:unchecked {
                background-color: transparent;
                border: 2px solid #A9A9A9;
            }
            QRadioButton {
                color: #000000;
            }
        """
