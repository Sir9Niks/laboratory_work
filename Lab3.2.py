def find_common_participants(participants1, participants2, separator=','):

    participants1 = participants1.split(separator)
    participants2 = participants2.split(separator)
    result = list(set(participants1).intersection(participants2))
    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

answer = find_common_participants(participants_first_group, participants_second_group, separator='|')
print('Общие участники: ', answer)


