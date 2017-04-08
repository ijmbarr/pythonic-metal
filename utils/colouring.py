class ColourIter:
    def __init__(self):
        self.n = 0
        # Note: taken from d3 category10 color scale.
        # becasue their colour scale is awesome.
        # see https://github.com/d3/d3-scale/blob/master/src/category10.js
        colours_base = "1f77b4ff7f0e2ca02cd627289467bd8c564be377c27f7f7fbcbd2217becf"
        self.cols = ["#" + colours_base[i*6:(i+1)*6] for i in range(10)]

    def __call__(self):
        self.n += 1
        if self.n >= len(self.cols):
            self.n = 0
        return self.cols[self.n]


def colour_text_html(word, colour):
    return '<span style="color:' + colour + '">' + word + '</span>'

def colour_text_background_html(word, colour):
    return '<span style="color:' + colour + '">' + word + '</span>'