#!/bin/python3

import sys

def progress(accents, colors):
	print('\t<div class="col col-33">')
	print('\t\t<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 768 480" height="100%">')
	dec = 480/(len(colors))
	h = 480
	for e in reversed(colors): 
		print('\t\t\t<path fill=' + e + ' d="M0 0h768v' + str(int(h)) + 'H0z"/>')
		h -= dec
	print('\t\t\t<polygon points="0,0 120,0 360,240 120,480 0,480" style="fill:' + accents[0] + '"/>')
	print('\t\t\t<polygon points="0,0 60,0 300,240 60,480 0,480" style="fill:' + accents[1] + '"/>')
	print('\t\t\t<polygon points="0,0 240,240 0,480" style="fill:' + accents[2] + '"/>')
	print('\t\t\t<polygon points="-60,0 180,240 -60,480" style="fill:' + accents[3] + '"/>')
	print('\t\t\t<polygon points="-120,0 120,240 -120,480" style="fill:' + accents[4] + '"/>')
	print('\t\t</svg>')
	print('\t</div>')

def polyamory(accents, colors):
	print('\t<div class="col col-33">')
	print('\t\t<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 768 480" height="100%">')
	dec = 480/(len(colors))
	h = 480
	for e in reversed(colors): 
		print('\t\t\t<path fill=' + e + ' d="M0 0h768v' + str(int(h)) + 'H0z"/>')
		h -= dec
	print('<path d="m 130.2,112.8 c 0,-2.6 0.8,-4.8 1.5,-7.5 l 6,-21 c 0.5,-1.8 0.3,-2.7 -1.9,-2.7 -6.6,0 -9.9,1.8 -12.3,9 -0.2,0.5 -0.2,1.4 -1,1.4 -0.8,0 -1.4,-1.3 -1.4,-3.8 0,-5.3 3.8,-12.9 16.3,-12.9 4.4,0 9.1,0.3 13.5,0.6 3.4,0.2 6.5,0.4 9.3,0.4 2.7,0 4.6,-0.9 6,-1.6 1.1,-0.7 1.7,-1.2 2.2,-1.2 1,0 1.2,0.8 1.2,3 0,2.8 -2.1,6.4 -3.6,6.4 -2.6,0 -5.7,-0.4 -7,-0.4 -2.1,0 -2.9,0.3 -3.3,3 -0.4,2.8 -2.3,14.5 -2.3,18.4 0,2.4 1.7,3.4 3.6,3.5 1.1,0.1 2.3,-0.1 3.3,-0.5 0.8,-0.3 1.3,-0.6 1.5,-0.6 0.9,0 1,0.5 1,1.5 0,3.3 -2.2,8.3 -7,8.3 -3.3,0 -6.2,-3.2 -6.2,-9.6 0,-4.8 2.5,-18.6 2.5,-21.7 0,-1.2 -0.6,-2.4 -1.5,-2.4 l -7.5,-0.3 c -1.3,-0.1 -2,0.5 -2.4,2 -3,11.3 -3.8,18.5 -4,23.2 -0.1,3.2 0.2,5.2 0.4,6.4 0.3,1.7 0.4,2.6 -1,2.6 -1.3,0 -5.9,-2 -5.9,-3.5 z" fill="' + accents[0] + '" transform="scale(2.5)"/>')
	print('\t\t</svg>')
	print('\t</div>')

def tricolor_polyamory(accents, colors):
	print('\t<div class="col col-33">')
	print('\t<!-- Source https://www.polyamproud.com/flag <3<3-->')
	print('\t\t<svg id="Layer_2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 899.36 555.59" height="100%"><g id="Layer_1-2"><rect y="370.39" width="924.09" height="185.2" transform="translate(924.09 925.98) rotate(180)" style="fill:#340c46;"/><rect y="185.2" width="924.09" height="185.2" transform="translate(924.09 555.59) rotate(180)" style="fill:#e50051;"/><rect y="0" width="924.09" height="185.2" transform="translate(924.09 185.2) rotate(180)" style="fill:#009fe3;"/><polygon points="185.2 0 0 0 0 555.59 370.39 185.2 185.2 0" style="fill:#fff;"/><path d="M89.62,94.72h0c-23.89,23.89-23.89,62.64,0,86.53l3.82,3.82h0s-4.07,4.07-4.07,4.07c-23.89,23.89-23.89,62.64,0,86.53h0c23.89,23.89,62.64,23.89,86.53,0l4.07-4.07,86.53-86.53,.79-.79-87.09-85.52-.23-.23-3.82-3.82c-23.89-23.89-62.64-23.89-86.53,0Z" style="fill:#fcbf00;"/></g></svg>')
	print('\t</div>')

def intersex(accents, colors):
	print('\t<div class="col col-33">')
	print('\t\t<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 768 480" height="100%">')
	print('\t\t\t<path fill="' + colors[0] + '" d="M0 0h768v480H0z"/>')
	print('\t\t\t<circle cx="50%" cy="50%" r="137.6px" stroke="' + accents[0] + '" stroke-width="40px" fill="' + colors[0] + '" />')
	print('\t\t</svg>')
	print('\t</div>')

def bisexual(accents, colors):
	print('\t<div class="col col-33">')
	print('\t\t<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 768 480" height="100%">')
	print('\t\t\t<path fill="' + colors[0] + '" d="M0 0h768v480H0z"/>')
	print('\t\t\t<path fill="' + colors[1] + '" d="M0 0h768v288H0z"/>')
	print('\t\t\t<path fill="' + colors[2] + '" d="M0 0h768v192H0z"/>')
	print('\t\t</svg>')
	print('\t</div>')

def demisexual(accents, colors):
	print('\t<div class="col col-33">')
	print('\t\t<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 768 480" height="100%">')
	print('\t\t\t<path fill="' + colors[0] + '" d="M0 0h768v480H0z"/>')
	print('\t\t\t<path fill="' + colors[1] + '" d="M0 0h768v288H0z"/>')
	print('\t\t\t<path fill="' + colors[2] + '" d="M0 0h768v192H0z"/>')
	print('\t\t\t<polygon points="0,0 306,240 0,480" style="fill:' + accents[0] + '"/>')
	print('\t\t</svg>')
	print('\t</div>')

def color_row(col):
	# Hex div
	print('\t<div class="col col-10 col-offset-10" style="line-height: ' + lineheight[len(col)] + ';">')
	for e in col:
		print('\t\t<div class="row pride-color" style="--col: ' + e + '">' + e + '</div>')
	print('\t</div>')
	# RGB div
	print('\t<div class="col col-20 col-offset-5" style="line-height: ' + lineheight[len(col)] + ';">')
	for e in col:
		print('\t\t<div class="row pride-color" style="--col: ' + e + '">' + str(tuple(int(e.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))) + '</div>')
	print('\t</div>')

def bar_flag(accents, colors):
	# svg
	print('\t<div class="col col-33">')
	print('\t\t<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 768 480" height="100%">')
	dec = 480/(len(colors))
	h = 480
	for e in reversed(colors): 
		print('\t\t\t<path fill=' + e + ' d="M0 0h768v' + str(int(h)) + 'H0z"/>')
		h -= dec
	print('\t\t</svg>')
	print('\t</div>')

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
	{	"name": "philadelphia rainbow", 
		"accent": [],
		"color": ["#000000", "#613915", "#ff0000", "#ff8e00", "#ffff00", "#008e00", "#00c0c0", "#400098", "#8e008e"],
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
	{	"name": "demigirl",
		"accent": [], "color": ["#7f7f7f", "#c4c4c4", "#fdadc8", "#ffffff", "#fdadc8", "#c4c4c4", "#7f7f7f"],
		"fn": bar_flag
	},
	{	"name": "demiboy",
		"accent": [], "color": ["#7f7f7f", "#c4c4c4", "#9dd7ea", "#ffffff", "#9dd7ea", "#c4c4c4", "#7f7f7f"],
		"fn": bar_flag
	},
	{	"name": "greysexual",
		"accent": [], "color": ["#810081", "#a4a4a4", "#ffffff", "#a4a4a4", "#810081"],
		"fn": bar_flag
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
	{	"name": "tricolor polyamory",
		"accent": ["#fcbf00", "#ffffff"], "color": ["#009fe3", "#e50051", "#340c46"],
		"fn": tricolor_polyamory
	},
	{	"name": "polyamory",
		"accent": ["#ffff00"], "color": ["#0000ff", "#ff0000", "#000000"],
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
		print('<h3>' + flagname + '</h3>')

		# container
		print('<div class="row"  style="height: 25rem;">')
		
		# svg
		flag["fn"](accents, colors)

		# colors
		color_row(accents + colors)

		# Dimensions
		#print("\t<div class="col col-offset-10">')
		#print("\t\tDIMENSIONS')
		#print("\t</div>')
		
		# end container
		print('</div>')
		
		# delim
		print('<br>')
		print('<hr class="delim">')