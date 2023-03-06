#!/bin/python3

import sys

def progress(accents, colors):
	print("\t<div class=\"col col-33\">")
	print("\t\t<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 777 480\" height=\"100%\">")
	dec = 480/(len(colors))
	h = 480
	for e in reversed(colors): 
		print("\t\t\t<path fill=" + e + " d=\"M0 0h777v" + str(int(h)) + "H0z\"/>")
		h -= dec
	print("\t\t\t<polygon points=\"0,0 120,0 360,240 120,480 0,480\" style=\"fill:" + accents[0] + "\"/>")
	print("\t\t\t<polygon points=\"0,0 60,0 300,240 60,480 0,480\" style=\"fill:" + accents[1] + "\"/>")
	print("\t\t\t<polygon points=\"0,0 240,240 0,480\" style=\"fill:" + accents[2] + "\"/>")
	print("\t\t\t<polygon points=\"-60,0 180,240 -60,480\" style=\"fill:" + accents[3] + "\"/>")
	print("\t\t\t<polygon points=\"-120,0 120,240 -120,480\" style=\"fill:" + accents[4] + "\"/>")
	print("\t\t</svg>")
	print("\t</div>")

def polyamory(accents, colors):
	pass

def intersex(accents, colors):
	print("\t<div class=\"col col-33\">")
	print("\t\t<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 777 480\" height=\"100%\">")
	print("\t\t\t<path fill=\"" + colors[0] + "\" d=\"M0 0h777v480H0z\"/>")
	print("\t\t\t<circle cx=\"50%\" cy=\"50%\" r=\"137.6px\" stroke=\"" + accents[0] + "\" stroke-width=\"40px\" fill=\"" + colors[0] + "\" />")
	print("\t\t</svg>")
	print("\t</div>")

def bisexual(accents, colors):
	print("\t<div class=\"col col-33\">")
	print("\t\t<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 777 480\" height=\"100%\">")
	print("\t\t\t<path fill=\"" + colors[0] + "\" d=\"M0 0h777v480H0z\"/>")
	print("\t\t\t<path fill=\"" + colors[1] + "\" d=\"M0 0h777v288H0z\"/>")
	print("\t\t\t<path fill=\"" + colors[2] + "\" d=\"M0 0h777v192H0z\"/>")
	print("\t\t</svg>")
	print("\t</div>")

def demisexual(accents, colors):
	print("\t<div class=\"col col-33\">")
	print("\t\t<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 777 480\" height=\"100%\">")
	print("\t\t\t<path fill=\"" + colors[0] + "\" d=\"M0 0h777v480H0z\"/>")
	print("\t\t\t<path fill=\"" + colors[1] + "\" d=\"M0 0h777v288H0z\"/>")
	print("\t\t\t<path fill=\"" + colors[2] + "\" d=\"M0 0h777v192H0z\"/>")
	print("\t\t\t<polygon points=\"0,0 306,240 0,480\" style=\"fill:" + accents[0] + "\"/>")
	print("\t\t</svg>")
	print("\t</div>")

def color_row(col):
	# Hex div
	print("\t<div class=\"col col-10 col-offset-10\" style=\"line-height: " + lineheight[len(col)] + ";\">")
	for e in col:
		print("\t\t<div class=\"row pride-color\" style=\"--col: " + e + "\">" + e + "</div>")
	print("\t</div>")
	# RGB div
	print("\t<div class=\"col col-20 col-offset-5\" style=\"line-height: " + lineheight[len(col)] + ";\">")
	for e in col:
		print("\t\t<div class=\"row pride-color\" style=\"--col: " + e + "\">" + str(tuple(int(e.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))) + "</div>")
	print("\t</div>")

def bar_flag(accents, colors):
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

flags = [
	{	"name": "classic rainbow", 
		"accent": [],
		"color": ["#e50000", "#ff8d00", "#ffee00", "#028121", "#004cff", "#770088"],
		"fn": bar_flag
	},
	{	"name": "progress rainbow",
		"accent": ["#000000", "#613915", "#73d7ee", "#ffafc7", "#ffffff"],
		"color": ["#e50000", "#ff8d00", "#ffee00", "#028121", "#004cff", "#770088"],
		"fn": progress
	},
	{	"name": "8-color rainbow", 
		"accent": [],
		"color": ["#ff69b4", "#ff0000", "#ff8e00", "#ffff00", "#008e00", "#00c0c0", "#400098", "#8e008e"],
		"fn": bar_flag
	},
	{	"name": "7-color rainbow", 
		"accent": [],
		"color": ["#ff0000", "#ff8e00", "#ffff00", "#008e00", "#00c0c0", "#400098", "#8e008e"],
		"fn": bar_flag
	},
	{	"name": "trans", 
		"accent": [],
		"color": ["#55cdfd", "#f6aab7", "#ffffff", "#f6aab7", "#55cdfd"],
		"fn": bar_flag
	},
	{	"name": "nonbinary", 
		"accent": [],
		"color": ["#fcf431", "#fcfcfc", "#9d59d2", "#282828"],
		"fn": bar_flag
	},
	{	"name": "intersex",
		"accent": ["#7902aa"],
		"color": ["#ffd800"],
		"fn": intersex
	},
	{	"name": "5-color lesbian", 
		"accent": [],
		"color": ["#d62800", "#ff9b56", "#ffffff", "#d462a6", "#a40062"],
		"fn": bar_flag
	},
	{	"name": "7-color lesbian", 
		"accent": [],
		"color": ["#d52d00", "#ef7627", "#ff9a56", "#ffffff", "#d162a4", "#b55690", "#a30262"],
		"fn": bar_flag
	},	
	{	"name": "pink lesbian", 
		"accent": [],
		"color": ["#a40061", "#b75592", "#d063a6", "#ededeb", "#e4accf", "#c54e54", "#8a1e04"],
		"fn": bar_flag
	},	
	{	"name": "bisexual",
		"accent": [], "color": ["#d60270", "#9b4f96", "#0038a8"],
		"fn": bisexual
	},
	{	"name": "pansexual", 
		"accent": [],
		"color": ["#ff1c8d", "#ffd700", "#1ab3ff"],
		"fn": bar_flag
	},
	{	"name": "genderqueer", 
		"accent": [],
		"color": ["#b57fdd", "#ffffff", "#49821e"],
		"fn": bar_flag
	},
	{	"name": "agender", 
		"accent": [],
		"color": ["#000000", "#bababa", "#ffffff", "#baf484", "#ffffff", "#bababa", "#000000"],
		"fn": bar_flag
	},
	{	"name": "asexual", 
		"accent": [],
		"color": ["#000000", "#a4a4a4", "#ffffff", "#810081"],
		"fn": bar_flag
	},
	{	"name": "demisexual",
		"accent": ["#000000"], "color": ["#ffffff", "#6e0071", "#d3d3d3"],
		"fn": demisexual
	},
	{	"name": "genderfluid", 
		"accent": [],
		"color": ["#fe76a2", "#ffffff", "#bf12d7", "#000000", "#303cbe"],
		"fn": bar_flag
	},
	{	"name": "bigender", 
		"accent": [],
		"color": ["#c479a2", "#eda5cd", "#d5c7e8", "#ffffff", "#d5c7e8", "#9ac7e8", "#6d82d1"],
		"fn": bar_flag
	},
	{	"name": "polyamory",
		"accent": ["#ffff00"], "color": ["0000ff", "#ff0000", "#000000"],
		"fn": polyamory
	},
	{	"name": "polysexual", 
		"accent": [],
		"color": ["#f61cb9", "#07d569", "#1c92f6"],
		"fn": bar_flag
	},
	{	"name": "aromantic", 
		"accent": [],
		"color": ["#3ba740", "#a8d47a", "#ffffff", "#ababab", "#000000"],
		"fn": bar_flag
	},
	{	"name": "gay men pride", 
		"accent": [],
		"color": ["#078d70", "#26ceaa", "#99e8c2", "#ffffff", "#7bade3", "#5049cb", "#3e1a78"],
		"fn": bar_flag
	}
]

lineheight = ["", "25rem", "12.5rem", "8.33rem", "6.25rem", "5rem", "4.167rem", "3.57rem", "3.125rem", "2.778rem", "2.5rem", "2.273rem", "2.083rem", "1.923rem"]

if __name__ == '__main__':
	for flag in flags:
		flagname = flag["name"]
		colors = flag["color"]
		accents = flag["accent"]
		
		# title
		print("<h3>" + flagname + "</h3>")

		# container
		print("<div class=\"row\"  style=\"height: 25rem;\">")
		
		# svg
		flag["fn"](accents, colors)

		# colors
		color_row(accents + colors)

		# Dimensions
		#print("\t<div class=\"col col-offset-10\">")
		#print("\t\tDIMENSIONS")
		#print("\t</div>")
		
		# end container
		print("</div>")
		
		# delim
		print("<br>")
		print("<hr class=\"delim\">")