import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout

class Student:
    def __init__(self, name, roll_number, course, total_marks):
        self.name = name
        self.roll_number = roll_number
        self.course = course
        self.total_marks = total_marks
        self.next = None

class StudentRecordManagementSystem(QWidget):
    def __init__(self):
        super().__init__()

        self.head = None
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.roll_number_label = QLabel("Roll Number:")
        self.roll_number_input = QLineEdit()
        self.course_label = QLabel("Course:")
        self.course_input = QLineEdit()
        self.total_marks_label = QLabel("Total Marks:")
        self.total_marks_input = QLineEdit()
        self.create_button = QPushButton("Create Record")
        self.search_button = QPushButton("Search Record")
        self.delete_button = QPushButton("Delete Record")
        self.show_button = QPushButton("Show Records")
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Roll Number", "Course", "Total Marks"])

        self.create_button.clicked.connect(self.create_record)
        self.search_button.clicked.connect(self.search_record)
        self.delete_button.clicked.connect(self.delete_record)
        self.show_button.clicked.connect(self.show_records)

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.name_label)
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.roll_number_label)
        input_layout.addWidget(self.roll_number_input)
        input_layout.addWidget(self.course_label)
        input_layout.addWidget(self.course_input)
        input_layout.addWidget(self.total_marks_label)
        input_layout.addWidget(self.total_marks_input)
        input_layout.addWidget(self.create_button)
        input_layout.addWidget(self.search_button)
        input_layout.addWidget(self.delete_button)
        input_layout.addWidget(self.show_button)

        table_layout = QHBoxLayout()
        table_layout.addWidget(self.table)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(table_layout)

        self.setLayout(main_layout)

    def create_record(self):
        name = self.name_input.text()
        roll_number = self.roll_number_input.text()
        course = self.course_input.text()
        total_marks = self.total_marks_input.text()

        if not name or not roll_number or not course or not total_marks:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        current_node = self.head
        while current_node is not None:
            if current_node.roll_number == roll_number:
                QMessageBox.warning(self, "Error", "Record already exists.")
                return
            current_node = current_node.next

        student = Student(name, roll_number, course, total_marks)
        if self.head is None:
            self.head = student
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = student

        self.name_input.clear()
        self.roll_number_input.clear()
        self.course_input.clear()
        self.total_marks_input.clear()
        QMessageBox.information(self, "Success", "Record created successfully.")

    def search_record(self):
        roll_number = self.roll_number_input.text()

        if not roll_number:
            QMessageBox.warning(self, "Error", "Please enter a roll number.")
            return

        current_node = self.head
        while current_node is not None:
            if current_node.roll_number == roll_number:
                self.name_input.setText(current_node.name)
                self.course_input.setText(current_node.course)
                self.total_marks_input.setText(current_node.total_marks)
                return
            current_node = current_node.next

        QMessageBox.warning(self, "Error", "Record not found.")

    def delete_record(self):
        roll_number = self.roll_number_input.text()

        if not roll_number:
            QMessageBox.warning(self, "Error", "Please enter a roll number.")
            return

        if self.head is None:
            QMessageBox.warning(self, "Error", "Record not found.")
            return

        if self.head.roll_number == roll_number:
            self.head = self.head.next
            self.name_input.clear()
            self.course_input.clear()
            self.total_marks_input.clear()
            QMessageBox.information(self, "Success", "Record deleted successfully.")
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.roll_number == roll_number:
                current_node.next = current_node.next.next
                self.name_input.clear()
                self.course_input.clear()
                self.total_marks_input.clear()
                QMessageBox.information(self, "Success", "Record deleted successfully.")
                return
            current_node = current_node.next

        QMessageBox.warning(self, "Error", "Record not found.")

    def show_records(self):
        self.table.setRowCount(0)

        current_node = self.head
        while current_node is not None:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(current_node.name))
            self.table.setItem(row, 1, QTableWidgetItem(current_node.roll_number))
            self.table.setItem(row, 2, QTableWidgetItem(current_node.course))
            self.table.setItem(row, 3, QTableWidgetItem(current_node.total_marks))
            current_node = current_node.next

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Record Management System")
        self.setGeometry(100, 100, 800, 600)
        self.student_record_management_system = StudentRecordManagementSystem()
        self.setCentralWidget(self.student_record_management_system)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
