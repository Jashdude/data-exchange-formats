import csv
from prettytable import PrettyTable
import copy
# Variable to hold the filename
file_name = "freshman_kgs.csv"

# Assignment Question List
question_list = [
"1. Does the sample contain more men or women?",
"2. Which gender has the largest beginning BMI?",
"3. How many observations in the sample, regardless of gender, have a beginning BMI equal to the overall largest BMI?",
"4. Over the course of the school year, which gender experienced the largest average change in weight?"
]

# All answers will be appended to this list.
answer_list = []

# function that takes file name as parameter and returns a list of ordered dictionaries
def gimme_dict(file_name):
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True, delimiter='|')
        dict_list = []
        [dict_list.append(row) for row in reader]
        return dict_list

# Function that returns the average of
def gimme_avg(count,  *args):
    summation = 0
    for arg in args:
        summation += arg
    avg = round(summation/count,2)
    return avg

# function that prints all answers to the assignment questions.
def assignment_tasks(file_name):
    # Get the csv file content by calling gimme_dict function.
    freshman_list = gimme_dict(file_name)
    # necessary variables over the course of the program.
    count_men = count_women = begin_bmi_men = begin_bmi_women = begin_wt_men = begin_wt_women \
        = end_wt_men = end_wt_women = chg_in_wt_men = chg_in_wt_women = 0
    ovrall_lrg_bmi = []
    # Iterates over the list of dictionaries and pulls/computes using required column data.
    for person in freshman_list:
        if person['gender'] == 'M':
            count_men += 1
            begin_bmi_men += float(person['begin_BMI'])
            begin_wt_men += float(person['begin_weight'])
            end_wt_men += float(person['end_weight'])
            chg_in_wt_men += abs(float(person['begin_weight']) - float(person['end_weight']))
        elif person['gender'] == 'F':
            count_women += 1
            begin_bmi_women += float(person['begin_BMI'])
            begin_wt_women += float(person['begin_weight'])
            end_wt_women += float(person['end_weight'])
            chg_in_wt_women += abs(float(person['begin_weight']) - float(person['end_weight']))

        ovrall_lrg_bmi.append(person['begin_BMI'])

    # Solution to question 1.
    if count_women > count_men:
        answer_list.append(f"- Men to Women ratio is {count_men} to {count_women}. Clearly shows count of Women are more!")
        print(f"- Men to Women ratio is {count_men} to {count_women}. Clearly shows count of Women are more! Women Power!")
    else:
        answer_list.append(f"- Men to Women ratio is {count_men} to {count_women}. Clearly shows count of Men are more!")

    # Get Averages for men and women on Begin BMI
    begin_bmi_men =  gimme_avg(count_men, begin_bmi_men)
    begin_bmi_women = gimme_avg(count_women, begin_bmi_women)

    # Solution to question 2.
    if begin_bmi_men > begin_bmi_women:
        answer_list.append(f"- To begin with Men BMI {begin_bmi_men} is greater than Women BMI {begin_bmi_women}")
    else:
        answer_list.append(f"- To begin with Women BMI {begin_bmi_women} is greater than Men BMI {begin_bmi_men}")

    # Solution for question 3 (until line 95).
    # Find max largest beginning BMI regardless of gender.
    overall_largest_bmi = max(ovrall_lrg_bmi)
    # make a deep copy of freshman_list dict which can be compared against the max value.
    # Note: This approach is not required. We can arrive at the matching numbers by getting total match count minus 1.
    # However doing this approach for my learning.
    freshman_list_copy = copy.deepcopy(freshman_list)
    # remove the item from the copy before comparing.
    [freshman_list_copy.remove(item) for item in freshman_list_copy if round(float(item['begin_BMI']), 2) == float(overall_largest_bmi)]


    # Loop through and find if there is a matching Beginning BMI when compared to the Overall largest BMI
    count_bmi = 0
    for prs in freshman_list_copy:
        if round(float(prs['begin_BMI']),2) == float(overall_largest_bmi):
            count_bmi += 1

    answer_list.append(f"- There is {count_bmi} observation(s) in sample, regardless of gender, have a beginning"
          f" BMI equal to the overall largest BMI")

    # Solution for question 4.
    # Find averages of begin & end weight for men and women.
    avg_wt_chg_men = gimme_avg(count_men, chg_in_wt_men)
    avg_wt_chg_women = gimme_avg(count_women, chg_in_wt_women)

    # Compare the average change for men and women.
    if avg_wt_chg_men > avg_wt_chg_women:
        answer_list.append(f"- Men experienced largest average change of {avg_wt_chg_men} "
              f"in weight vs. Women whose change was {avg_wt_chg_women} in weight ")
    else:
        answer_list.append(f"- Women experienced largest average change of {avg_wt_chg_men} "
              f"in weight vs. Men whose change was {avg_wt_chg_women} in weight")

    # Below piece of code helps pretty print the Questions and Answers in a tabular format using Pretty Table.
    result_table = PrettyTable(['Assignment Questions', 'Answers'])
    for x in range(len(question_list)):
        result_table.add_row([question_list[x], answer_list[x]])
        result_table.align = "l"

    print(result_table)

# function call to run the assignment tasks.
assignment_tasks(file_name)