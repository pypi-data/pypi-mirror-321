
class CalibrationBoard:
    def __init__(self, width=8, height=8, pattern_size_mm_width=16.25, pattern_size_mm_height=16.25, pattern_type="checker_board"):
        self.pattern_type = pattern_type
        self.width = width
        self.height = height
        self.pattern_size_mm_width = pattern_size_mm_width
        self.pattern_size_mm_height = pattern_size_mm_height


    def dimension(self):
        return self.height, self.width
