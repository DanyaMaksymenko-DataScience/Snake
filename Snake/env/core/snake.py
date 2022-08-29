import numpy as np

from settings.constants import DIRECTIONS, SNAKE_BLOCK


class Snake:
    def __init__(self, head_position, direction_index, length):
        """
        @param head_position: tuple
        @param direction_index: int
        @param length: int
        """
        # Information snake need to know to make the move
        self.snake_block = SNAKE_BLOCK
        self.current_direction_index = direction_index
        # Alive identifier
        self.alive = True
        # Place the snake
        self.blocks = [head_position]
        current_position = np.array(head_position)
        for i in range(1, length):
            # Direction inverse of moving
            current_position = current_position - DIRECTIONS[self.current_direction_index]  # ???
            self.blocks.append(tuple(current_position))

    def step(self, action):
        """
        @param action: int
        @param return: tuple, tuple
        """
        # Check if action can be performed (do nothing if in the same direction or opposite)
        if self.alive and (
                self.current_direction_index != action and
                self.current_direction_index - 2 != action and
                self.current_direction_index + 2 != action):

            self.current_direction_index = action
        # Remove tail
        if action != self.current_direction_index:
            a = 0
        tail = self.blocks[-1]
        self.blocks = self.blocks[:-1]
        # Check new head
        new_head = tuple(self.blocks[0] + DIRECTIONS[action]) if action == self.current_direction_index \
            else tuple(tail + DIRECTIONS[action])
        # Add new head
        self.blocks = [new_head] + self.blocks if action == self.current_direction_index \
            else [new_head] + [tail] + self.blocks[::-1][:-1]
        self.current_direction_index = action
        return new_head, tail
