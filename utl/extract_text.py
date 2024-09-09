def extract_figure_info(paper_name: str, file_name: str, file_path: str):
    url = 'http://192.168.23.4:8080'  # replace with your URL
    # file_path = './single_example/example.pdf'  # replace with your file path

    with open(file_path, 'rb') as file:
        files = {'file': file}

        response = requests.post(url, files=files)

    try:
        text_data = json.loads(response.text)

        text_paragraphs = text_data["pdf_parse"]["body_text"]
        paper_text = ''
        for item in text_paragraphs:
            paper_text += item["text"]
        
        print(paper_text)
        return paper_text
    except Exception as e:
        print(f"An error occurred while processing an article: {str(e)}") 
        return "error"         