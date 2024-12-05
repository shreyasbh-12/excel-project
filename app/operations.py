import io
from flask import request
from flask_restful import Resource
import pandas as pd


class TransformData(Resource):

    def post(self):

        # Check if a file is provided
        if 'file' not in request.files:
            return {"message": "No file part in the request"}, 400

        file = request.files['file']

        # Check if the file is a CSV
        if file.filename == '' or not file.filename.endswith('.csv'):
            return {"message": "Invalid file type. Please upload a CSV file."}, 400

        try:
            # Read CSV directly from the uploaded file
            df = pd.read_csv(file)

             # Get the number of rows
            row_count = len(df)

            # # Convert DataFrame to JSON
            # data = df.to_dict(orient='records')

            # Define the maximum number of rows per split
            max_rows = 500000
            dfs = []

            # Split the DataFrame
            for i in range(0, len(df), max_rows):
                split_df = df.iloc[i:i + max_rows]
                dfs.append(split_df)

            # Save each split DataFrame to an in-memory Excel file
            excel_files = []
            for i, split_df in enumerate(dfs):
                output = io.BytesIO()
                split_df.to_excel(output, index=False, engine='openpyxl')
                output.seek(0)
                excel_files.append({
                    "filename": f"splitted-data-{i+1}.xlsx",
                    "data": output.read()
                })
                print(f"df {i+1} = {len(split_df)}")

            # Return the filenames of the Excel files as a response
            return {
                "message": "DataFrames successfully split and saved to Excel files.",
                "files": [file["filename"] for file in excel_files],
                "split_counts": [len(split_df) for split_df in dfs]
            }, 200


            # return {
            #     "row_count": row_count,
            #     # "data": data
            # }, 200
        
        except Exception as e:
            return {"message": f"An error occurred while processing the file: {str(e)}"}, 500