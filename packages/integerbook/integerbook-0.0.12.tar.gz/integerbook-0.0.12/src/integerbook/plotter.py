from matplotlib.figure import Figure
import matplotlib.font_manager as fm

class Plotter:

    def plot(output_path):
        font_path = 'TimesNewRomanExtended.ttf'
        custom_font = fm.FontProperties(fname=font_path)

        fig = Figure()
        ax = fig.subplots()

        ax.text( 0.5, 0.5, "♭I   ♭3", fontproperties=custom_font)

        fig.savefig(output_path)






