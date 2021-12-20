from AoC2021.day_18 import Pair


def main():
    a = Pair('[[[[4,3],4],4],[7,[[8,4],9]]]')
    b = Pair('[1,1]')
    # actual = a + b
    # print(actual)
    
    tree = Pair('[[[[1,1],[2,2]],[3,3]],[4,4]]')
    tree.print_tree()

if __name__ == '__main__':
    main()
