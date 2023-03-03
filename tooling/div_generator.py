#!/bin/python3

import sys

#other_flags = {
#	{name: "progress rainbow",  accent: ["#613915", "#000000", "#ffafc7", "#73d7ee", "#ffffff"], color: ["#e50000", "#ff8d00", "#ffee00", "#028121", "#004cff", "#770088"]},
#	{name: "demisexual", accent: ["#000000"], color: ["#ffffff", "#6e0071", "#d3d3d3"]},
#	{name: "poly", accent: ["#ffff00"], color: ["0000ff", "#ff0000", "#000000"]}
#}

bar_flags = [
	{"name": "trans", "color": ["#55cdfd", "#f6aab7", "#ffffff", "#f6aab7", "#55cdfd"]},
	{"name": "classic rainbow",  "color": ["#e50000", "#ff8d00", "#ffee00", "#028121", "#004cff", "#770088"]},
	{"name": "bisexual", "color": ["#d60270", "#9b4f96", "#0038a8"]},
	{"name": "pansexual", "color": ["#ff1c8d", "#ffd700", "#1ab3ff"]},
	{"name": "nonbinary", "color": ["#fcf431", "#fcfcfc", "#9d59d2", "#282828"]},
	{"name": "lesbian", "color": ["#d62800", "#ff9b56", "#ffffff", "#d462a6", "#a40062"]},
	{"name": "agender", "color": ["#000000", "#bababa", "#ffffff", "#baf484", "#ffffff", "#bababa", "#000000"]},
	{"name": "asexual", "color": ["#000000", "#a4a4a4", "#ffffff", "#810081"]},
	{"name": "genderqueer", "color": ["#b57fdd", "#ffffff", "#49821e"]},
	{"name": "genderfluid", "color": ["#fe76a2", "#ffffff", "#bf12d7", "#000000", "#303cbe"]},
	{"name": "intersex", "color": ["#ffd800", "#7902aa"]},
	{"name": "aromantic", "color": ["#3ba740", "#a8d47a", "#ffffff", "#ababab", "#000000"]}
]

lineheight = ["", "25rem", "12.5rem", "8.33rem", "6.25rem", "5rem", "4.167rem", "3.57rem"]

if __name__ == '__main__':
	for flag in bar_flags:
		flagname = flag["name"]
		colors = flag["color"]
		# title
		print("<h3>" + flagname + "</h3>")
		# container
		print("<div class=\"row\"  style=\"height: 25rem;\">")
		# svg
		print("\t<div class=\"col col-33\">")
		print("\t\t<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 777 480\" height=\"100%\">")
		dec = 480/(len(colors))
		h = 480
		for e in reversed(colors): 
			print("\t\t\t<path fill=" + e + " d=\"M0 0h777v" + str(int(h)) + "H0z\"/>")
			h -= dec
		print("\t\t</svg>")
		print("\t</div>")
		# Hex div
		print("\t<div class=\"col col-10 col-offset-10\" style=\"line-height: " + lineheight[len(colors)] + ";\">")
		for e in colors:
			print("\t\t<div class=\"row pride-color\" style=\"--col: " + e + "\">" + e + "</div>")
		print("\t</div>")
		# RGB div
		print("\t<div class=\"col col-20 col-offset-5\" style=\"line-height: " + lineheight[len(colors)] + ";\">")
		for e in colors:
			print("\t\t<div class=\"row pride-color\" style=\"--col: " + e + "\">" + str(tuple(int(e.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))) + "</div>")
		print("\t</div>")
		# Dimensions
		#print("\t<div class=\"col col-offset-10\">")
		#print("\t\tDIMENSIONS")
		#print("\t</div>")
		# end container
		print("</div>")
		# delim
		print("<br>")
		print("<hr class=\"delim\">")