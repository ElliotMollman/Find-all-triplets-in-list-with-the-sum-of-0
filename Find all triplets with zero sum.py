#Coding question, Find all triplets in list with the sum of 0
#Original answer by Elliot Mollman

#My solution looks like this where I would add the numbers in parentheses. 
#------Loop 1------
#(3), (6), (-4), 1, -2, -1
#(3), 6, (-4), (1), -2, -1
#(3), 6, -4, (1), (-2), -1
#(3), 6, -4, 1, (-2), (-1)
#------Loop 2------
#3, (6), (-4), (1), -2, -1
#3, (6), -4, (1), (-2), -1
#3, (6), -4, 1, (-2), (-1)
#------Loop 3------
#3, 6, (-4), (1), (-2), -1
#And so on........

def check_anwer(len_of_list, List):
        start = 0


        for number_1_position in range(start, len_of_list - 2):
            number_1_value = List[number_1_position]

            if List[number_1_position] == List[len_of_list - 2]:
                break

            for number_2_position in range(number_1_position, len_of_list-1):
                number_2_value = (List[number_2_position + 1])

                if List[number_2_position + 1] == List[len_of_list - 1]:
                    break

                for number_3_position in range(number_2_position, len_of_list):
                    number_3_value = (List[number_3_position + 2])

                    if number_1_value + number_2_value + number_3_value == 0:
                        print(f"sum of {number_1_value}, {number_2_value}, and {number_3_value} = " + str(
                            number_1_value + number_2_value + number_3_value))
                    if List[number_3_position + 2] == List[len_of_list - 1]:
                        print("finished loop")
                        break






List = [3, 6, -4, 1, -2, -1]
len_of_list = len(List)

check_anwer(len_of_list, List)
