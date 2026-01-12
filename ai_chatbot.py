import tkinter as tk
name = "karthikeya"
phono = "9182858276"
age = "20"
birth = "17th sep 2004"

#  main Logic
def bot_reply(user):
    user = user.lower()

    if user in ("exit", "bye","close"):
        return "Have a nice day, goodbye!"

    elif "hi" in user or "hello" in user:
        return "Hi! How can I help you?"

    elif "how are you" in user:
        return "I am doing well. Thank you!"

    elif "my name" in user:
        return f"Your name is {name}"

    elif ("call" in user and "name" in user) or "tell" in user:
        return "You can call me Jarvis"

    elif "age" in user or "born" in user:
        return f"You were born on {birth} and your age is {age}"

    elif "phone" in user:
        return f"My phone number is {phono}"

    else:
        return "Sorry! I didn't understand. Please try again."
#send
def send_message():
    user = in_box.get("1.0", tk.END).strip()
    if user=="":
        return
    chat_box.insert(tk.END,"You: "+ user + "\n")
    reply=bot_reply(user)
    chat_box.insert(tk.END,"Bot: "+ reply +"\n\n")
    in_box.delete("1.0",tk.END)
    chat_box.see(tk.END)
    if user.lower() in("exit","bye"):
        top.after(1000,top.destroy)





# tkinter main window
top=tk.Tk()
top.title("Simple Ai Chatbot")

top.geometry("500x500")
top.configure(bg="black")
t1=tk.Label(top,text="AI CHATOBOT",bg="black",fg="Yellow")
t1.pack(expand=True)
frame=tk.LabelFrame(top,text="Chat Area",fg="Yellow",bg="black")
frame.pack(pady=20)
chat_box=tk.Text(frame,height=18,width=50,fg="red")
chat_box.pack()
#user input frame
in_frame=tk.LabelFrame(top,text="User Input" ,bg="black",fg="Yellow")
in_frame.pack(pady=10)
in_box=tk.Text(in_frame,height=3,width=50,fg="red")
in_box.pack()
b1=tk.Button(top,text="Send",command=send_message,bg="red",fg="yellow", height=3,pady=50)
b1.pack(pady=10)
top.mainloop()
