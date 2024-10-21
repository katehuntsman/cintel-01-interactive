from shiny import App, render, ui
import numpy as np
import matplotlib.pyplot as plt
from palmerpenguins import load_penguins
import seaborn as sns

app_ui = ui.page_fluid(
    ui.panel_title("My App with Histogram and Scatterplot"),
    ui.input_slider("selected_number_of_bins", "Number of bins", 0,100, 20), 
    ui.output_plot("histogram"),
    ui.output_plot("scatterplot")
)

def server(input, output, session):
    @output
    @render.plot(alt = "A histogram")
    def histogram():
        np.random.seed(19680801)
        x= 100 + 15 * np.random.randn(437)
        plt.hist(x, input.selected_number_of_bins(), density=True)
        plt.xlabel("Number of Bins")
        plt.ylabel("Frequency")
    @render.plot(alt="My Histogram Chart")
    def scatterplot():
        penguins=load_penguins()
        g=sns.lmplot(
            x="flipper_length_mm",
            y="body_mass_g",
            hue="species",
            height=7,
            data=penguins
        )
        g.set_xlabels("Flipper Length")
        g.set_ylabels("Body Mass")
        return g


app = App(app_ui,server,debug=True)