from copy import deepcopy

class DeepCopy:
    def lst_lst(self):

        lst = [[1,2],[3,4],[5,6],[7,8]]

        print(lst)

inst = DeepCopy()
inst1 = deepcopy(inst)

print(inst.lst_lst())
print(inst1.lst_lst())
