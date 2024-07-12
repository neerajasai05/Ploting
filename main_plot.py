import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil

#base_path = 'C:\\Users\\neera\\OneDrive\\Desktop\\Projects_Data Science'
base_path = os.path.dirname(os.path.abspath(__file__))
base_path_output = f'{base_path}/output'

def clear_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def statistics(data):
        numeric_columns = data.select_dtypes(include=['number']).columns
        #print(numeric_columns)
        mean_value = data.mean(numeric_only= True)
        median_value = data.median(numeric_only= True)
        mode_value = data.mode().iloc[0]         
        # Using f-strings to format the output
        print("---------------------")
        print(f"Mean value for each column: \n{mean_value}")
        print("---------------------")
        print(f"Median value for each column: \n{median_value}")
        print('---------------------')
        print(f"Mode value for each column: \n{mode_value}")     
        for column in numeric_columns:
            total_sum = data[column].sum()     
            std_value = data[column].std()     
            count_value = data[column].count()
            max_value = data[column].max()
            min_value = data[column].min()
            print("-----------------")
            print(f"Total sum of '{column}': {total_sum}")
            print(f"Standard Deviation of '{column}': {std_value}")
            print(f"Count value of '{column}': {count_value}")
            print(f"Max Value of '{column}': {max_value}")
            print(f"Min Value of '{column}': {min_value}")
        return mean_value, median_value, mode_value


def histogram_plot(data):
    # Select only numeric columns
    numeric_columns = data.select_dtypes(include=['number']).columns
    #print(numeric_columns)
    
    # Plot histogram for each numeric column
    for column in numeric_columns:
        #creates a new figure for the plot. Each time through the loop, a new figure is created to ensure that each histogram is plotted in its own separate window or plot.
        plt.figure(figsize=(6, 6))
        data[column].plot(kind='hist', bins=20, edgecolor='black')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {column}')
        plt.savefig(f'{base_path_output}/Output_{column}_Historam_Plot.png')
        plt.close()
        #plt.show()
        


def scatter_plot(data):
    # Select only numeric columns
    numeric_columns = data.select_dtypes(include=['number']).columns
    colors = ['g','r']
    # Create a color map
    color_map = [colors[i % len(colors)] for i in range(len(data))]
    for column1 in numeric_columns:
        for column2 in numeric_columns:
                if column1 != column2:
                    plt.figure(figsize=(6, 6))
                    plt.scatter(data[column1], data[column2], c=color_map, label='Data Points')
                    plt.title(f"Scatter Plot of: {column1} and {column2}")
                    plt.xlabel(column1)
                    plt.ylabel(column2)
                    plt.legend()
                    plt.grid(True)
                    plt.savefig(f'{base_path_output}/Output_{column1}{column2}_Scatter_plot.png')
                    plt.close()
                    #plt.show()
                    

def line_plot(data):
    # Select only numeric columns
    numeric_columns = data.select_dtypes(include=['number']).columns
    # Plot histogram for each numeric column
    for column in numeric_columns:
        plt.figure(figsize=(6, 6))
        numeric_data = data.select_dtypes(include='number')
        #print(numeric_data) numeric_data.index,
        plt.plot(numeric_data[column], color='green' , label=column, linestyle='-', marker='o')
        plt.title('Line Plot')
        plt.xlabel('Index')
        plt.ylabel(column)
        plt.legend()
        plt.grid(True)
        plt.savefig(f'{base_path_output}/Output_{column}_LinePlot.png')
        plt.close()
        #plt.show()


def box_plot(data):
    # Select only numeric columns
    numeric_columns = data.select_dtypes(include=['number']).columns
    # Plot histogram for each numeric column
    numeric_data = data.select_dtypes(include='number')
    #print(numeric_data)
    for column in numeric_columns:
        plt.figure(figsize=(8, 8))
        plt.boxplot(numeric_data[column])   #, tick_labels=numeric_columns
        plt.title('Box Plot')
        plt.xlabel(column)
        plt.ylabel('Values')
        plt.grid()
        plt.savefig(f'{base_path_output}/box_{column}.png')
        plt.close()
    #plt.show()
    

def main():
    file_path = input("Enter path:")
    base = os.path.splitext(file_path)[0]
    excel_file_path = f"{base}.xlsx"
    data = pd.read_csv(file_path, delimiter=',', engine='python' )
    data.to_excel(excel_file_path, index=False)
    #print(data)
    mean_value, median_value, mode_value = statistics(data)
    output_dir = os.path.join(base_path , 'output')
    os.makedirs(output_dir, exist_ok=True)
    clear_directory(output_dir)
    histogram_plot(data)
    scatter_plot(data)
    line_plot(data)
    box_plot(data)
    
    
main()



    