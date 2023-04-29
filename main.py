class Problem2:

    def __init__(self, input) -> None:
        self.root = input

    def generate_tree(self) -> str:
        result = []
        self.preorder_generate(0, result)
        return ''.join(result)

    def preorder_generate(self, index, out):
        if index >= len(self.root):
            return False
        if self.root[index] == None:
            return False
        out.append(str(self.root[index]))
        left_tree_index = index*2+1
        right_tree_index = (index+1)*2
        out_l = []
        out_r = []
        result_l = self.preorder_generate(left_tree_index, out_l)
        result_r = self.preorder_generate(right_tree_index, out_r)
        if result_l is False and result_r is False:
            pass
        elif result_l is False and result_r is True:
            out.append('(')
            out.append(')')
            out.append('(')
            out.extend(out_r)
            out.append(')')
        elif result_l is True and result_r is False:
            out.append('(')
            out.extend(out_l)
            out.append(')')
        else:
            out.append('(')
            out.extend(out_l)
            out.append(')')
            out.append('(')
            out.extend(out_r)
            out.append(')')

        return True

if __name__ == '__main__':
    root1 = [1,2,3,4]
    solution1 = Problem2(root1)
    assert(solution1.generate_tree() == "1(2(4))(3)")

    root2 = [1, 2, 3, None, 4]
    solution2 = Problem2(root2)
    assert(solution2.generate_tree() == "1(2()(4))(3)")