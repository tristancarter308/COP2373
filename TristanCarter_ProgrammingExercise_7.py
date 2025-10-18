import re

#Get user paragraph
def get_paragraph():
    paragraph = input("Enter your paragraph: ")
    return paragraph

#Extract and count sentences
def count_sentences(paragraph):

    sentences = re.split(r'(?<=[.!?])\s+', paragraph)
    sentences = [s.strip() for s in sentences if s.strip()]

    return sentences, len(sentences)

#Display individual sentences and how many there are
if __name__ == "__main__":

    user_paragraph = get_paragraph()
    individual_sentences, sentence_count = count_sentences(user_paragraph)

    print("\nSentences:")
    for i, sentence in enumerate(individual_sentences):
        print(f"- {sentence}")

    print(f"\nThere are {sentence_count} sentences.")