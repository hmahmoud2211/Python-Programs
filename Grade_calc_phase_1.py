import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
gradebook = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 84],
    "Charlie": [79, 85, 89],
    "Diana": [95, 92, 96],
}

def calculate_statistics(gradebook):

    student_averages = {}
    all_grades = []

    for student, grades in gradebook.items():
        average = sum(grades) / len(grades)  
        student_averages[student] = average
        all_grades.extend(grades)

    if all_grades:
        overall_average = sum(all_grades) / len(all_grades)
    else:
        overall_average = 0

    return student_averages, overall_average

def visualize_statistics(student_averages):

    students = list(student_averages.keys())
    averages = list(student_averages.values())

    plt.bar(students, averages, color='skyblue')
    plt.xlabel("Students")
    plt.ylabel("Average Grade")
    plt.title("Student Average Grades")
    plt.ylim(0, 100) 
    plt.show()

def show_statistics():

    student_averages, overall_average = calculate_statistics(gradebook)
    stats_text = "Individual Averages:\n"

    for student, avg in student_averages.items():
        stats_text += f"{student}: {avg:.2f}\n"

    stats_text += f"\nOverall Average: {overall_average:.2f}"
    stats_label.config(text=stats_text)

def generate_chart():

    student_averages, _ = calculate_statistics(gradebook)
    visualize_statistics(student_averages)

def add_student():
    name = student_name_entry.get()
    grades_text = grades_entry.get()

    try:
        grades = list(map(int, grades_text.split(',')))
        if name and grades:
            gradebook[name] = grades
            messagebox.showinfo("Success", f"Student {name} added!")
            student_name_entry.delete(0, tk.END)
            grades_entry.delete(0, tk.END)
        else:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid name and comma-separated grades.")

root = tk.Tk()
root.title("Gradebook Statistics Visualizer")
root.geometry("500x400")

title_label = tk.Label(root, text="Gradebook Statistics Visualizer", font=("Arial", 16))
title_label.pack(pady=10)


input_frame = tk.Frame(root)
input_frame.pack(pady=10)

student_name_label = tk.Label(input_frame, text="Student Name:")
student_name_label.grid(row=0, column=0, padx=5, pady=5)

student_name_entry = tk.Entry(input_frame)
student_name_entry.grid(row=0, column=1, padx=5, pady=5)

grades_label = tk.Label(input_frame, text="Grades (comma-separated):")
grades_label.grid(row=1, column=0, padx=5, pady=5)

grades_entry = tk.Entry(input_frame)
grades_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Student", command=add_student)
add_button.grid(row=2, columnspan=2, pady=10)


stats_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
stats_label.pack(pady=10)

show_button = tk.Button(root, text="Show Statistics", command=show_statistics)
show_button.pack(pady=5)


chart_button = tk.Button(root, text="Generate Chart", command=generate_chart)
chart_button.pack(pady=5)


root.mainloop()