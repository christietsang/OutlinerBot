import os
import openai

OPENAI_API_KEY = "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"
OPENAI_ORGANIZATION = "org-JXuF0c8m0LBGctd5KgIg1BN1"


def answer_question(documents, question):
    openai.organization = OPENAI_ORGANIZATION
    openai.api_key = OPENAI_API_KEY
    sample_outline = """Course Credits 5
    Minimum Passing Grade 50%
    Start Date January 04, 2022
    End Date April 22, 2022
    Total Hours 75
    Total Weeks 15
    Hours/Weeks 5
    Criteria % Comments
    Weekly quizzes 10 Short in-lab and in-class quizzes and coding activities
    Weekly labs 30 Weekly time-restricted programming exercises"""

    sample_questions = [["What grade do I need to pass this course?", "A minimum of 50%"],
                        ["What is the start date of this class?", "January 04, 2020"],
                        ["How much are the labs worth for this class?", "30%"]]

    result = openai.Answer.create(
        search_model="davinci",
        model="davinci",
        question=question,
        documents=documents,
        examples_context=sample_outline,
        examples=sample_questions,
        max_tokens=200,
        stop=["\n", "<|endoftext|>"],
    )

    print(result)


def main():

    with open("course_outline.txt") as text_file:
        course_outline = text_file.read()
    with open("course_outline_2.txt") as text_file:
        course_outline_2 = text_file.read()
    with open("course_outline_3.txt") as text_file:
        course_outline_3 = text_file.read()
    documents = [course_outline, course_outline_2, course_outline_3]
    question = "is there a the midterms for comms 2"
    answer_question(documents, question)


if __name__ == '__main__':
    main()
