#!/usr/bin/env python3
# coding=utf-8

import inkex
from simpletransform import computePointInNode
import simplestyle

class Raport(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option("-c", "--count",
                        action="store", type="int",
                        dest="count", default=24,
                        help="Count raport")
                        
        self.OptionParser.add_option("-w", "--width",
                        action="store", type="float",
                        dest="width", default=20.0,
                        help="width")
                        
        self.OptionParser.add_option("--height",
                        action="store", type="float",
                        dest="height", default=20.0,
                        help="height")

    def ornament(self, coords_left, coords_right, coords_top, coords_bottom):
        rapport_str = ''

        triangle_left = 'M{},{} L{},{} L{},{} z '.format(
            coords_left['x1'], 
            coords_left['y1'], 
            coords_left['x2'], 
            coords_left['y2'], 
            coords_left['x3'], 
            coords_left['y3']
        )
        
        triangle_right = 'M{},{} L{},{} L{},{} z '.format(
            coords_right['x1'], 
            coords_right['y1'], 
            coords_right['x2'], 
            coords_right['y2'], 
            coords_right['x3'], 
            coords_right['y3']
        )
        
        triangle_top = 'M{},{} L{},{} L{},{} z '.format(
            coords_top['x1'], 
            coords_top['y1'], 
            coords_top['x2'], 
            coords_top['y2'], 
            coords_top['x3'], 
            coords_top['y3']
        )
        
        triangle_bottom = 'M{},{} L{},{} L{},{} z '.format(
            coords_bottom['x1'], 
            coords_bottom['y1'], 
            coords_bottom['x2'], 
            coords_bottom['y2'], 
            coords_bottom['x3'], 
            coords_bottom['y3']
        )
        
        return rapport_str + triangle_left + triangle_right + triangle_top + triangle_bottom

    def effect(self):
    
        count = self.options.count
        width = self.options.width
        height = self.options.height
        
        parent = self.current_layer

        rapport_str = ''
        

        for i in range(1, count+1):
            coords_left = {
                'x1' : width*i-width,
                'y1' : 0,
                    
                'x2' : width*i-width/2 - 2,
                'y2' : height / 2,
                    
                'x3' : width*i-width,
                'y3' : height,
            }
            
            coords_right = {
                'x1' : width*i,
                'y1' : 0,
                
                'x2' : width*i-width/2 + 2,
                'y2' : height / 2,
                    
                'x3' : width*i,
                'y3' : height,
            }
            if i == 1:
                x1 = width/3
                x2 = width/2
                x3 = width - width/3
            else:
                x1 = (width*i - width) + width/3
                x2 = width*i - width/2
                x3 = width*i - width/3
            coords_top = {
                'x1' : x1,
                'y1' : 0,
                    
                'x2' : x2,
                'y2' : height / 6,
                    
                'x3' : x3,
                'y3' : 0,
            }

            coords_bottom = {
                'x1' : x1,
                'y1' : height,
                    
                'x2' : x2,
                'y2' : height - height / 6,
                    
                'x3' : x3,
                'y3' : height,
            }
            rapport_str += self.ornament(
                coords_left, 
                coords_right,
                coords_top,
                coords_bottom
            )
       
        style = {'fill': 'black'}
        path = {
                'style':simplestyle.formatStyle(style),
                'd': rapport_str
        } 
            
        inkex.etree.SubElement(parent, inkex.addNS('path','svg'), path )
    

if __name__ == '__main__':
    Raport().affect()


