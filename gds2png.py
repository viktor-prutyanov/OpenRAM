#!/usr/bin/python3

import gdstk
import cairosvg

def gds2d_view(gds_file, scale=10):
    svg = gds_file.split(".")[0] + ".svg"
    png = gds_file.split(".")[0] + ".png"
    library = gdstk.read_gds(gds_file)
    top_cells = library.top_level()
    top_cells[0].write_svg(svg)
    cairosvg.svg2png(url=svg, write_to=png, scale=scale)


if __name__ == "__main__":
    import sys
    gds2d_view(sys.argv[1])