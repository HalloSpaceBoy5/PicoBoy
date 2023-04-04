from machine import Pin, PWM
from math import log2, pow
import utime

"""
RPMidi
A PWM-based MIDI player for the Raspberry Pi Pico. Uses GPIO 6-9 for 4 voices.

Created by MikeDEV for use in https://github.com/MikeDev101/oops-all-picos-computer
========================================================================================================

MIDIS must be converted using https://github.com/LenShustek/miditones.

Recommended defaults:
.\miditones.exe -t=4 .\your-midi-here.mid

Copy-paste your-midi-here.c's array data into a list.
MIDI files must not contain more than 4 voices, as any other channel will be ignored by the converter.

========================================================================================================

THE MEOW LICENSE ("MEOW") 1.3 - Last revised Jan 7, 2022.

COPYRIGHT (C) 2022 MikeDEV.

Under this license:

* You are free to change, remove, or modify the above copyright notice.
* You are free to use the software in private or commercial forms.
* You are free to use, copy, modify, and/or distribute the software for any purpose.
* You are free to distribute this software with or without fee.
* Absolutely no patent use is permitted.

With the above conditions, the author(s) of this software do NOT gurantee warranty. As part of this license,
under no circumstance shall the author(s) and/or copyright holder(s) be held liable for any and all forms of
damages.

NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. THE SOFTWARE IS
PROVIDED "AS IS" AND THE AUTHOR(S) DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY
SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
========================================================================================================
"""

class RPMidi:
    def __init__(self):
        self.ch_a_0 = PWM(Pin(15))
        self.ch_a_1 = PWM(Pin(14))
        self.ch_b_0 = PWM(Pin(13))
        self.ch_b_1 = PWM(Pin(12))
        self.stop_all()

    def _pitch(self, freq):
        return (2**((freq-69)/12))*440

    def _duty_cycle(self, percent):
        return round((percent/100)*65535)

    def play_note(self, note, channel, duty):
        if channel == "a0":
            self.ch_a_0.freq(round(self._pitch(note)))
            self.ch_a_0.duty_u16(self._duty_cycle(duty))
        elif channel == "a1":
            self.ch_a_1.freq(round(self._pitch(note)))
            self.ch_a_1.duty_u16(self._duty_cycle(duty))
        elif channel == "b0":
            self.ch_b_0.freq(round(self._pitch(note)))
            self.ch_b_0.duty_u16(self._duty_cycle(duty))
        elif channel == "b1":
            self.ch_b_1.freq(round(self._pitch(note)))
            self.ch_b_1.duty_u16(self._duty_cycle(duty))

    def stop_channel(self, channel):
        if channel == "a0":
            self.ch_a_0.duty_u16(0)
        elif channel == "a1":
            self.ch_a_1.duty_u16(0)
        elif channel == "b0":
            self.ch_b_0.duty_u16(0)
        elif channel == "b1":
            self.ch_b_1.duty_u16(0)
    
    def stop_all_music(self):
        self.done=True
    
    def stop_all(self):
        self.ch_a_0.duty_u16(0)
        self.ch_a_1.duty_u16(0)
        self.ch_b_0.duty_u16(0)
        self.ch_b_1.duty_u16(0)
    
    def _opcodes(self):
        return [0x90, 0x91, 0x92, 0x93, 0x80, 0x81, 0x82, 0x83, 0xf0, 0xe0]
    
    def _play_note_opcodes(self):
        return [0x90, 0x91, 0x92, 0x93]

    def _stop_note_opcodes(self):
        return [0x80, 0x81, 0x82, 0x83]
    
    def _end_song_opcodes(self):
        return [0xf0, 0xe0]
    
    def play_song(self, music, playing=True):
        if type(music) == list:
            self.done = False
            tmp = []
            index = 0
            isReading = False
            opcode = 0x00
            
            self.stop_all() # Silence any existing music
            
            while not self.done:
                if index >= len(music):
                    print("out of range while reading opcode")
                    self.done = True
                    break
                if not playing:
                    return
                else:
                    # Read opcode
                    if music[index] in self._opcodes():
                        opcode = music[index]
                        
                        # Scan for timing data
                        isReading = True
                        tmp = []
                        tmp_index = 1
                        
                        # Read next bytes for timing info
                        while isReading: 
                            if (index + tmp_index) >= len(music):
                                self.done = True
                                break
                            else:
                                if not music[index + tmp_index] in self._opcodes():
                                    tmp.append(music[index + tmp_index])
                                    tmp_index += 1
                                else:
                                    isReading = False
                        
                        # Execute instruction
                        if opcode in self._play_note_opcodes():
                            # Play voice and goto next instruction or play and wait for x milliseconds
                            if len(tmp) > 0:
                                if opcode == 0x90:
                                    self.play_note(tmp[0], "a0", 50)
                                elif opcode == 0x91:
                                    self.play_note(tmp[0], "b0", 50)
                                elif opcode == 0x92:
                                    self.play_note(tmp[0], "a1", 50)
                                elif opcode == 0x93:
                                    self.play_note(tmp[0], "b1", 50)
                                
                                if len(tmp) == 3:
                                    delay = ((tmp[1]*256)+(tmp[2]))
                                    utime.sleep_ms(delay)
                            else:
                                print("expecting at least one entry in tmp, got nothing")
                                self.done = True
                                break
                            index += 1
                            
                        elif opcode in self._stop_note_opcodes():
                            # Mute voice or mute and wait for x milliseconds
                            if opcode == 0x80:
                                self.stop_channel("a0")
                            elif opcode == 0x81:
                                self.stop_channel("b0")
                            elif opcode == 0x82:
                                self.stop_channel("a1")
                            elif opcode == 0x83:
                                self.stop_channel("b1")
                                
                            if len(tmp) >= 2:
                                delay = ((tmp[0]*256)+(tmp[1]))
                                utime.sleep_ms(delay)
                            index += 1
                            
                        elif opcode in self._end_song_opcodes():
                            # End or loop the song
                            if opcode == 0xf0: # Song is over, stop playing.
                                self.done = True
                                break
                            else:
                                self.done = False
                                index = 0 # Song is looping, go back to beginning of song.
                    else:
                        index += 1