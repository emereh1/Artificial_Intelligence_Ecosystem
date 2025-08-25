# Mental Health Check-in Bot

## Part 1: Initial Project Ideas

### 1. Project Idea 1: Personal Fitness Advisor
- **Description:** A system that recommends personalized workout routines based on user input (fitness level, available equipment, etc.).
- **Rule-Based Approach:**  
  - The system uses predefined rules to recommend workouts (e.g., strength training, cardio) based on the user's goal and equipment.
  - It adjusts workout difficulty based on the user's fitness level (beginner, intermediate, advanced).

### 2. Project Idea 2: Personalized Study Planner
- **Description:** A system that creates a customized study plan for users, considering deadlines, exam schedules, and learning preferences.
- **Rule-Based Approach:**  
  - The system breaks down study tasks based on the user's input and gives recommendations for study techniques (active recall, spaced repetition).
  - The system can adapt to the user’s stress levels and workload, offering tips like relaxation exercises or breaking up study sessions.

### 3. Project Idea 3: Mental Health Check-in Bot
- **Description:** A bot that helps users track their mood and provides personalized recommendations to improve their mental well-being.
- **Rule-Based Approach:**  
  - The system checks the user's input for mood keywords (e.g., "happy", "stressed", "sad") and provides tailored responses (e.g., relaxation exercises, talking to someone, or suggesting professional help).
  - The bot offers consistent emotional support with gentle nudges for self-care based on the user’s reported mood.
  - New functionality: **View mood history** and **delete mood history** for better tracking and user control.

### **Chosen Idea:** Mental Health Check-in Bot  
**Justification:** I chose this project because mental health is an important topic, and this bot can provide users with daily support. It’s highly relevant in today’s world, where mental well-being is more recognized, and it’s an opportunity to create a system that directly helps people.

---

## Part 2: Rules/Logic for the Chosen System

The **Mental Health Check-in Bot** system will follow these rules:

1. **Happy Mood Rule:**  
   - **IF** the user reports feeling happy → **Suggest** maintaining a positive mood by engaging in something fun, like a hobby or time with loved ones.

2. **Stressed or Anxious Mood Rule:**  
   - **IF** the user reports feeling stressed or anxious → **Suggest** relaxation techniques such as deep breathing exercises or mindfulness activities.

3. **Sad or Overwhelmed Mood Rule:**  
   - **IF** the user reports feeling sad or overwhelmed → **Suggest** journaling or talking with a friend or family member.

4. **Anger Management Rule:**  
   - **IF** the user reports feeling angry → **Suggest** physical activities like walking or stretching to help release built-up tension.

5. **Professional Help Suggestion:**  
   - **IF** the user repeatedly reports negative emotions over time → **Recommend** seeking professional support from a therapist or counselor.

---

## Part 3: Sample Input and Output

**Sample input and output for the system:**

**Input:**  
"I feel stressed today."  
**Output:**  
"Try some deep breathing exercises: Inhale for 4 seconds, hold for 4 seconds, and exhale for 4 seconds."

**Input:**  
"I'm feeling happy!"  
**Output:**  
"That's awesome! Keep up the good vibes! How about treating yourself to something fun today?"

**Input:**  
"I'm feeling sad."  
**Output:**  
"It might help to talk it out or write down how you’re feeling. Would you like to talk more about it?"

---

## Part 4: Reflection

### Project Overview:  
This project involved designing a supportive, rule-based system to check in with users about their mental health and offer personalized recommendations. The system provides emotional support by responding to mood-related inputs and offering tailored suggestions like relaxation techniques or physical activities. It now includes the ability to **view mood history** and **delete mood history**, empowering users with more control.

### Challenges:  
- **Handling Various Emotional States:**  
  Creating rules that covered a wide range of emotions (happiness, stress, anger) while maintaining a tone of support was challenging.
- **Consistency in Offering Support:**  
  Ensuring that the bot's responses remained supportive and empathetic was key, which required careful thought in wording each response.
- **Ensuring User Control:**  
  Adding the ability to view and delete mood history required careful handling of user data and additional commands.

---