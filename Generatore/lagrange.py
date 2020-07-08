import argparse


def read_problem(problem_instance):
    str_problem = ''
    with open(problem_instance, mode='r') as myfile:
        for line in myfile:
            if line.startswith('c'):
                str_problem+=line
            if line.startswith('u'):
                break
    return str_problem






if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        type=str,
    )

    # parser.add_argument(
    #     "-l",
    #     type=str,
    # )

    args = parser.parse_args()
    str_prob = read_problem(args.p)