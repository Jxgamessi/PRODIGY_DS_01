import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\Lenovo\Desktop\Prodigy Infotech\Population_sample_data.xlsx'
df = pd.read_excel(file_path)

fig, ax = plt.subplots()
bars = ax.bar(df['Age'], df['Value'], color='red')

ax.set_xlabel('Age')
ax.set_ylabel('Value')
ax.set_title('AGE DISTRIBUTION IN POPULATION') 
def on_bar_click(event):
    if event.inaxes == ax:
        for i, bar in enumerate(bars):
            if bar.contains(event)[0]:
                age = df['Age'].iloc[i]
                value = df['Value'].iloc[i]
                label = f"Age: {age}\nValue: {value}"
                plt.text(age, value, label, ha='center', va='bottom', fontsize=8, color='black')
                fig.canvas.draw_idle()

fig.canvas.mpl_connect('button_press_event', on_bar_click)


plt.show()
