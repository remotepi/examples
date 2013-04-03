#!/usr/bin/env python
# 
# Copyright (c) 2013, Luis Artola
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# - Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

'''
Demostrates how to use respond to mouse motion and mouse button down events
sent wirelessly by Remote Pi application running on iPhone, iPad and iPod
touch. Displays a green circle on a window that follows the mouse cursor
as you drag your finger on your iOS device surface. Tap to pin a circle at
the current mouse pointer position.

Checkout video at http://vimeo.com/63726089

Author: luis at remotepi dot io
Created: 2013.04.09
'''


import pygame
import sys

def build_circle(radius):
    '''build_circle(radius) -> (Surface, rect)
    '''
    width = radius*2
    height = radius*2
    color = (0, 255, 0, 0)
    surface = pygame.Surface((width,height))
    rect = pygame.draw.circle(surface, color, (radius, radius), radius)
    return surface, rect

def main():

    # Initialize window to display interactive green circle
    pygame.init()
    width = 800
    height = 640
    background = (0, 0, 0)
    screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
    radius = 50
    surface, rect = build_circle(radius)
    rect.x = width/2
    rect.y = height/2
    pins = []

    # Event loop
    done = False
    while not done:
        # This is where you respond to regular keyboard and mouse events
        # The Remote Pi app and driver installed on your Raspberry Pi or
        # Linux computer will take care of feeding these events as you
        # use the app on your iPhone, iPad or iPod touch
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEMOTION:
                # Have the center of the circle follow the mouse pointer
                x, y = event.pos
                rect.x = x - radius
                rect.y = y - radius
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Pin a green circle on every position you tap
                if event.button == 1:
                    pins.append( event.pos )
        # Clear display
        screen.fill(background)
        # Draw pinned circles
        for pin in pins:
            x = pin[0] - radius
            y = pin[1] - radius
            screen.blit(surface, (x, y, radius*2, radius*2))
        # Draw green circle that follows the mouse pointer
        screen.blit(surface, rect)
        pygame.display.flip()

    pygame.quit()
    return 0

if __name__ == '__main__':
    result = main()
    sys.exit(result)

