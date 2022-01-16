import openai
import ast

# Insert API key here
OPENAI_API_KEY = "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"
OPENAI_ORGANIZATION = "org-d32asjx5v8BlNuI9aUwLDYeo"

def get_data(file_name):
    try:
        with open(file_name, errors="ignore") as text_file:
            data = text_file.read()
    except FileNotFoundError:
        print(f"\"{file_name}\" does not exist.", )
    else:
        if data[0] == "[" and data[-1] == "]":
            return ast.literal_eval(data)
        else:
            return data


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
    print(documents)
    result = openai.Answer.create(
        search_model="davinci",
        model="davinci",
        question=question,
        documents=documents,
        examples_context=sample_outline,
        examples=sample_questions,
        max_tokens=50,
        stop=["\n", "<|endoftext|>"],
    )
    print(result)

    # answer = result["answers"][0]
    # score = result["selected_documents"][0]["score"]
    # if score > 200:
    #     accuracy = "high"
    # elif score > 100:
    #     accuracy = "medium"
    # elif score > 0:
    #     accuracy = "low"
    # else:
    #     accuracy = "negative"
    #
    # if accuracy == "negative":
    #     return "Could not find an answer."
    # else:
    #     return f"{answer}\nAccuracy: {accuracy}"


def main():
    documents = get_data("course_outline.txt")
    question = "How much is the final exam worth?"
    print(answer_question([documents], question))


if __name__ == '__main__':
    main()
