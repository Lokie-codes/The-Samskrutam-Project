# Define the Sanskrit to English dictionary
sanskrit_to_english = {
    "नमस्ते": "Hello",
    "कृपया": "Please",
    "धन्यवाद": "Thank you",
    "शुभ प्रभात": "Good morning",
    # Add more translations as needed
}

def sanskrit_translator(sanskrit_text):
    english_text = sanskrit_to_english.get(sanskrit_text, "Translation not found")
    return english_text

# Example usage
sanskrit_word = input("Enter a Sanskrit word or phrase: ")
translation = sanskrit_translator(sanskrit_word)
print("Translation:", translation)
