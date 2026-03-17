class ContainerWord:

    def solution(self,source,target):
        present = True

        for ch in target:
            if ch not in source:
                present = False
                break

        return present
    
cont_inst = ContainerWord()
print(cont_inst.solution("traviduxtechnology","vridautx"))
