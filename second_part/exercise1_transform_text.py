"""
* Created By Miguel Gemio

* Date: 10/09/22
* time: 12:00
* Project Name: Lab 2 Exercise - Transform strings

"""

# * For each step you will be presented with the goal for the step, 
# * followed by an empty cell. Enter your Python into the cell and run it.

# Declare the value text
text =  "Interesting facts about the Moon. The Moon is Earth's only" \
        "satellite. There are several interesting facts about the Moon" \
        "and how it affects life here on Earth. On average, the Moon " \
        "moves 4cm away from the Earth every year. This yearly drift is "\
        "not significant enough to cause immediate effects on Earth. " \
        "The highest daylight temperature of the Moon is 127 C."

print(text, end="\n\n")
        
# Separating the paragraph into sentences
sentences = text.split(". ")
print(sentences, end="\n\n")

# Find keywords
for sentence in sentences:
    if "temperature" in sentence:
        print(sentence, end="\n\n")