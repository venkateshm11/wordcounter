class WordCounter:
    def __init__(self):
        self.text = ""
    
    def get_input(self):
        """Prompt the user to enter a sentence or paragraph."""
        self.text = input("Enter a sentence or paragraph: ").strip()
    
    def count_words(self):
        """Count the number of words in the input text."""
        if not self.text:
            return 0
        return len(self.text.split())
    
    def display_output(self, word_count):
        """Display the word count to the user."""
        print(f"The number of words in the given text is: {word_count}")
    
    def run(self):
        """Main method to run the Word Counter program."""
        self.get_input()
        if not self.text:
            print("Error: No input provided. Please enter some text.")
            return
        word_count = self.count_words()
        self.display_output(word_count)

# Create an instance of the WordCounter class and run the program
word_counter = WordCounter()
word_counter.run()
