from groq import generate_response

def run_activity():
    category = input("Enter a category (e.g., fruit,city,animal): ").strip()
    item = input(f"Enter a specific {category}: ").strip()

    print("\n--- Zero-Shot ----")
    zero_prompt = f"Is {item} a {category}? Answer yes or no."
    print(f"Prompt: {zero_prompt}") 
    print("Response:", generate_response(zero_prompt, temperature=0.3, max_tokens=1024))

    print("\n--- One-Shot --- ")
    one_prompt = f"""Determine if the item belongs to the category. Example:
    Category: fruit
    Item: apple
    Answer: yes, apple is a fruit.
    
    Now you try:
    Category: {category}
    Item: {item}
    Answer:"""
    print("Response:", generate_response(one_prompt, temperature=0.3, max_tokens=1024))

    print("\n--- Few-Shot ---")
    few_prompt = f"""Determine if the item belongs to the category. Examples:
    Category: fruit
    Item: apple
    Answer: yes, apple is a fruit.

    Category: city
    Item: Paris
    Answer: yes, Paris is a city.
    
    Now you try:
    Category: {category}
    Item: {item}
    Answer:"""
    print("Response:", generate_response(few_prompt, temperature=0.3, max_tokens=1024))

    print("\n--- Creative-Few-Shot ---")
    creative_prompt = f"""Write a one-sentence story about the give word.
Example:
Word: moon
Story: The moon danced winked at the lovers as they shared their first kiss.

Example:
Word: ocean
Story: The ocean whispered secrets to the shore as the sun

Word: {item}
Story:"""
    print("Response:", generate_response(creative_prompt, temperature=0.7, max_tokens=1024))

    print("\n --- Reflection Questions ---")
    print("1) How did the response differ between each approach?")
    print("2) Which approach gave the most helpful or creative response?")
    print("3) How did examples in few-shot prompts guide the output?")
    print("4) How could you apply these techniques to your own tasks?")

if __name__ == "__main__":
    run_activity()
    