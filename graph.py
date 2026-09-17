import time
import matplotlib.pyplot as plt


def visual_linear_search(data, target):
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 5))

    # Run the linear search loop
    for index, value in enumerate(data):
        # Clear the previous bars to update colors
        ax.clear()

        # Build a list of colors depending on the state of the search
        colors = []
        for i in range(len(data)):
            if i == index:
                colors.append("red")  # Currently checking
            elif data[i] == target and i <= index:
                colors.append("green")  # Target found!
            else:
                colors.append("skyblue")  # Unchecked or others

        # Draw the bar chart
        bars = ax.bar(range(len(data)), data, color=colors, edgecolor="black")
        ax.bar_label(bars, fmt="%d", padding=3)  # Add values on top of bars

        # Customize labels and title
        ax.set_title(
            f"Linear Search: Checking index {index} (Value: {value})", fontsize=14
        )
        ax.set_xlabel("Array Index", fontsize=12)
        ax.set_ylabel("Value", fontsize=12)
        ax.set_xticks(range(len(data)))

        # Pause to create an animation effect
        plt.pause(0.6)

        # If the target is found, break and keep the final frame
        if value == target:
            ax.set_title(
                f"Target {target} FOUND at index {index}!", fontsize=14, color="green"
            )
            plt.draw()
            plt.show()
            return index

    # If the target is not found after looking through the entire list
    ax.set_title(f"Target {target} NOT FOUND in the list", fontsize=14, color="darkred")
    plt.draw()
    plt.show()
    return -1


# Sample data and target value
sample_list = [14, 45, 23, 89, 52, 11, 76, 38]
target_value = 52

# Run the visualization
visual_linear_search(sample_list, target_value)
