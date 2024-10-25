def fpgrowth_():
    import timeit
    import tkinter as tk
    from tkinter import scrolledtext
    from mlxtend.frequent_patterns import fpgrowth, association_rules
    import pandas as pd

    # Sample DataFrame (replace this with your own DataFrame)
    df_main = pd.read_csv("final_dataset2.csv")
    df_main.drop({'Unnamed: 0'}, axis=1, inplace=True)

    def generate_rules():
        start_time = timeit.default_timer()
        min_support = float(min_support_entry.get())
        min_threshold = float(min_threshold_entry.get())
        frequent_itemsets = fpgrowth(df_main, min_support=min_support, use_colnames=True)
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_threshold)
        
        # Convert association rules to DataFrame
        rules_df = pd.DataFrame(rules)
        
        # Format DataFrame for better display
        rules_df['antecedents'] = rules_df['antecedents'].apply(lambda x: list(x))
        rules_df['consequents'] = rules_df['consequents'].apply(lambda x: list(x))
        
        # Clear previous output
        output_text.delete(1.0, tk.END)
        
        # Display DataFrame in text area
        output_text.insert(tk.END, rules_df.to_string(index=False))
        
        # Add horizontal scrollbar
        output_text.config(wrap=tk.NONE)
        horizontal_scrollbar = tk.Scrollbar(output_text_frame, orient="horizontal", command=output_text.xview)
        horizontal_scrollbar.pack(side="bottom", fill="x")
        output_text.config(xscrollcommand=horizontal_scrollbar.set)

        execution_time_label.config(text=f"Execution Time: {timeit.default_timer() - start_time:.4f} seconds")

    def generate_frequent_itemsets():
        start_time = timeit.default_timer()
        min_support = float(min_support_entry.get())
        frequent_itemsets = fpgrowth(df_main, min_support=min_support, use_colnames=True)
        output_text.delete(1.0, tk.END)  # Clear previous output
        frequent_itemsets_df = pd.DataFrame(frequent_itemsets)
        output_text.insert(tk.END, frequent_itemsets_df)
        execution_time_label.config(text=f"Execution Time: {timeit.default_timer() - start_time:.4f} seconds")

    # Create the main window
    window = tk.Tk()
    window.title("Association Rule Mining using FP-Growth")
    window.geometry('800x650')

    # Add labels and entry fields
    tk.Label(window, text="Min Support:").place(relx=0.25, rely=0.1, anchor=tk.CENTER)
    min_support_entry = tk.Entry(window)
    min_support_entry.place(relx=0.75, rely=0.1, anchor=tk.CENTER)

    tk.Label(window, text="Min Threshold:").place(relx=0.25, rely=0.2, anchor=tk.CENTER)
    min_threshold_entry = tk.Entry(window)
    min_threshold_entry.place(relx=0.75, rely=0.2, anchor=tk.CENTER)

    # Add buttons
    generate_frequent_itemsets_button = tk.Button(window, text="Generate Frequent Itemsets", command=generate_frequent_itemsets)
    generate_frequent_itemsets_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    generate_rules_button = tk.Button(window, text="Generate Association Rules", command=generate_rules)
    generate_rules_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    # Add text area for output with scroll bars
    output_text_frame = tk.Frame(window)
    output_text_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER, relwidth=0.9, relheight=0.3)
    output_text = scrolledtext.ScrolledText(output_text_frame, wrap=tk.WORD)
    output_text.pack(expand=True, fill='both')

    # Add label for execution time
    execution_time_label = tk.Label(window, text="Execution Time: ", font=('Arial', 10))
    execution_time_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    # Start the GUI
    window.mainloop()
