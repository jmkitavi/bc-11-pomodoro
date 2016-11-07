#!/usr/bin/env python
import pygame


# initializing pygame
pygame.init()
timer_width = 280;
timer_height = 120
timer_dsp = pygame.display.set_mode((timer_width, timer_height))
pygame.display.set_caption("Pomodoro Timer")
Font = pygame.font.SysFont('monospace', 15)

#time for timer in h min sec
TotalTime = "00:10:07".split(':')

# convert time to integer
try:
    for i in [0, 1, 2]:		#check if all 3 fields are present h:m:s
        TotalTime[i] = int(TotalTime[i])
except:
    print "The Input wasn't Valid!"
    quit()

# conver time to seconds
#[2] is sec + [1] min*60 + [0] hrs*60*60
TotalTimeSeconds = (TotalTime[2]) + (TotalTime[1] * 60) + (TotalTime[0] * (60*60))


#formatting countdown output
def countdown_time(Time_In_Seconds):
    Hours = Time_In_Seconds / (60 ** 2)
    Minutes = (Time_In_Seconds / 60) % 60
    Seconds = Time_In_Seconds % 60
    return "%i H, %i Min and %i Sec" % (Hours, Minutes, Seconds)


# Wait for the user's input to start the countdown
# raw_input("Press [Enter] to begin the countdown!\n")



#function to quit pygame timer
def quit_timer():
    Events = pygame.event.get()
    for Event in Events:
        if Event.type == pygame.QUIT or (Event.type == pygame.KEYDOWN and Event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()

# Run the Timer
while TotalTimeSeconds > 0:
    quit_timer()
    # pause_timer()
    if TotalTimeSeconds <= 30:
        timer_dsp.fill((255, 4.25 * TotalTimeSeconds, 4.25 * TotalTimeSeconds))
    else:
        timer_dsp.fill((255, 255, 255))
    String = countdown_time(TotalTimeSeconds)
    Font_Position = (
        (0.5 * timer_width) - (0.5 * Font.size(String)[0]),
        (0.5 * timer_height) - (0.5 * Font.size(String)[1])
    )
    Rendered_Font = Font.render(String, 1, (0, 0, 0))
    timer_dsp.blit(Rendered_Font, Font_Position)
    pygame.display.flip()
    pygame.time.wait(1000)
    TotalTimeSeconds -= 1



pygame.quit()
print "The Countdown Finished!"