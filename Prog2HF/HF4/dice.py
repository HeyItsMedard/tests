import random


class Die:
    def __init__(self, n_faces=6):
        if n_faces < 2:
            raise ValueError()
        self.n_faces = n_faces

    def roll(self) -> int:
        return random.randint(1, self.n_faces)

class DieWithMemory(Die):
    """Olyan dobókocka, amivel lehetetlen kétszer egymás után ugyanazt a számot dobni.

    A roll metódus implementálásához ne használd a random modult, hanem az ősosztály
    roll metódusát hívd addig, míg az előző dobástól különböző értéket nem kapsz.
    """
    def __init__(self, n_faces=6):
        super().__init__(n_faces)
        self.last_roll = None

    def roll(self) -> int:
        while True:
            result = super().roll()
            if result != self.last_roll:
                self.last_roll = result
                return result

class DieWithSharedMemory(Die):
    """Olyan dobókocka, ami kapcsolatban áll a többi azonos típusú objektummal, és nem
    lehet vele ugyanazt a számot dobni, mint ami az utolsó dobás eredménye volt
    bármelyik DieWithSharedMemory típusú dobókockával.

    A roll metódus implementálásához ne használd a random modult, hanem az ősosztály
    roll metódusát hívd addig, míg az előző dobástól különböző értéket nem kapsz.
    """
    _shared_memory = set()

    def __init__(self, n_faces=6):
        super().__init__(n_faces)
        self.last_roll = None
        DieWithSharedMemory._shared_memory.add(None)

    def roll(self) -> int:
        while True:
            result = super().roll()
            if self.last_roll is not None:
                if self.last_roll in DieWithSharedMemory._shared_memory:
                    DieWithSharedMemory._shared_memory.remove(self.last_roll)
            if result not in DieWithSharedMemory._shared_memory:
                DieWithSharedMemory._shared_memory.add(result)
                self.last_roll = result
                return result

if __name__ == "__main__":
    die = DieWithMemory(6)
    results = [die.roll()]
    for _ in range(1000):
        results.append(die.roll())
        assert results[-1] != results[-2], "Hiba: kétszer egymás után ugyanazt a számot dobtad!"
    dice = [DieWithSharedMemory(4), DieWithSharedMemory(4)]
    for _ in range(1000):
        a, b = (die.roll() for die in dice)
        assert a != b, "Hiba: két dobókockával egymás után ugyanazt a számot dobtad!"
