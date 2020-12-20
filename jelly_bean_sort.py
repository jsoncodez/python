"""
File: jelly_bean_sort.py
Author: Jason Song
Date: 12/9/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Sorts box of jelly beans, grouping based on color and sorting based on quantity from smallest to largest amount.
"""

def color_count(list_of_colors):
    """
    :param list_of_colors: list of all the jelly beans in the box
    :return: list of pairs [color, quantity]

    Helper function to categorize the jellybeans and count of each category.
    """

    sorted_beans = []
    # list of unique colors with no repeats
    for color in list_of_colors:
        if color not in sorted_beans:
            sorted_beans.append(color)

    # count of frequency of each category
    print(list_of_colors)
    for category_color in range(len(sorted_beans)):
        sorted_beans[category_color] = [sorted_beans[category_color], 0]
        for color in list_of_colors:
            if color == sorted_beans[category_color][0]:
                sorted_beans[category_color][1] += 1

    print(sorted_beans)
    return sorted_beans


def swap(list_of_colors, x, y):

    temp = list_of_colors[x]
    list_of_colors[x] = list_of_colors[y]
    list_of_colors[x] = list_of_colors[y]
    list_of_colors[y] = temp


def jelly_bean_sort(list_of_colors):

    for index in range(len(list_of_colors)):
        min_index = index
        for color_count in range(index + 1, len(list_of_colors)):
            if list_of_colors[min_index][1] > list_of_colors[color_count][1]:
                min_index = color_count
        swap(list_of_colors, index, min_index)
    return list_of_colors


if __name__ == '__main__':
    list_of_colors = ['blue', 'red', 'green', 'red', 'yellow', 'green', 'red', 'blue', 'red', 'green', 'yellow', 'yellow', 'white', 'orange', 'red', 'red', 'pink', 'pink', 'cyan', 'cyan']

    print(jelly_bean_sort(color_count(list_of_colors)))









