from graphics import Canvas

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Coordinates for the red rectangle
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH
    bottom_y = CANVAS_HEIGHT // 2
    
    # Draw the red rectangle
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, "red")
    
    # Display the canvas
    canvas.mainloop()

if __name__ == '__main__':
    main()
