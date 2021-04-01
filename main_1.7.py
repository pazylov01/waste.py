trata = 0
def func(day):
    global trata
    trata += day

func(12)
func(45)


def func_2(*trata):
    c = 0
    for day in trata:
        c += day
    return c

print(func_2(2,6,5))        
