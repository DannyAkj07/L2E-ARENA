

def hanoi(n: int, source: str, target: str, helper: str) -> list[tuple[str, str]]:
    if n == 1:
        return [(source, target)]

    moves_one = hanoi(n-1, source, helper, target)
    middle_move = [(source, target)]
    moves_two = hanoi(n - 1, helper, target, source)

    return moves_one + middle_move + moves_two


    
print(hanoi(1, "A", "C", "B"))
print(hanoi(3, "A", "C", "B"))
print(hanoi(5, "A", "C", "B"))
