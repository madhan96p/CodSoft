import gradio as gr

def calculator(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                return "❌ Error: Cannot divide by zero."
            result = num1 / num2
        else:
            return "❌ Invalid Operation"

        return f"✅ Result: {result}"
    
    except ValueError:
        return "❌ Error: Invalid input."

# Gradio Interface
iface = gr.Interface(
    fn=calculator,
    inputs=[
        gr.Textbox(label="Enter First Number"),
        gr.Textbox(label="Enter Second Number"),
        gr.Radio(["Addition", "Subtraction", "Multiplication", "Division"], label="Choose Operation")
    ],
    outputs="text",
    title="🧮 Simple Calculator (CodSoft Task 1)",
    description="A clean calculator built with Python + Gradio. Created by Pragadeesh 💡"
)

gr.Markdown("Created by [Pragadeesh](https://pragadeeshfolio.netlify.app)")

iface.launch()
