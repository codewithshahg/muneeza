import pyjokes


PROMPT: str = "What do you want? "
SORRY: str = "Sorry I only tell jokes."

def main():
  
    user_input = input(PROMPT)
    user_input = user_input.strip().lower()
    
    if "joke" in user_input:
        print(pyjokes.get_joke())
    else:
        print(SORRY)

if __name__ == "__main__":
    main()