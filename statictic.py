import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame(columns=['time', 'velocity', 'distance'])

def get_data(space_objects, physical_time):
    if space_objects[0].type == 'planet':
        planet = space_objects[0]
        star = space_objects[1]
    else:
        planet = space_objects[1]
        star = space_objects[0]
    new_row = [float(physical_time), (planet.Vx**2 + planet.Vy**2)**0.5, float(((planet.x - star.x) ** 2 + (planet.y - star.y) ** 2) ** 0.5)]
    df.loc[len(df.index)] = new_row

def save_data():
    df.to_csv("tr.csv")


def save_plots(x_label, y_label):
    fig, ax = plt.subplots()
    df.plot(x=x_label, y=y_label, ax=ax)
    fig.savefig(f'{y_label}({x_label})')
    