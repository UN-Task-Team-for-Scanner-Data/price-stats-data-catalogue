from bs4 import BeautifulSoup
import os

def update_index():
    """
    Update the main index.html - which is the home page of the catalogue:
    - Make the search on datasets
    - Fix the reference to the catalogue home (top left)
    - Change datacontract.com reference to reproducibility project site
    """
    
    # Define the path to your HTML file
    file_path = '_site/index.html'

    # Open and read the HTML file
    with open(file_path, 'r') as file:
        html_content = file.read()

    # Create a BeautifulSoup object to parse the content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Change the main text
    h2_tag_main_title = soup.find('h2', class_="text-2xl")
    h2_tag_main_title.string = '\n              Price Statistics Open Data Catalogue'

    # Modify the Catalogue home link
    a_tag_top_left = soup.find('a', class_="text-xl text-gray-900 font-semibold")
    a_tag_top_left.string = '\n              Catalogue Home\n            '
    a_tag_top_left['href'] = "https://un-task-team-for-scanner-data.github.io/price-stats-data-catalogue/"
    a_tag_top_left

    # Modify the reference to the project
    a_tag_top_right = soup.find('a', class_="text-sky-500 hover:text-gray-700 text-sm font-semibold")
    # <a class="text-sky-500 hover:text-gray-700 text-sm font-semibold" href="https://datacontract.com" target="_blank">datacontract.com</a>
    a_tag_top_right.string = 'Price Statistics Reproducibility Project'
    a_tag_top_right['href'] = "https://un-task-team-for-scanner-data.github.io/reproducibility-project/docs/"

    # Save the modified HTML back to the file
    with open(file_path, 'w') as file:
        file.write(str(soup))

def update_dataset(_path):
    """
    Update each dataset's html
    """
    # Open and read the HTML file
    with open(_path, 'r') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')

    # Change the main text
    h2_tag_main_title = soup.find('h2', class_="text-2xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight")
    h2_tag_main_title.string = '\n              Dataset'

    # Modify the Catalogue home link
    a_tag_top_left = soup.find('a', class_="text-xl text-gray-900 font-semibold")
    a_tag_top_left.string = '\n              <- Back to Catalogue Home\n            '
    a_tag_top_left['href'] = "https://un-task-team-for-scanner-data.github.io/price-stats-data-catalogue/"
    a_tag_top_left

    # Modify the reference to the project
    a_tag_top_right = soup.find('a', class_="text-sky-500 hover:text-gray-700 text-sm font-semibold")
    # <a class="text-sky-500 hover:text-gray-700 text-sm font-semibold" href="https://datacontract.com" target="_blank">datacontract.com</a>
    a_tag_top_right.string = 'Price Statistics Reproducibility Project'
    a_tag_top_right['href'] = "https://un-task-team-for-scanner-data.github.io/reproducibility-project/docs/"

    # Save the modified HTML back to the file
    with open(_path, 'w') as file:
        file.write(str(soup))


if __name__ == "__main__":
    update_index()
    files = os.listdir('_site/')
    files.remove('index.html')
    for file in files:
        update_dataset('_site/'+file)