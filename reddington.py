# reddington by McSpadden
# Copyright (c) 2019 McSpadden
# View https://github.com/mcspadden/reddington/blob/master/README.md for license details

import random, time

quotes = ['Red: I’m not a gumball machine, Lizzy. You don’t get to just twist the handle whenever you want a treat.',
'Keen: And I’m supposed to believe you?\nRed: Of course not! I’m a criminal. Criminals are notorious liars. Everything about me is a lie. But, if anyone will give me a second chance it’s you. The two of us have overcome so much.',
'Keen: A lawyer? How is that gonna help us with this?\nRed: Lawyers find and exploit loopholes. It’s what makes them so loathsome. And Marvin Gerard is the most loathsome of them all. That’s what makes him so invaluable.',
'Red: A farmer comes home one day to find that everything that gives meaning to his life is gone. Crops are burned, animals slaughtered, bodies and broken pieces of his life strewn about. Everything that he loved taken from him – his children. One can only imagine the pit of despair, the hours of Job-like lamentations, the burden of existence. He makes a promise to himself in those dark hours. A life’s work erupts from his knotted mind. Years go by. His suffering becomes complicated. One day he stops – the farmer who is no longer a farmer – sees the wreckage he’s left in his wake. It is now he who burns, he who slaughters, and he knows in his heart he must pay.',
'Keen: I’m sorry, you’re decoding CIA messages on behalf of the Chinese…\nRed: [nods at Elizabeth reassuringly] Now you see? You make it sound like treason, so black and white. It’s not, it’s green.',
'Keen: A man’s life is at stake!\nRed: A man’s life is always at stake. And tragically low stakes at that. I should remind you that I did not offer you my services to help you round up your run of the mill drug lord or what have you. You all seem to be doing a perfectly mediocre job of that on your own. I’m after the big game Lizzie. The ones that matter.',
'Keen: You have a suburban housewife printing fake money out of her garage.\nRed: Mary is an artist. She has a tremendous gift.',
'Red: This is a Colt .45 1911. I can strip and reassemble this weapon in well under two minutes.\nAram: Mr. Reddington, please.\nRed: Once I have it reassembled, I’m gonna reload the mag and if, at that time, your task remains incomplete, I’m gonna empty that mag into your head.\nAram: That’s really messed up.\nRed: Don’t look so stricken. The first shot will kill you.',
'[Christopher Maly jumps through the window, killing himself. Dembe runs over to look, then walks away]\nRed: [Nonchalantly] Okay then.\n[Walks over to window and looks down]\nKeen: What now?\n[Red grabs his coat]\nKeen: What are you doing?\nRed: Putting on my coat.\nKeen: A man just jumped through the window, there’s a body on the sidewalk.\nRed: Yes, and your husband, the police and all the king’s men will be here soon. If you care to stick around and explain, feel free. I for one will not be in attendance.\n[Keen grabs coat and heads for the door]\nRed: Dembe, I’ll get her downstairs. After you’re finished, grab the pretzels.',
'Ressler: We are not going to live through this.\n Red: I think we will.\nRessler: How?\nRed: Have you ever sailed across an ocean, Donald…\nRessler: No.\nRed: …on a sailboat, surrounded by sea with no land in sight, without even the possibility of sighting land for days to come? To stand at the helm of your destiny. I want that, one more time. I want to be in the Piazza del Campo in Siena. To feel the surge as 10 racehorses go thundering by. I want another meal in Paris, at L’Ambroisie, at the Place des Vosges. I want another bottle of wine. And then another. I want the warmth of a woman and a cool set of sheets. One more night of jazz at the Vanguard. I want to stand on the summits and smoke Cubans and feel the sun on my face for as long as I can. Walk on the Wall again. Climb the Tower. Ride the River. Stare at the Frescos. I want to sit in the garden and read one more good book. Most of all I want to sleep. I want to sleep like I slept when I was a boy. Give me that, just one time. That’s why I won’t allow that punk out there to get the best of me, let alone the last of me.']

print('\nreddington by McSpadden')
name = input('What’s your name? ')
print('\n[Calling Red’s phone..]')
time.sleep(2)
print('Dembe, it’s ' + name + '. Put Raymond on the phone.')
time.sleep(1)
print('Raymond, it’s ' + name + '.')
time.sleep(1)
print('Red: Hold up, ' + name + '. I need to handle this.\n[Red puts phone down]')
print('[Background noises]\n' + random.choice(quotes))
