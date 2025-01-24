from qtpy import QtWidgets, QtGui


class ProjectDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        # Set up main window properties
        self.setWindowTitle("Project")
        self.setGeometry(0, 0, 1202, 697)

        # Create main layout
        main_layout = QtWidgets.QVBoxLayout(self)

        # --- Create tab widget ---
        self.tab_widget = QtWidgets.QTabWidget(self)
        main_layout.addWidget(self.tab_widget)

        # --- Information tab ---
        self.create_information_tab()

        # --- Ethogram tab ---
        self.create_ethogram_tab()

        # --- Subjects tab ---
        self.create_subjects_tab()

        # --- Independent variables tab ---
        self.create_independent_variables_tab()

        # --- Behaviors coding map tab ---
        self.create_behaviors_coding_map_tab()

        # --- Time converters tab ---
        self.create_time_converters_tab()

        # --- Buttons ---
        button_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(button_layout)

        button_layout.addStretch()  # Add spacer to push buttons to the right

        self.pb_cancel = QtWidgets.QPushButton("Cancel", self)
        button_layout.addWidget(self.pb_cancel)

        self.pb_ok = QtWidgets.QPushButton("OK", self)
        button_layout.addWidget(self.pb_ok)

    def create_information_tab(self):
        info_tab = QtWidgets.QWidget()
        self.tab_widget.addTab(info_tab, "Information")

        layout = QtWidgets.QVBoxLayout(info_tab)

        # Project name
        layout.addLayout(self.create_labeled_widget(
            "Project name:", QtWidgets.QLineEdit()))

        # Project file path
        self.lb_project_file_path = QtWidgets.QLabel("Project file path:")
        layout.addWidget(self.lb_project_file_path)

        # Project date and time
        date_layout = QtWidgets.QHBoxLayout()
        date_layout.addWidget(QtWidgets.QLabel("Project date and time:"))
        self.dte_date = QtWidgets.QDateTimeEdit()
        self.dte_date.setDisplayFormat("yyyy-MM-dd hh:mm")
        self.dte_date.setCalendarPopup(True)
        date_layout.addWidget(self.dte_date)
        date_layout.addStretch()  # Add spacer to push the date time edit to the left
        layout.addLayout(date_layout)

        # Project description
        layout.addWidget(QtWidgets.QLabel("Project description:"))
        self.te_description = QtWidgets.QPlainTextEdit()
        layout.addWidget(self.te_description)

        # Project time format
        time_format_layout = QtWidgets.QHBoxLayout()
        time_format_layout.addWidget(QtWidgets.QLabel("Project time format:"))
        self.rb_seconds = QtWidgets.QRadioButton("seconds", checked=True)
        time_format_layout.addWidget(self.rb_seconds)
        self.rb_hms = QtWidgets.QRadioButton("hh:mm:ss.mss")
        time_format_layout.addWidget(self.rb_hms)
        time_format_layout.addStretch()
        layout.addLayout(time_format_layout)

        # Project format version
        self.lb_project_format_version = QtWidgets.QLabel(
            "Project format version:")
        layout.addWidget(self.lb_project_format_version)

    def create_ethogram_tab(self):
        ethogram_tab = QtWidgets.QWidget()
        self.tab_widget.addTab(ethogram_tab, "Ethogram")

        layout = QtWidgets.QVBoxLayout(ethogram_tab)

        # Behaviors table and buttons
        table_button_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(table_button_layout)

        self.tw_behaviors = QtWidgets.QTableWidget()
        self.tw_behaviors.setColumnCount(9)
        self.tw_behaviors.setHorizontalHeaderLabels(
            [
                "Behavior type",
                "Key",
                "Code",
                "Description",
                "Color",
                "Category",
                "Modifiers",
                "Exclusion",
                "Modifiers coding map",
            ]
        )
        self.tw_behaviors.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tw_behaviors.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        table_button_layout.addWidget(self.tw_behaviors)

        button_layout = QtWidgets.QVBoxLayout()
        table_button_layout.addLayout(button_layout)
        button_layout.addWidget(QtWidgets.QPushButton("Behavior"))
        button_layout.addWidget(QtWidgets.QPushButton("Import ethogram"))
        button_layout.addWidget(QtWidgets.QPushButton("Behavioral categories"))
        button_layout.addStretch()
        button_layout.addWidget(QtWidgets.QPushButton("Exclusion matrix"))
        button_layout.addWidget(QtWidgets.QPushButton("Export ethogram"))

        self.lb_observations_state = QtWidgets.QLabel("TextLabel")
        layout.addWidget(self.lb_observations_state)

    def create_subjects_tab(self):
        subjects_tab = QtWidgets.QWidget()
        self.tab_widget.addTab(subjects_tab, "Subjects")

        layout = QtWidgets.QVBoxLayout(subjects_tab)

        # Subjects table and buttons
        table_button_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(table_button_layout)

        self.tw_subjects = QtWidgets.QTableWidget()
        self.tw_subjects.setColumnCount(3)
        self.tw_subjects.setHorizontalHeaderLabels(
            ["Key", "Subject name", "Description"]
        )
        self.tw_subjects.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tw_subjects.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        table_button_layout.addWidget(self.tw_subjects)

        button_layout = QtWidgets.QVBoxLayout()
        table_button_layout.addLayout(button_layout)
        button_layout.addWidget(QtWidgets.QPushButton("Subjects"))
        button_layout.addWidget(QtWidgets.QPushButton("Import subjects"))
        button_layout.addStretch()
        button_layout.addWidget(QtWidgets.QPushButton("Export subjects"))

        self.lb_subjects_state = QtWidgets.QLabel("TextLabel")
        layout.addWidget(self.lb_subjects_state)

    def create_independent_variables_tab(self):
        variables_tab = QtWidgets.QWidget()
        self.tab_widget.addTab(variables_tab, "Independent variables")

        layout = QtWidgets.QHBoxLayout(variables_tab)

        table_input_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(table_input_layout)

        # Variables table and input fields
        table_layout = QtWidgets.QVBoxLayout()
        table_input_layout.addLayout(table_layout)

        self.tw_variables = QtWidgets.QTableWidget()
        self.tw_variables.setColumnCount(5)
        self.tw_variables.setHorizontalHeaderLabels(
            [
                "Label",
                "Description",
                "Type",
                "Predefined value",
                "Set of values",
            ]
        )
        self.tw_variables.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_variables.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection
        )
        self.tw_variables.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        table_layout.addWidget(self.tw_variables)

        table_layout.addLayout(self.create_labeled_widget(
            "Label:", QtWidgets.QLineEdit()))
        table_layout.addLayout(
            self.create_labeled_widget("Description:", QtWidgets.QLineEdit())
        )

        type_layout = QtWidgets.QHBoxLayout()
        type_layout.addWidget(QtWidgets.QLabel("Type:"))
        self.cb_type = QtWidgets.QComboBox()
        type_layout.addWidget(self.cb_type)
        type_layout.addStretch()
        table_layout.addLayout(type_layout)

        table_layout.addLayout(
            self.create_labeled_widget(
                "Predefined value:", QtWidgets.QLineEdit())
        )

        date_layout = QtWidgets.QHBoxLayout()
        date_layout.addWidget(QtWidgets.QLabel("Predefined timestamp:"))
        self.dte_default_date = QtWidgets.QDateTimeEdit()
        self.dte_default_date.setDisplayFormat("yyyy-MM-dd hh:mm:ss.zzz")
        date_layout.addWidget(self.dte_default_date)
        date_layout.addStretch()
        table_layout.addLayout(date_layout)

        table_layout.addLayout(
            self.create_labeled_widget(
                "Set of values (separated by comma):", QtWidgets.QLineEdit()
            )
        )

        # Buttons
        button_layout = QtWidgets.QVBoxLayout()
        table_input_layout.addLayout(button_layout)
        button_layout.addWidget(QtWidgets.QPushButton("Add variable"))
        button_layout.addWidget(QtWidgets.QPushButton("Remove variable"))
        button_layout.addWidget(QtWidgets.QPushButton(
            "Import variables\nfrom a BORIS project"))
        button_layout.addStretch()

    def create_behaviors_coding_map_tab(self):
        coding_map_tab = QtWidgets.QWidget()
        self.tab_widget.addTab(coding_map_tab, "Behaviors coding map")

        layout = QtWidgets.QVBoxLayout(coding_map_tab)

        # Coding map table and buttons
        table_button_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(table_button_layout)

        self.tw_behav_coding_map = QtWidgets.QTableWidget()
        self.tw_behav_coding_map.setColumnCount(2)
        self.tw_behav_coding_map.setHorizontalHeaderLabels(
            ["Name", "Behavior codes"]
        )
        self.tw_behav_coding_map.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection
        )
        self.tw_behav_coding_map.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows
        )
        table_button_layout.addWidget(self.tw_behav_coding_map)

        button_layout = QtWidgets.QVBoxLayout()
        table_button_layout.addLayout(button_layout)
        button_layout.addWidget(
            QtWidgets.QPushButton("Add a behaviors coding map")
        )
        button_layout.addWidget(
            QtWidgets.QPushButton("Remove behaviors coding map")
        )
        button_layout.addStretch()

    def create_time_converters_tab(self):
        converters_tab = QtWidgets.QWidget()
        self.tab_widget.addTab(converters_tab, "Converters")

        layout = QtWidgets.QVBoxLayout(converters_tab)

        layout.addWidget(
            QtWidgets.QLabel("Time converters for external data")
        )

        # Converters table and buttons
        table_button_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(table_button_layout)

        self.tw_converters = QtWidgets.QTableWidget()
        self.tw_converters.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_converters.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tw_converters.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tw_converters.setColumnCount(3)
        self.tw_converters.setHorizontalHeaderLabels(
            ["Name", "Description", "Code"])
        table_button_layout.addWidget(self.tw_converters)

        button_layout = QtWidgets.QVBoxLayout()
        table_button_layout.addLayout(button_layout)
        button_layout.addWidget(QtWidgets.QPushButton("Add new converter"))
        button_layout.addWidget(QtWidgets.QPushButton("Modify converter"))
        button_layout.addWidget(QtWidgets.QPushButton("Delete converter"))
        button_layout.addWidget(
            QtWidgets.QPushButton("Load converters from file"))
        button_layout.addWidget(QtWidgets.QPushButton(
            "Load converters from BORIS repository"))
        button_layout.addStretch()

        layout.addLayout(self.create_labeled_widget(
            "Name:", QtWidgets.QLineEdit()))
        layout.addLayout(
            self.create_labeled_widget("Description:", QtWidgets.QLineEdit())
        )

        code_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(code_layout)

        code_label_layout = QtWidgets.QVBoxLayout()
        code_layout.addLayout(code_label_layout)
        code_label_layout.addWidget(QtWidgets.QLabel("Python code"))
        code_label_layout.addWidget(QtWidgets.QPushButton("Help"))
        code_label_layout.addStretch()

        self.pte_code = QtWidgets.QPlainTextEdit()
        self.pte_code.setFont(QtGui.QFont("Monospace"))
        code_layout.addWidget(self.pte_code)

        code_button_layout = QtWidgets.QVBoxLayout()
        code_layout.addLayout(code_button_layout)
        code_button_layout.addWidget(QtWidgets.QPushButton("Save converter"))
        code_button_layout.addWidget(QtWidgets.QPushButton("Cancel"))
        code_button_layout.addStretch()

    def create_labeled_widget(self, label_text, widget):
        layout = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel(label_text)
        label.setMinimumWidth(120)
        layout.addWidget(label)
        layout.addWidget(widget)
        layout.addStretch()
        return layout


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    from project_dialog import ProjectDialog

    app = QApplication([])
    dialog = ProjectDialog()
    dialog.show()
    app.exec_()
