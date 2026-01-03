def export_data(df, filename="clean_student_data.csv"):
    df.to_csv(filename, index=False)
    print("Data Exported Successfully")
