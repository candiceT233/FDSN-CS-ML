

def write_combined_df_to_excel(combined_df, output_file):
    # Write the combined dataframe to an Excel file
    combined_df.to_excel(output_file, index=False)
    print(f"Combined data written to {output_file}.")
