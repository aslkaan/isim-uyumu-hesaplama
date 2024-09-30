import tkinter as tk
from collections import Counter
def calculate_match():
    name1 = entry_name1.get()
    name2 = entry_name2.get()
    combined_names = name1 + name2
    letter_counts = Counter(combined_names)
    result = ""
    for letter in sorted(letter_counts.keys()):
        count = letter_counts[letter]
        result += str(count)
    while len(result) < 2:
        total = int(result[0]) + int(result[-1])
        result = str(total) + result[1:-1]
    while len(result) > 2:
        total = int(result[0]) + int(result[-1])
        result = str(total) + result[1:-1]
    result_label.config(text=f"{result}%")
root = tk.Tk()
root.title("İsim Uyumu Hesaplama")
label1 = tk.Label(root, text="İlk kişinin adı:")
label1.pack()
entry_name1 = tk.Entry(root)
entry_name1.pack()
label2 = tk.Label(root, text="İkinci kişinin adı:")
label2.pack()
entry_name2 = tk.Entry(root)
entry_name2.pack()
calculate_button = tk.Button(root, text="Hesapla", command=calculate_match)
calculate_button.pack()
result_label = tk.Label(root, text="Sonuç: ")
result_label.pack()
root.mainloop()