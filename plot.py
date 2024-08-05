from PyQt5.QtWidgets import QWidget, QGridLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar

class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # Find and set up the plot widget
        self.plot_widget = self.findChild(QWidget, "frame")
        layout = QGridLayout()
        self.plot_widget.setLayout(layout)

        # Create and configure the plots
        self.figures = []
        self.canvases = []
        self.toolbars = []

        plot_configs = [
            {"row": 1, "col": 0, "title": "Temp 1", "data": "temperature1_list"},
            {"row": 1, "col": 1, "title": "Temp 2", "data": "temperature2_list"},
            {"row": 1, "col": 2, "title": "Temp 3", "data": "temperature3_list"},
            {"row": 3, "col": 0, "title": "Temp 4", "data": "temperature4_list"},
            {"row": 3, "col": 1, "title": "Temp 5", "data": "temperature5_list"},
            {"row": 3, "col": 2, "title": "Temp 6", "data": "temperature6_list"},
            {"row": 5, "col": 0, "title": "PSI Min", "data": "pressure_min_list"},
            {"row": 5, "col": 1, "title": "PSI Max", "data": "pressure_max_list"},
            {"row": 7, "col": 0, "title": "Amp start", "data": "ampstart_list"},
            {"row": 7, "col": 1, "title": "Voltage", "data": "volt_list"},
            {"row": 7, "col": 2, "title": "Amp total", "data": "amptotal_list"}
        ]

        for i, config in enumerate(plot_configs):
            self.create_plot(layout, config, i)

    def create_plot(self, layout, config, index):
        # Create a figure and canvas
        figure = Figure()
        canvas = FigureCanvas(figure)
        self.figures.append(figure)
        self.canvases.append(canvas)

        # Add canvas to layout
        row = config["row"]
        col = config["col"]
        layout.addWidget(canvas, row, col, 1, 1)

        # Create and add toolbar
        toolbar = NavigationToolbar(canvas, self)
        self.toolbars.append(toolbar)
        layout.addWidget(toolbar, row - 1, col, 1, 1)

    def update_plots(self):
        # List of data attributes corresponding to each plot
        data_list = [
            self.temperature1_list, self.temperature2_list, self.temperature3_list,
            self.temperature4_list, self.temperature5_list, self.temperature6_list,
            self.pressure_min_list, self.pressure_max_list, self.ampstart_list,
            self.volt_list, self.amptotal_list
        ]

        for figure, canvas, data in zip(self.figures, self.canvases, data_list):
            figure.clear()
            ax = figure.add_subplot(111)
            ax.plot(data)  # Use appropriate plot method based on your data
            ax.set_title(data)  # Set the title according to the plot data
            canvas.draw()
