
import pathlib
import random
import pygame
from PIL import Image
from platform import system
from treys import Card as tCard
from treys import Evaluator
from enum import Enum


#check if run on windows or mac
project_folder = str(pathlib.Path(__file__).parent.parent.resolve())
sys = system()
if sys == "Darwin":
    PIC_FOLDER = project_folder + "/assets/"
elif sys == "Windows":
    PIC_FOLDER = project_folder + r"\assets" + "\\"
else:
    PIC_FOLDER = ""
    raise ValueError()


class Suit(Enum):
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
    SPADES = 4



class Card:
    def __init__(self,num: int ,suit: str | int ) -> None:
        """

        Args:
            num (int): num is a number between 1 - 13 represting cards between A, 2, ..., 10, J, Q, K
            suit (Suit): one of four options - DIAMONDS, CLUBS, HEARTS, SPADES
        
        Raises:
            ValueError, if the above condition aren't met
        """
        
        if num < 1 or num > 13:
            raise ValueError("Num value should be between 1,13 not " ,num)
        
        self.__num = num
        
        if type(suit) == str:
            suit_map = {
                'D': Suit.DIAMONDS,
                'C': Suit.CLUBS,
                'H': Suit.HEARTS,
                'S': Suit.SPADES
            }
            if suit not in suit_map:
                raise ValueError("Invalid suit - ", suit)
            self.__suit = suit_map[suit] #type: ignore
        elif type(suit) == int:
            if suit < 1 or suit > 4:
                raise ValueError("Invalid suit - ", suit)
            self.__suit = Suit(suit) #type: ignore
        

    def __repr__(self) -> str:
        return str(self.__num) + str(self.__suit)

    def to_tCard(self) -> int:
        st_arr = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
        suit_arr = ['d','c','h','s']
        st = st_arr[self.__num - 1] + suit_arr[self.__suit.value - 1]
        return tCard.new(st)
        
    def get_suit(self) -> Suit:
        return self.__suit
    
    def get_str_suit(self) -> str:
        suit_map = {
            Suit.DIAMONDS: 'D',
            Suit.CLUBS: 'C',
            Suit.HEARTS: 'H',
            Suit.SPADES: 'S'
        }
        return suit_map[self.__suit]

    def get_num(self) -> int:
        return self.__num
    
    def get_picture(self) -> pygame.surface.Surface:
        im = Image.open(PIC_FOLDER + "deck.png")    
        
        top = (Suit.SPADES.value - 1, Suit.CLUBS.value - 1, Suit.DIAMONDS.value - 1, Suit.HEARTS.value - 1).index(self.__suit.value - 1) * 59
        if (self.__suit == Suit.DIAMONDS):
            top += 2
        if (self.__suit == Suit.HEARTS):

            top += 4
        bottom = top + 59
        
        if (self.__num) == 1: # Ace
            left,right = 0,39
        else:
            left = (14 - self.__num) * 40 - 1
            right = left + 40
        if self.__num <= 5:
            left += 1
            right += 1


        
        im1 = im.crop((left,top,right,bottom))

        if im1.mode != "RGBA":
            im1 = im1.convert("RGBA")


        return pygame.image.fromstring(im1.tobytes(),im1.size,"RGBA")
