def check_decision(coordinate_map):

    candidates = [2**i for i in range(9)]
    decision_coordinates = []
    for i in range(3):

        yoko_first_idx = i*3
        yoko_last_idx = (i+1)*3
        yoko_ans = sum(candidates[yoko_first_idx:yoko_last_idx])
        decision_coordinates.append(yoko_ans)

        tate_list = [candidates[i+3*j] for j in range(3)]
        tate_ans = sum(tate_list)
        decision_coordinates.append(tate_ans)

        naname_1_list = [candidates[4*i] for i in range(3)]
        naname_1_ans = sum(naname_1_list)
        decision_coordinates.append(naname_1_ans)

        naname_2_list = [candidates[2*(i+1)] for i in range(3)]
        naname_2_ans = sum(naname_2_list)
        decision_coordinates.append(naname_2_ans)

    naname_1_list = [candidates[4*i] for i in range(3)]
    naname_1_ans = sum(naname_1_list)
    decision_coordinates.append(naname_1_ans)

    naname_2_list = [candidates[2*(i+1)] for i in range(3)]
    naname_2_ans = sum(naname_2_list)
    decision_coordinates.append(naname_2_ans)

    total_val = sum([int(i) for i in coordinate_map])
    if total_val in decision_coordinates:
        return True
    return False

def marubatu_game():
    print('座標を指定してください')
    text = """
    1|2|3
    -----
    4|5|6
    -----
    7|8|9
    """
    print(text)
    coordinate_list = [str(i) for i in range(1, 10)]
    candidates = [2**i for i in range(9)]

    pre_user_input = str()
    pre_user_operations = []

    pos_user_input = str()
    pos_user_operations = []

    err_message = '正しい座標を入力する必要があります。'

    turn_user = 0
    turn_count = 0

    while True:
        if turn_user == 0:
            try:
                mes = 'pre_userの座標を入力'
                pre_user_input = input(mes)
            except Exception as e:
                print(err_messag)
                continue
            if pre_user_input in coordinate_list:
                text = text.replace(str(pre_user_input), "o")
                idx = coordinate_list.index(pre_user_input)
                coordinate_list[idx] = "o"
                pre_user_operations.append(candidates[idx])
                print(text)
                if check_decision(pre_user_operations):
                    print('user0の勝ち')
                    break
            else:
                print(err_message)
                continue
            turn_user = 1
            turn_count += 1
        else:
            try:
                mes = 'pos_userの座標を入力'
                pos_user_input = input(mes)
            except Exception as e:
                print(err_message)
                continue
            if pos_user_input in coordinate_list:
                text = text.replace(str(pos_user_input), "x")
                idx = coordinate_list.index(pos_user_input)
                coordinate_list[idx] = "x"

                pos_user_operations.append(candidates[idx])
                print(text)
                if check_decision(pos_user_operations):
                    print('user1の勝ち')
                    break
            else:
                print(err_message)
                continue
            turn_user = 0
            turn_count += 1
        if turn_count == 9:
            print("引き分けです")
            break
marubatu_game()

