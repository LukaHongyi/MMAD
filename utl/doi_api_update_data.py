import requests

# Function of getting paper metadata by calling crossref server
def get_details_from_doi(doi):
    api_url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        authors_list = []
        authors_sequence = []
        license_urls = []
        subjects = []

        if 'author' in data['message']:
            for author in data['message']['author']:
                given_name = author.get('given', '')
                family_name = author.get('family', '')
                author_name = f"{given_name} {family_name}"
                authors_list.append(author_name)
                authors_sequence.append((author['sequence'], author_name))

        if 'license' in data['message']:
            for license_info in data['message']['license']:
                license_urls.append(license_info['URL'])

        if 'subject' in data['message']:
            for subject in data['message']['subject']:
                subjects.append(subject)

        if 'abstract' in data['message']:
            abstract = data['message']['abstract']
        else:
            abstract = ""
        return authors_list, authors_sequence, license_urls, subjects, abstract
    else:
        print("Failed to retrieve DOI information.")
        return [], [], [], [],""
