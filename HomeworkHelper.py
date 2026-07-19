import google.generativeai as genai
#pip install google.generativeai


client = genai.configure(api_key="YOUR GEMINI API KEY HERE")

class System_Client():
        
        def __init__(self):
            system_instruction = self.System_Prompt()
            self.model = genai.GenerativeModel(
            model_name="gemini-3.5-flash",
            system_instruction=system_instruction
)

            self.chat = self.model.start_chat()

        
        def System_Prompt(self): #System Prompt for you to give specific work for the AI
                Sys_instruction = "You are a tutor for student who are in need of help. Explain concepts simply and clearly. Always give examples"
                Sys_Restriction = "You will not give direct Answer to the students."
                Sys_limitation = "If the student ask for a direct Answer. Simply say i Cannot fulfill the Request"
                All_Sys_promt = (f"{Sys_instruction}, {Sys_Restriction}, {Sys_limitation}")
                return All_Sys_promt

        def System_output(self):

            response = self.chat.send_message(input("You: "))
            print(response.text)



AIHelper = System_Client()

print("====================================")
print("======= Homework Helper ============")
print("====================================")

while True:
      
    AIHelper.System_output()