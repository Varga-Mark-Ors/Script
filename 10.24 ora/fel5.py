#!/usr/bin/env python3

class Rect():
    
    def __init__(self, v1, v2) -> None:
        self.height = v1
        self.widths = v2
        
    def width(self, value):
        self.widths = value
    
    def __str__(self):
        return f"Rectangle ({self.height},{self.widths})"
    
def main():
    
    rect = Rect(50, 10)
    rect.width(60)
    print(rect)
    
if __name__=="__main__":
    main()