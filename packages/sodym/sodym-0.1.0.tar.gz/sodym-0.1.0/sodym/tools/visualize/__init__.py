from tools.config import cfg
from tools.paths import figure_path
from matplotlib import pyplot as plt
import plotly.graph_objects as go
from tools.config import cfg
from tools.visualize.sankey import visualize_mfa_sankey


visualization_routines = {}

def register_for_visualization(name):
    def decorator(routine):
        visualization_routines[name] = routine
        return routine
    return decorator

def visualize_mfa(mfa):
    for name, routine in visualization_routines.items():
        if cfg.visualize[name]['do_visualize']:
            routine(mfa)

# Here, some general, non-model-specific display names can be set
display_names = {
    'my_variable': 'My Variable',
}

def update_display_names(display_names_in):
    display_names.update(display_names_in)

def dn(st):
    return display_names[st] if st in display_names else st


def show_and_save_pyplot(fig, name):
    if cfg.do_save_figs:
        plt.savefig(figure_path(f"{name}.png"))
    if cfg.do_show_figs:
        plt.show()

def show_and_save_plotly(fig: go.Figure, name):
    if cfg.do_save_figs:
        fig.write_image(figure_path(f"{name}.png"))
    if cfg.do_show_figs:
        fig.show()
