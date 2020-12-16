from voicebot_en import *

if __name__ == "__main__":
    Welcome()

    while True:
        query = command().lower()

        if 'google' in query:
            Speak("What should I search, boss?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            Speak(f"Here is your {search} on Google.")

        if 'youtube' in query:
            Speak("What should I search, boss?")
            search = command().lower()
            url = f"https://www.youtube.com/results?search_query={search}"
            wb.get().open(url)
            Speak(f"Here is your {search} on Youtube.")

        elif 'time' in query:
            Time()
        
        elif 'exit' or 'quit' in query:
            Speak('Sana-chan have a schedule, bye bye boss!')
            quit()