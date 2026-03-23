def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def draw_grid():
    do_twice(print_row)
    print_beams()

print("\n--- 2x2 Grid ---")
draw_grid()

def print_beams_4():
    do_four(print_beam)
    print('+')

def print_posts_4():
    do_four(print_post)
    print('|')

def print_row_4():
    print_beams_4()
    do_four(print_posts_4)

def draw_grid_4():
    do_four(print_row_4)
    print_beams_4()

print("\n--- 4x4 Grid ---")
draw_grid_4()
