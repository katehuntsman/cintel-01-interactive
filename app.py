from shiny import App, render, ui
import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
data = np.random.randn(1000)

app_ui = ui.page_fluid(
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20),
    ui.output_plot("histogram_plot")
)

def server(input, output):
    @output
    @render.plot
    def histogram_plot():
        plt.figure(figsize=(8, 5))
        plt.hist(data, bins=input.selected_number_of_bins(), density=True, alpha=0.7)
        plt.title('Histogram of Random Data')
        plt.xlabel('Value')
        plt.ylabel('Density')
        plt.grid(True)
        plt.show()

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
