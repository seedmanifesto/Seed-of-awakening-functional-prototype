from seed_wrapper import pause_and_reflect

@pause_and_reflect
def respond(prompt):
    return "This is a reflective response."

if __name__ == "__main__":
    prompt = "What is silence?"
    print(respond(prompt))
