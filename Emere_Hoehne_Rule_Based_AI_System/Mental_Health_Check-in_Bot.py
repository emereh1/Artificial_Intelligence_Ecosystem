import datetime
import os

# Function to offer relaxation techniques
def relaxation_techniques():
    techniques = [
        "1. Try progressive muscle relaxation (PMR): Tense and release each muscle group in your body.",
        "2. Practice deep breathing: Inhale for 4 seconds, hold for 4, and exhale for 4.",
        "3. Listen to calming music or nature sounds.",
        "4. Try a 5-minute guided meditation (search YouTube for '5-minute meditation')."
    ]
    return "\n".join(techniques)

# Function to log user mood
def log_mood(user_mood):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("mood_log.txt", "a") as file:
            file.write(f"{current_date}: {user_mood}\n")
    except Exception as e:
        print(f"Error logging mood: {e}")

# Function to read the mood log
def read_mood_log():
    try:
        with open("mood_log.txt", "r") as file:
            print("\nMood History:\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No mood history available.")

# Function to delete mood history
def delete_mood_history():
    confirmation = input("Are you sure you want to delete the mood history? (y/n): ").lower()
    if confirmation == "y":
        try:
            os.remove("mood_log.txt")
            print("Mood history has been deleted.")
        except FileNotFoundError:
            print("No mood history file found.")
    else:
        print("Deletion canceled.")

# Function to provide mental health suggestions
def mental_health_check_in(mood):
    mood = mood.lower().strip()  # Normalize the input
    
    # Handling recognized moods
    if "happy" in mood:
        return "That's awesome! Keep up the good vibes! How about treating yourself to something fun today?"
    
    elif "stressed" in mood or "anxious" in mood:
        return f"You're not alone. Here are some relaxation techniques you can try:\n{relaxation_techniques()}"
    
    elif "sad" in mood or "overwhelmed" in mood:
        return "It might help to talk it out or write down how you’re feeling. Would you like to talk more about it?"
    
    elif "angry" in mood:
        return "Consider doing a quick physical activity, like stretching or going for a brisk walk. Let’s channel that energy!"
    
    else:
        return (
            "I don't quite understand what you mean. Here are some emotions I can help with:\n"
            "1. Happy\n2. Stressed\n3. Anxious\n4. Sad\n5. Angry\n\n"
            "Please let me know how you're feeling, and I’ll try to assist you!"
        )

# Main function to interact with the user
def main():
    print("Welcome to the Mental Health Check-in Bot!")
    print("Type 'exit' to quit, 'history' to view mood history, or 'delete history' to delete mood history.\n")
    
    while True:
        user_input = input("\nHow are you feeling today? (e.g., happy, stressed, sad, angry): ")
        
        # If the user wants to see their mood history
        if user_input.lower() == "history":
            read_mood_log()
            continue
        
        # If the user wants to delete mood history
        if user_input.lower() == "delete history":
            delete_mood_history()
            continue
        
        # If the user wants to exit, break the loop
        if user_input.lower() == "exit":
            print("\nGoodbye! Take care of yourself!\n")
            break
        
        # Log the mood entry if it’s a valid mood
        response = mental_health_check_in(user_input)
        
        # Only log recognized moods
        if "I don't quite understand what you mean" not in response:
            log_mood(user_input)
        
        # Respond based on the user's input
        print(response)

# Run the program
if __name__ == "__main__":
    main()