import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from palmerpenguins import load_penguins
from shiny import App, ui, render

# Load the Palmer Penguins dataset
penguins = load_penguins()

# Set up the app's UI
app_ui = ui.page_fluid(
    ui.panel_title("Interactive Histogram and Penguin Data"),
    ui.sidebar(
        ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20),  # Change min to 1
        ui.input_select("species", "Select Species", choices=["All"] + list(penguins['species'].dropna().unique()))  # Changed options to choices
    ),
    ui.output_plot("histogram"),
    ui.output_plot("scatterplot")
)

# Define the server logic
def server(input, output, session):  # Added session parameter
    @output.plot(alt="A histogram")
    def histogram():
        np.random.seed(19680801)
        x = 100 + 15 * np.random.randn(437)
        plt.hist(x, bins=input.selected_number_of_bins(), density=True)
        plt.xlabel("Value")
        plt.ylabel("Density")
        plt.title("Histogram of Random Values")

    @output.plot(alt="Penguin Flipper Length vs Body Mass")
    def scatterplot():
        df = penguins
        if input.species() != "All":
            df = df[df['species'] == input.species()]
        
        plt.scatter(df['flipper_length_mm'], df['body_mass_g'], alpha=0.7)
        plt.xlabel("Flipper Length (mm)")
        plt.ylabel("Body Mass (g)")
        plt.title("Flipper Length vs Body Mass for Penguins")
        plt.grid()

# Combine the UI and server into an app
app = App(app_ui, server)

# Run the app without calling app.run() directly in the Shiny environment
