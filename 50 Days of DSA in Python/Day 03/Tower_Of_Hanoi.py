def tower_of_hanoi(n_disks, source, target, auxiliary):
    """
    Solves the Tower of Hanoi problem and prints the moves.

    Args:
        n_disks (int): The number of disks to move.
        source (int): The source rod.
        target (int): The target rod.
        auxiliary (int): The auxiliary rod.

    Returns:
        int: The total number of moves performed.
    """
    move_count = 0

    def solve_hanoi(n, source_rod, target_rod, aux_rod):
        """
        Recursive helper function to solve the Tower of Hanoi problem.

        Args:
            n (int): Number of disks to move.
            source_rod (int): The source rod.
            target_rod (int): The target rod.
            aux_rod (int): The auxiliary rod.
        """
        nonlocal move_count
        if n == 1:
            move_count += 1
            print(f"Move disk {n} from rod {source_rod} to rod {target_rod}")
            return

        # Move n-1 disks from source to auxiliary using target as auxiliary.
        solve_hanoi(n - 1, source_rod, aux_rod, target_rod)

        # Move the nth disk from source to target.
        move_count += 1
        print(f"Move disk {n} from rod {source_rod} to rod {target_rod}")

        # Move n-1 disks from auxiliary to target using source as auxiliary.
        solve_hanoi(n - 1, aux_rod, target_rod, source_rod)

    solve_hanoi(n_disks, source, target, auxiliary)
    return move_count


if __name__ == "__main__":
    # Example usage
    number_of_disks = 3
    source_rod = 1
    target_rod = 3
    auxiliary_rod = 2

    print(f"Solving Tower of Hanoi with {number_of_disks} disks:")
    total_moves = tower_of_hanoi(number_of_disks, source_rod, target_rod, auxiliary_rod)
    print(f"\nTotal moves required: {total_moves}")
