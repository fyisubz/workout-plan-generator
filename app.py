import gradio as gr
from utils.grok_generator import generate_plan_with_grok
from utils.pdf_export import export_to_pdf

with gr.Blocks() as demo:
    gr.Markdown("# Personalized Workout and Diet Plan Generator")
    
    with gr.Row():
        with gr.Column():
            age = gr.Number(label="Age", value=25)
            gender = gr.Dropdown(choices=["Male", "Female", "Other"], label="Gender")
            weight = gr.Number(label="Weight (kg)", value=70)
            height = gr.Number(label="Height (cm)", value=175)
            goal = gr.Dropdown(choices=["Lose Weight", "Build Muscle", "Maintain Fitness"], label="Fitness Goal")
            activity = gr.Dropdown(choices=["Sedentary", "Lightly Active", "Moderately Active", "Very Active"], label="Activity Level")
            diet_pref = gr.Textbox(label = "Dietary Preference/Restriction", placeholder="eg., Vegan, Keto, Carnivore, etc.")
            submit_btn = gr.Button("Generate Plan")

        with gr.Column():
            output = gr.Textbox(label="Generated Plan", lines=20, max_lines=50)
    
    submit_btn.click(fn=generate_plan_with_grok, inputs=[age, gender, weight, height, goal, activity, diet_pref], outputs=output)

    demo.launch()