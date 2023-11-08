pip install pyqt5
pip install mysql-connector-python
pip install zpl
pip install zebra
pip install minimalmodbus
pip install jdatetime
pip install matplotlib
pip install bcrypt

def update_plot(self, figure, canvas, data, title):
    figure.clear()
    ax = figure.add_subplot(111)
    ax.plot(data)  # Use appropriate plot method based on your data
    ax.set_title(title)
    canvas.draw()

def update_plots(self):
    # Fetch real-time temperature data from sensors
    # Replace with your actual method of fetching temperature data
    self.update_plot(self.figure1, self.canvas1, self.temperature1_list, "Temp 1")
    self.update_plot(self.figure2, self.canvas2, self.temperature2_list, "Temp 2")
    self.update_plot(self.figure3, self.canvas3, self.temperature3_list, "Temp 3")
    self.update_plot(self.figure4, self.canvas4, self.temperature4_list, "Temp 4")
    self.update_plot(self.figure5, self.canvas5, self.temperature5_list, "Temp 5")
    self.update_plot(self.figure6, self.canvas6, self.temperature6_list, "Temp 6")
    self.update_plot(self.figure7, self.canvas7, self.pressure_min_list, "PSI Min")
    # Continue for the rest of the figures...
