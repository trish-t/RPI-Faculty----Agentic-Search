"""
This file contains a class definition and methods that can be used during the scraping process to keep track of information
by faculty member.
"""

class Faculty:
    faculty_directory_page_url = None
    email = None
    personal_website = None
    phone_number = None
    office = None
    linkedIn_url = None
    youtube_url = None
    instagram_url = None

    core_department = None
    affiliated_with = None
    titles = None
    affiliated_departments_links = None

    def __init__(self, first_name, last_name, page_url):
        self.first_name = first_name
        self.last_name = last_name
        self.faculty_directory_page_url = page_url
        self.affiliated_with = []
        self.titles = []
        self.affiliated_departments_links = []

        def set_email(self, email):
            self.email = email

        def set_personal_website(self, url):
            self.personal_website = url

        def set_phone_number(self, phone):
            self.phone_number = phone

        def set_office(self, office):
            self.office = office

        def set_linkedin_url(self, url):
            self.linkedIn_url = url

        def set_youtube_url(self, url):
            self.youtube_url = url

        def set_instagram_url(self, url):
            self.instagram_url = url

        def set_core_department(self, dept):
            self.core_department = dept

        def add_affiliation(self, affiliation):
            affiliation = affiliation.strip()
            if affiliation and affiliation not in self.affiliated_with:
                self.affiliated_with.append(affiliation)

        def add_title(self, title):
            title = title.strip()
            if title and title not in self.titles:
                self.titles.append(title)

    