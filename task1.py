"""
Exercise 1 (Factory Pattern - DocumentFactory):
You are working on a project that requires creating different types of documents.
Implement a function-based Factory pattern to create a Document factory that can
produce instances of Resume and CoverLetter classes. Both Resume and CoverLetter
should be implemented as functions that return instances of the respective classes.
The Document factory should take a document_type parameter and return the
corresponding document function.
Instructions:
Implement the create_resume() function that takes a name and experience parameter
and returns an instance of the Resume class initialized with the provided name and experience.
Implement the create_cover_letter() function that takes a name and company parameter
and returns an instance of the CoverLetter class initialized with the provided name and company.
Implement the DocumentFactory() function that takes a document_type parameter.
Inside the factory function, use a dictionary mapping the document types to their
corresponding document functions (create_resume and create_cover_letter).
The DocumentFactory() function should return the document function based
on the provided document_type. If the document_type is not found in the dictionary,
the factory should raise a ValueError.
Test your implementation by creating instances of both a resume and a cover
letter using the DocumentFactory.

Test the implementation
factory = DocumentFactory("resume")
resume = factory("John Doe", "5 years of experience")

factory = DocumentFactory("cover_letter")
cover_letter = factory("John Doe", "ABC Company")

print(resume.name, resume.experience) # Output: John Doe 5 years of experience
print(cover_letter.name, cover_letter.company) # Output: John Doe ABC Company

"""

# Solution
# an implementation of the Factory pattern for creating
# different types of documents using function-based approach

class Resume:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

class CoverLetter:
    def __init__(self, name, company):
        self.name = name
        self.company = company

def create_resume(name, experience):
    return Resume(name, experience)

def create_cover_letter(name, company):
    return CoverLetter(name, company)

def DocumentFactory(document_type):
    document_functions = {
        "resume": create_resume,
        "cover_letter": create_cover_letter
    }

    if document_type in document_functions:
        return document_functions[document_type]
    else:
        raise ValueError("Invalid document type")

# Test the implementation
factory = DocumentFactory("resume")
resume = factory("John Doe", "5 years of experience")

factory = DocumentFactory("cover_letter")
cover_letter = factory("John Doe", "ABC Company")

print(resume.name, resume.experience)  # Output: John Doe 5 years of experience
print(cover_letter.name, cover_letter.company)  # Output: John Doe ABC Company

